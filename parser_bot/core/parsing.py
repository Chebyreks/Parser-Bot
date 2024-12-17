import aiohttp

from parser_bot.models.bestoffer import BestOffer
from parser_bot.schemas.bestoffer import BestOfferBase
from typing import Dict
from bs4 import BeautifulSoup
from datetime import date

async def parse_offer(url: str) -> BestOfferBase:
    async with aiohttp.ClientSession() as session:
        async with session.get(url=url) as resp:
            response = await resp.text()
    soup = BeautifulSoup(response, "html.parser")
    container = soup.select("a.tc-item")
    bestoffer_score = 0
    today = date.today()
    bestoffer = BestOfferBase(
        date = today,
        offer = "0",
        url = "0",
        price = 0
    )
    for block in container:
        price_element = block.select_one("div.tc-price")
        price = round((float)(price_element.select_one("div").text.strip().split(" ")[0])) if price_element else None

        account_age_element = block.select_one("div.media-user-info")
        account_age = account_age_element.text.strip() if account_age_element else None
        age = account_age.split(" ")
        if age[-1] == "года" or age[-1] == "лет":
            account_age_num = (float)(age[-2])
        elif age[-1] == "год":
            account_age_num = 1
        elif age[-1] == "месяца" or age[-1] == "месяцев":
            account_age_num = (float)(age[-2]) / 12
        elif age[-1] == "месяц":
            account_age_num = 1

        name_element = block.select_one("div.media-user-name")
        name = name_element.text.strip() if name_element else None

        offer_element = block.select_one("div.tc-desc-text")
        offer = offer_element.text.strip() 

        rating_element = block.select_one("div.media-user-reviews")
        rating_cont = rating_element.select_one("div")
        if rating_cont:
            rating = rating_cont["class"][1].split("-")[-1] if rating_element else None #rating-5 -> 5
        else:
            rating = 0

        reviews_count_element = rating_element.select_one("span.rating-mini-count")
        if reviews_count_element:
            reviews_count = reviews_count_element.text.strip()
        else:
            reviews_count_theory = (rating_element.text.strip().split()[0])
            if (reviews_count_theory == "нет"):
                reviews_count = 0
            else:
                reviews_count = (float)(reviews_count_theory)

        link = block["href"] if block else None

        score = round(1000 * (1 / (int)(price)) + (account_age_num * 1) + ((int)(rating) * 500) + ((int)(reviews_count) * 4), 2) # Вычисление рейтинга 

        if score > bestoffer_score:
            bestoffer.offer = offer
            bestoffer.url = link
            bestoffer.price = (int)(price)
        
    return bestoffer