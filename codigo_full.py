import telebot as tb
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

chave = "6332233970:AAHDxrOHak-Uss-f19_u7-GXypqrJfYq81E"
bot = tb.TeleBot(chave)

def link():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Link do Mines 💣", url="https://jonbet.cxclick.com/visit/?bta=36278&brand=jonbet"), 
        InlineKeyboardButton("Link do Robo 🤖", url="https://t.me/robominespremium1")
    )
    return markup

def link_18():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Link da Putaria 🔞", url="https://t.me/BrasileirasTaradas"), 
        )
    return markup

'''@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "pnnormal":
        bot.send_message(call.id, text = "<a href='https://t.me/BrasileirasTaradas'>telegeam</a>", parse_mode = ParseMode.HTML)
    elif call.data == "pnmacho":
        bot.answer_callback_query(call.id, "https://t.me/+TwFLuYKvt8xiMzcx")'''

@bot.message_handler(commands=["video"])
def video_premiado(mensagem):
    with open('video_premiado.mp4', 'rb') as foto_premiada:
        bot.send_video(mensagem.chat.id, foto_premiada, caption='Grupo com varias Gostosas esperando por ti!', reply_markup=link_18()) # send a video with buttons

@bot.message_handler(commands=["start"])
def responder(mensagem):
    with open('foto_premiada.jpg', 'rb') as foto_premiada:
        bot.send_photo(mensagem.chat.id, foto_premiada, caption='Robo do Mines Pagando muito!', reply_markup=link()) # send a photo with buttons
        bot.send_message(mensagem.chat.id, "também temos o comando /video (Conteudo 🔞)")

bot.polling()
