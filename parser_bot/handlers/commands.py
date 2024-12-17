from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.fsm.context import FSMContext

from parser_bot.curd.bestoffer import *
from parser_bot.schemas.bestoffer import BestOfferBase, BestOfferRead
from parser_bot.utils.states import *
from parser_bot.curd.bestoffer import get_offer_by_date, create_offer
from parser_bot.core.parsing import parse_offer

from parser_bot.utils.keyboard import main_kb, return_kb, hello_kb, confirm_kb
from parser_bot.utils.createplot import createplot

router = Router(name="commands_router")

@router.message(CommandStart())
async def command_start(message: Message, session: AsyncSession, state: FSMContext):
    await message.answer("Привет, поздоровайся со мной")
    await state.set_state(Main.tomainmenu)


@router.message(Main.tomainmenu)
async def command_to_main_menu(message: Message, session: AsyncSession, state: FSMContext):
    await message.answer("Выбери действие", reply_markup=main_kb)
    await state.set_state(Main.mainmenu)


@router.message(Main.mainmenu)
async def command_main_menu(message: Message, session: AsyncSession, state: FSMContext):
    match message.text:
        case "Посмотреть лучшее предложение за сегодня":
            await message.answer("Перейти в лучшее предложение за сегодня?", reply_markup=confirm_kb)
            await state.set_state(Main.sendoffer)
        case "Посмотреть статистику":
            await message.answer("Перейти в статистику?", reply_markup=confirm_kb)
            await state.set_state(Main.stat)


@router.message(Main.sendoffer)
async def command_get_offer(message: Message, session: AsyncSession, state: FSMContext):
    answer = await get_offer_by_date(date.today(), session)
    if answer == None:
        await message.answer("Нету сохраненной информации, ожидайте...")
        bestoffer: BestOfferBase = await parse_offer("https://funpay.com/lots/221/")
        await create_offer(bestoffer, session)
    else:
        bestoffer = BestOfferRead.model_validate(answer)

    text = f"Это лучшее предложение на {bestoffer.date.strftime("%d/%m/%Y")}\n{bestoffer.offer}\nС ценой в размере: {bestoffer.price}\nСсылка на предложение: {bestoffer.url}"
    await message.answer(text)
    await message.answer("Выбери действие", reply_markup=main_kb)
    await state.set_state(Main.mainmenu)


@router.message(Main.stat)
async def command_get_stat(message: Message, session: AsyncSession, state: FSMContext):
    answer = await get_all_offers(session)
    offers = [BestOfferRead.model_validate(offer) for offer in answer]
    createplot(offers) # Впадлу асинхронной делать
    plot = FSInputFile("parser_bot/utils/plot.png")
    await message.answer_photo(plot)
    await message.answer("Выбери действие", reply_markup=main_kb)
    await state.set_state(Main.mainmenu)


