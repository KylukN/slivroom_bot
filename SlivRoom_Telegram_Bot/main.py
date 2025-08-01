
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8361460365:AAF-N4_phWzrRsveQ1tZG8-9xh3oJjo5S5E"
CHANNEL_USERNAME = "@SlivRoomCourses"
PDF_PATH = "SlivRoom_FreeCourses_Guide.pdf"

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    chat_id = message.chat.id
    try:
        member = bot.get_chat_member(CHANNEL_USERNAME, user_id)
        if member.status in ['member', 'creator', 'administrator']:
            with open(PDF_PATH, 'rb') as pdf_file:
                bot.send_document(chat_id, pdf_file, caption="Ось твій PDF-гайд 🎁")
        else:
            ask_to_subscribe(chat_id)
    except Exception as e:
        ask_to_subscribe(chat_id)

def ask_to_subscribe(chat_id):
    markup = InlineKeyboardMarkup()
    btn = InlineKeyboardButton("✅ Підписатись", url=f"https://t.me/{CHANNEL_USERNAME[1:]}")
    markup.add(btn)
    bot.send_message(chat_id, "Щоб отримати гайд, підпишись на канал і натисни /start", reply_markup=markup)

bot.polling()
