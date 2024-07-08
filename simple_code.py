import telebot as tb
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

chave = "Sua_chave_telegram"
bot = tb.TeleBot(chave)

def link():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Link do Mines 💣", url="https://jon.ceo/r/2Exaj"), 
    )
    return markup

def link_18():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Link do Robo 🤖", url="https://t.me/robominespremium1")
    )
    return markup

@bot.message_handler(commands=["robo"])
def video_premiado(mensagem):
    with open('foto_premiada.jpg', 'rb') as foto_premiada:
        bot.send_video(mensagem.chat.id, foto_premiada, caption='Grupo com Robô esperando por ti!', reply_markup=link_18()) # send a video with buttons

@bot.message_handler(commands=["start"])
def responder(mensagem):
    with open('foto_premiada.jpg', 'rb') as foto_premiada:
        bot.send_photo(mensagem.chat.id, foto_premiada, caption='Robo do Mines Pagando muito!', reply_markup=link()) # send a photo with buttons
        bot.send_message(mensagem.chat.id, "CORRE! que é por TEMPO LIMITADO!!!")
        bot.send_message(mensagem.chat.id, "Entre no ROBÔ para AUMENTAR AS CHANCES DE GANHAR!!!")
        bot.send_message(mensagem.chat.id, "/robo")

bot.polling()
