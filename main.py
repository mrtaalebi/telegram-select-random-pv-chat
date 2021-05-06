#!/usr/bin/env python

import os
import asyncio
import math
import random
from pprint import pprint as pp

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

    chats, users, accumulative_count = client.iter_dialogs(), [], 0
    async for chat in chats:
        if chat.is_user:
            user = await client.get_entity(chat.id)
            if user.username and user.username.endswith('bot'):
                continue
            messages = client.iter_messages(user, search='+')
            async for message in messages:
                break
            log_count = int(math.log(messages.total))
            accumulative_count += log_count
            users.append((user, messages.total, accumulative_count,))
            print('.', end='', flush=True)

    puser = lambda user: (
        f'{"@" + user.username if user.username is not None else "":<32s} '
        f'{user.first_name} '
        f'{user.last_name if user.last_name is not None else ""}'
    )

    print('\n\nYour top 100 PVs are listed:')
    print('\n'.join([
        f'[{i+1:04d}] [{count:07d}] {puser(user)}'
        for i, (user, count, _) in enumerate(sorted(users, key=lambda x: x[1], reverse=True)[0:100])
    ]))

    print(f'You have {chats.total} total chats, {len(users)} are PVs with {sum([u[1] for u in users])} total messages.')
    next_ = True
    while (next_):
        choosen_num = random.randint(0, accumulative_count)
        for user, _, count in users:
            if choosen_num <= count:
                choosen = user
                break
        print(f'The choosen one is: {puser(choosen)}')
        next_ = input('\nGet another?[Yn] ') not in ['n', 'N']


if api_id == 0 or api_hash == "" or phone_number == 0:
    print('api_id, api_hash or phone_number not present')
    exit(1)

asyncio.run(run())

