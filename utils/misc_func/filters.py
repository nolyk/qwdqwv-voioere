# - *- coding: utf- 8 - *-
from aiogram.filters import BaseFilter
from aiogram.types import Message, CallbackQuery

from data.config import ADMIN
from aiogram import Bot, Dispatcher, F, Router
from utils.bot_database import BotDB
from loguru import logger
from utils.misc_func.bot_models import *
from utils.misc_func.otherfunc import success_content
from typing import *


class NotSuccessContentType(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        return await success_content(message.content_type)

class SuccessContentType(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        status = await success_content(message.content_type)
        return False if status else True



# Проверка на админа
class IsAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        async with BotDB() as db:
            user = await db.getUser(message.from_user.id)

        if not user:
            return True

        if message.from_user.id in ADMIN or user.get('admin', 0) == 1:
            return True
        return False
        

# Проверка на админа
class IsNotAdmin(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        if message.from_user.id in ADMIN:
            return False
        else:
            return True
        

class IsNotWork(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        async with BotDB() as db:
            settings = await db.getSettings()

        if settings['workbot'] == 1:
            return False
        else:
            return True

class IsWork(BaseFilter):
    async def __call__(self, message: Message) -> bool:

        async with BotDB() as db:
            settings = await db.getSettings()
            user = await db.getUser(message.from_user.id)


        if message.from_user.id in ADMIN:
            return True

        if settings.get('workbot', 0) == 1 and settings.get('technical_work', 0) == 0:
            return True
        
        else:
            return False
        



class IsTechWork(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        async with BotDB() as db:
            settings = await db.getSettings()
            user = await db.getUser(message.from_user.id)


        if settings.get('technical_work', 0) == 0 or message.from_user.id in ADMIN or user.get('admin', 0) == 1:
            return False
        return True


class IsChat(BaseFilter):
    async def __call__(self, message: Union[Message, CallbackQuery]) -> bool:

        async with BotDB() as db:
            settings = await db.getSettings()

        try:
            type_ = message.chat.type
            chat_id = message.chat.id
        except:
            type_ = message.message.chat.type
            chat_id = message.message.chat.id

        if str(type_) != 'private' and chat_id == settings['chat_id']:
            return True
        else:
            return False


class IsModer(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        async with BotDB() as db:
            user = await db.getUser(message.from_user.id)


        if not user:
            return True

        if message.from_user.id in ADMIN or user.get('moderator', 0) == 1:
            return True
        return False


class IsPrivate(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        
        if message.chat.type == 'private':
            return True
        else:
            return False
      

class IsBan(BaseFilter):
    async def __call__(self, message: Message) -> bool:
        async with BotDB() as db:
            user = await db.getUser(message.from_user.id)


        if not user:
            return True

        if message.from_user.id in ADMIN or user.get('ban', 0) != 1:
            return True
        return False


    
