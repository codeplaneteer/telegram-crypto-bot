import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import curse
import settings

logging.basicConfig(level=logging.INFO)


 #локальный запуск
bot = Bot(token=f"{settings.TG_TOKEN}")

dp = Dispatcher(bot)

HelpButton = KeyboardButton("Помощь🆘")
CurseButton = KeyboardButton("Курс криптовалют‼️")
InfoButton = KeyboardButton("О боте🤨")
AuthorButton = KeyboardButton("Авторы👤")

main_kb = ReplyKeyboardMarkup(resize_keyboard=True)
main_kb.add(HelpButton, CurseButton, InfoButton, AuthorButton)


@dp.message_handler(Command("start"))
async def start(message: types.Message):
    await message.answer("Привет, я бот помощник в мире криптовалюты👋",
                         reply_markup=main_kb)


@dp.message_handler(content_types='text')
async def MainButton(message: types.Message):
    if message.text == "Авторы👤":
        await message.reply("Создатель: @hkkk89", reply_markup=main_kb)

    elif message.text == "Курс криптовалют‼️":

        with open("CoinData.txt", "r") as file:
            curse.get_AllCount()
            src = file.read()
            await message.reply(src, parse_mode="HTML")

    elif message.text == "О боте🤨":
        await message.reply(
            "Это бот помощник, он может найти интересующий вас материал на тему криптовалют",
            reply_markup=main_kb)

    elif message.text == "Помощь🆘":
        await message.reply("Если вы нашли недочет или баг, пишите сюда: @hkkk89",
                            reply_markup=main_kb)

    else:
        await message.reply("Бот не знает такой комманды")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
