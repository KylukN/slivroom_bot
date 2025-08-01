
import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

API_TOKEN = "YOUR_BOT_TOKEN"
CHANNEL_USERNAME = "@SlivRoomCourses"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = InlineKeyboardMarkup(row_width=1)
    button = InlineKeyboardButton(text="✅ Я підписався", callback_data="check_sub")
    keyboard.add(button)
    await message.answer("Привіт! Щоб отримати безкоштовний PDF-гайд, підпишись на наш канал та натисни кнопку нижче.", reply_markup=keyboard)

@dp.callback_query_handler(lambda c: c.data == 'check_sub')
async def check_subscription(callback_query: types.CallbackQuery):
    user_id = callback_query.from_user.id
    try:
        member = await bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ['member', 'creator', 'administrator']:
            await bot.answer_callback_query(callback_query.id)
            await bot.send_message(user_id, "Ось твій PDF-гайд 🎁:
https://your_pdf_link_here.com/guide.pdf")
        else:
            await bot.answer_callback_query(callback_query.id, text="Спершу підпишись на канал!", show_alert=True)
    except:
        await bot.answer_callback_query(callback_query.id, text="Помилка перевірки підписки. Спробуй пізніше.", show_alert=True)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
