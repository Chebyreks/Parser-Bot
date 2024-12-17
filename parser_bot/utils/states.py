from aiogram.fsm.state import StatesGroup, State

class Main(StatesGroup):
    tomainmenu = State()
    mainmenu = State()
    sendoffer = State()
    stat = State()