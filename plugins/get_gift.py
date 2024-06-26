import os
from ..config import *
try:
    from telethon.sessions import StringSession
    import asyncio, re, json
    from kvsqlite.sync import Client as uu
    from telethon.tl.types import KeyboardButtonUrl
    from telethon.tl.types import KeyboardButton
    from telethon import TelegramClient, events, functions, types, Button
    import time, datetime
    from datetime import timedelta
    from telethon.errors import (
        ApiIdInvalidError,
        PhoneNumberInvalidError,
        PhoneCodeInvalidError,
        PhoneCodeExpiredError,
        SessionPasswordNeededError,
        PasswordHashInvalidError
    )
    from plugins.messages import *
except:
    os.system("pip install telethon kvsqlite")
    try:
        from telethon.sessions import StringSession
        import asyncio, re, json
        from kvsqlite.sync import Client as uu
        from telethon.tl.types import KeyboardButtonUrl
        from telethon.tl.types import KeyboardButton
        from telethon import TelegramClient, events, functions, types, Button
        import time, datetime
        from datetime import timedelta
        from telethon.errors import (
            ApiIdInvalidError,
            PhoneNumberInvalidError,
            PhoneCodeInvalidError,
            PhoneCodeExpiredError,
            SessionPasswordNeededError,
            PasswordHashInvalidError
        )
        from plugins import *
    except Exception as errors:
        print('An Erorr with: ' + str(errors))
        exit(0)
        


async def get_gift(session):
    async with TelegramClient(StringSession(session), API_ID, API_HASH) as X:
        async for x in X.iter_messages(777000, limit=5):
            try:
                if x.action.slug:
                    return x.action.slug
            except:
                return False

async def join_channel(session, channel):
    async with TelegramClient(StringSession(session), API_ID, API_HASH) as X:
        try:
            result = await X(functions.channels.JoinChannelRequest(
                channel=channel
            ))
            return True
        except:
            return False

async def leave_channel(session, channel):
    async with TelegramClient(StringSession(session), API_ID, API_HASH) as X:
        try:
            result = await X(functions.channels.LeaveChannelRequest(
                channel=channel
            ))
            return True
        except:
            return False

async def leave_all(session):
    async with TelegramClient(StringSession(session), API_ID, API_HASH) as X:
        try:
            async for dialog in X.iter_dialogs():
                if dialog.is_group or dialog.is_channel:
                    await dialog.delete()
            return True
        except:
            return False

async def check(session):
    client = TelegramClient(StringSession(session), API_ID, API_HASH)
    try:
        await client.start()
        await client.get_me()
        return True
    except:
        return False