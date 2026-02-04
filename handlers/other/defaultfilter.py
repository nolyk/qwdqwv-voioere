from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command, CommandObject
from aiogram.types import *
from typing import Any, Dict, Union
from loader import *
from aiogram.filters.chat_member_updated import ChatMemberUpdatedFilter, IS_NOT_MEMBER, MEMBER, ADMINISTRATOR
from datetime import datetime
from keyboards.reply.usermainkey import *
from keyboards.inline.userinlinekey import *
from loguru import logger
from utils.misc_func.bot_models import *

from utils.misc_func.messagefunc import *
from typing import *
from keyboards.inline.adminkeyinline import *
from random import randint
from states.other_state import *


@userRouter.message(IsNotWork())
async def IsNotWorkFunc(msg: Message, state: FSM):

    await state.clear()

    async with BotDB() as db:
        settings = await db.getSettings()

    text = f'''
💤 Сейчас не рабочие часы для тех.поддержки
{f'⏳ Рабочие часы: {settings["time_work"]} по МСК' if settings["time_work"] != None else ''}
'''

    await msg.answer(text)


@userRouter.message(NotSuccessContentType())
async def NotSuccessContentTypeFunc(msg: Message, state: FSM):
    await state.clear()

    text = f'''
🔴 Данный контент запрещен для отправки
'''
    await msg.answer(text)


@userRouter.message(IsTechWork())
async def IsTechWorkFunc(msg: Message, state: FSM):

    await state.clear()

    text = f'''
🔧 Ведутся технические работы
'''

    await msg.answer(text)







