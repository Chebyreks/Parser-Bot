import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import date, datetime
from parser_bot.schemas.bestoffer import BestOfferRead

def createplot(offerlist: list[BestOfferRead]):
    datelist = [datetime(year=offer.date.year, month=offer.date.month, day=offer.date.day) for offer in offerlist]
    pricelist = [offer.price for offer in offerlist]
    plt.plot(datelist, pricelist, linestyle='--', color="r")
    plt.ylabel("Цена")
    plt.xlabel("Дата")
    plt.gcf().autofmt_xdate()
    format_date = mdates.DateFormatter("%d-%m-%Y")
    plt.gca().xaxis.set_major_formatter(format_date)
    plt.savefig("parser_bot/utils/plot.png")