import time
from datetime import datetime
from pyrogram import Client
import asyncio
import logging
import os


# file_path = r'C:\projects\telegramsender\database.txt'
# print(os.path.exists(file_path))
logging.basicConfig(
    filename="log.log",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)
api_id = '27982348'
api_hash = 'b8046e9be94c4b6c90829dbb0dae1af7'

GREEDY_group_name = -1001725160790
WS_group_name = -1001995593406
WorkUslugi_group_name =  'WorkUslugi'
ChatUslyg_group_name = 'ChatUslyg'
up_days_group_name = 'up_days'
workers_666_group_name = 'workers_666'
blant_uslugi_group_name = 'blant_uslugi'
Visage_Cash_group_name = 'Visage_Cash'
otc_service_ban_group_name = 'otc_service_ban'
ExtasyService_group_name = 'ExtasyService'
u_holding_group_name = 'u_holding'
arbitrage_chat_uslug_group_name = 'arbitrage_chat_uslug'
MAPKET_BOPKEPOB_group_name = 'MAPKET_BOPKEPOB'
detective_group_name = 'mO5lFVf_sEY2Mjlk'
SULTRIXdrop_group_name = 'SULTRIXdrop'
joker_uslugi_group_name = 'joker_uslugi'
XranChat_group_name = 'XranChat'
RisingStarOTC_group_name = 'RisingStarOTC'

#utilits
LOG_group_name = 'logging1055p'
test_group_name = -1002419466058
test2_group_name = 'sadasdasdadsd'

app = Client("my_account", api_id=api_id, api_hash=api_hash)



WS_msge = f'''__Продаю__
**• Мануал на бесконечные баллы X5 клуба - 10$
• Мануал по рефанду Ebay - 10$
• Мануал по рефанду StockX - 10$
• Мануал по рефанду Grailed - 10$
• Мануал по речарджу PayPal - 10$
• Мануал по рефанду Farfetch - 10$
• Беск. пополнение Steam через playerok - 15$
• Мануал по рефаунду FunPay услуг - 10$
• Мануал по рефаунду Яндекс Маркета - 10$
• Мануал по рефаунду AliExpress- 10$**

__Также в продаже:__

**• Мануал по рефу Яндекс еды - 10$
• Мануал как забанить любой аккаунт в телеграме - 10$
• Мануал Австралии 1.0 - 10$
• Мануал Tutti 1.0 - 10$
• Мануал Vinted 1.0 - 10$
• Написанный лично мной скрипт для рассылки в ТГ чаты(__помогаю с установкой__) - 20$
**
Связь: @seller1055p
Гарант: @GarantWS_bot'''

GREEDY_msge = f'''__Продаю__
**• Мануал на бесконечные баллы X5 клуба - 10$
• Мануал по рефанду Ebay - 10$
• Мануал по рефанду StockX - 10$
• Мануал по рефанду Grailed - 10$
• Мануал по речарджу PayPal - 10$
• Мануал по рефанду Farfetch - 10$
• Беск. пополнение Steam через playerok - 15$
• Мануал по рефаунду FunPay услуг - 10$
• Мануал по рефаунду Яндекс Маркета - 10$
• Мануал по рефаунду AliExpress- 10$**

__Также в продаже:__

**• Мануал по рефу Яндекс еды - 10$
• Мануал как забанить любой аккаунт в телеграме - 10$
• Мануал Австралии 1.0 - 10$
• Мануал Tutti 1.0 - 10$
• Мануал Vinted 1.0 - 10$
• Написанный лично мной скрипт для рассылки в ТГ чаты(__помогаю с установкой__) - 20$
**
Связь: @seller1055p
Гарант: @GreedyGARANTbot'''

simple_msge = f'''__Продаю__
**• Мануал на бесконечные баллы X5 клуба - 10$
• Мануал по рефанду Ebay - 10$
• Мануал по рефанду StockX - 10$
• Мануал по рефанду Grailed - 10$
• Мануал по речарджу PayPal - 10$
• Мануал по рефанду Farfetch - 10$
• Беск. пополнение Steam через playerok - 15$
• Мануал по рефаунду FunPay услуг - 10$
• Мануал по рефаунду Яндекс Маркета - 10$
• Мануал по рефаунду AliExpress- 10$**

__Также в продаже:__

**• Мануал по рефу Яндекс еды - 10$
• Мануал как забанить любой аккаунт в телеграме - 10$
• Мануал Австралии 1.0 - 10$
• Мануал Tutti 1.0 - 10$
• Мануал Vinted 1.0 - 10$
• Написанный лично мной скрипт для рассылки в ТГ чаты(__помогаю с установкой__) - 20$
**
Связь: @seller1055p'''


async def main():
    async with app:
        tune = 0
        while True:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            if tune == 1:
                await app.send_message(WS_group_name, WS_msge)
                await app.send_message(LOG_group_name, "Сообщение в WS отправлено | Дата и время: {current_time}")
                await app.send_message(ChatUslyg_group_name, simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в ChatUslyg отправлено | Дата и время: {current_time}")
                await app.send_message(up_days_group_name, simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в up_dayz отправлено | Дата и время: {current_time}")
                await app.send_message(workers_666_group_name, simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в workers_666 отправлено | Дата и время: {current_time}")
                await app.send_message(blant_uslugi_group_name, simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в blant_uslugi отправлено | Дата и время: {current_time}")
                await app.send_message(Visage_Cash_group_name, simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в Visage_Cash отправлено | Дата и время: {current_time}")
                await app.send_message(otc_service_ban_group_name, simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в otc_service_ban отправлено | Дата и время: {current_time}")
                await app.send_message(ExtasyService_group_name, simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в ExtasyService отправлено | Дата и время: {current_time}")
                await app.send_message(arbitrage_chat_uslug_group_name, simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в arbitrage_chat_uslug отправлено | Дата и время: {current_time}")
                await app.send_message(MAPKET_BOPKEPOB_group_name, simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в MAPKET_BOPKEPOB отправлено | Дата и время: {current_time}")
                await app.send_message(detective_group_name, simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в detective отправлено | Дата и время: {current_time}")
                await app.send_message(SULTRIXdrop_group_name, simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в SULTRIXdrop отправлено | Дата и время: {current_time}")
                await app.send_message(joker_uslugi_group_name, simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в joker отправлено | Дата и время: {current_time}")
                await app.send_message(XranChat_group_name, simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в Xran отправлено | Дата и время: {current_time}")
                await app.send_message(RisingStarOTC_group_name, simple_msge)
                await app.send_message(LOG_group_name, f"Сообщение в RisingStarOTC отправлено | Дата и время: {current_time}")
                tune = -1
            tune += 1
            await app.send_message(GREEDY_group_name, GREEDY_msge)
            await app.send_message(LOG_group_name, f"сообщение в GREEDY отправлено | Дата и время: {current_time}")
            await app.send_message(WorkUslugi_group_name, simple_msge)
            await app.send_message(LOG_group_name, f"сообщение в WorkUslugi отправлено | Дата и время: {current_time}")
            await app.send_message(u_holding_group_name, simple_msge)
            await app.send_message(LOG_group_name, f"Сообщение в u_holding отправлено | Дата и время: {current_time}")

            await asyncio.sleep(1802)

asyncio.run(main())

