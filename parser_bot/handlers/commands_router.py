from aiogram import Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession
from aiogram.fsm.context import FSMContext

from parser_bot.curd.user import *
from parser_bot.schemas.user import UserBase
from parser_bot.utils.states import *

router = Router(name="commands_router")

@router.message(CommandStart())
async def command_start(message: Message, session: AsyncSession, state: FSMContext):
    await message.answer("HELLO!!!!!")
