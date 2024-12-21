from datetime import datetime
from pyrogram import Client
import asyncio
import logging
from config import group_list, fast_list, WS_msge, GREEDY_msge, simple_msge, api_id, api_hash


logging.basicConfig(
    filename="log.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


#utilits
LOG_group_name = 'logging1055p'
test_group_name = -1002419466058
test2_group_name = 'sadasdasdadsd'
#garant_chats
GREEDY_group_name = -1001725160790
WS_group_name = -1001995593406

app = Client("my_account", api_id=api_id, api_hash=api_hash)


async def main():
    async with app:
        tune = 0
        while True:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if tune == 1:
                for item in group_list.keys():
                    await app.send_message(group_list.get(item), simple_msge)
                    await app.send_message(LOG_group_name, f"Сообщение в {group_list.get(item)} отправлено | Дата и время: {current_time}")
                    # await app.send_message(WS_group_name, WS_msge)
                    # await app.send_message(LOG_group_name, f"Сообщение в WS отправлено | Дата и время: {current_time}")
                tune = -1
            tune += 1
            for item_fast in fast_list.keys():
                await app.send_message(fast_list.get(item_fast), simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в {fast_list.get(item_fast)} отправлено | Дата и время: {current_time}")
            await app.send_message(GREEDY_group_name, GREEDY_msge)
            await app.send_message(LOG_group_name, f"Сообщение в GREEDY отправлено | Дата и время: {current_time}")
            await asyncio.sleep(1802)

asyncio.run(main())