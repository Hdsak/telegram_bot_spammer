from telethon import TelegramClient, events, sync
import time
import params


api_id = params.API_ID
api_hash = params.API_HASH
phone_number = params.PHONE_NUMBER
PASS = params.PASS


@events.register(events.NewMessage(chats=('botan.spf'), incoming=True))
async def normal_handler(event):
    await client.forward_messages('CRM', event.message)


@events.register(events.NewMessage(chats=('CRM'), pattern=r'(?i).*\b(привет)\b'))
async def hello(event):
    await client.send_message('CRM', "Привет👋\nЯ заБОТа-БОТ от Botan")




with TelegramClient('new1', api_id, api_hash) as client:
    if not client.is_user_authorized():
        client.start(phone=phone_number, password=PASS)
    client.add_event_handler(normal_handler)
    client.add_event_handler(hello)
    client.run_until_disconnected()



