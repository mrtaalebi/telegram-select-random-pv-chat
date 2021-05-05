#!/usr/bin/env python

import os
import asyncio
import random

from dotenv import load_dotenv
from telethon import TelegramClient, events


load_dotenv()

api_id = os.getenv('TELEAPP_API_ID', 0)
api_hash = os.getenv('TELEAPP_API_HASH', "")
phone_number = os.getenv('TELEAPP_PHONE_NUMBER', 0)


async def connect():
    client = TelegramClient('telegram-select-random-pv-chat', api_id, api_hash)
    await client.connect()
    while True:
        auth = await client.is_user_authorized()
        if auth:
            break
        await client.send_code_request(phone_number)
        await client.sign_in(phone_number, input("enter code: "))
    return client

async def run():
    client = await connect()

    chats_iter, users = client.iter_dialogs(), []
    count = 0
    async for chat in chats_iter:
        count += 1
        if chat.is_user:
            users.append(chat)
    print(f'From {count} total chats, {len(users)} are PVs and')
    choosen = random.choice(users)
    chat = await client.get_entity(choosen.id)
    print(f'The choosen one is: {chat.first_name} {chat.last_name} - @{chat.username}')


if api_id == 0 or api_hash == "" or phone_number == 0:
    print('api_id, api_hash or phone_number not present')
    exit(1)

asyncio.run(run())

