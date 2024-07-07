import telebot as tb
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

chave = "6332233970:AAHDxrOHak-Uss-f19_u7-GXypqrJfYq81E"
bot = tb.TeleBot(chave)

chat_dono = 6234485725
chat = -1

responder = int(input("""
Digite um numero para escolher um Canal Privado

chat de teste [0]
chat do Ganhe na net [1]
chat das novinhas safadas [2]
chat novinhas boquete [3]
"""))

if responder == 0:
    chat = -1002171709561
elif responder == 1:
    chat = -1002091315401
elif responder == 2:
    chat = -1002090503159
elif responder == 3:
    chat = -1002181922730

# -1002171709561 -> teste
# -1002091315401 -> ganhe na net
# -1002090503159 -> novinhas safadas
# -1002181922730 -> novinhas boquete

#MANAUS777 BOTÃO
def manaus777():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Link da 🐮 Plataforma Manaus777 🐮", url="https://m.manaus777slots.com?manaus=2i11")
    )
    return markup

#PRIMEIRA PLATAFORMA
def link_plataformanova1():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Link da 🌟 Plataforma Nova 🌟", url="https://www.heepg.vip?gfs=pufsvysb"), #Link da plataforma
    )
    return markup

#BOTOES DO MINE
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

@bot.message_handler(commands=["robomine"])
def video_premiado(mensagem):
    with open('imagens/foto_premiada.jpg', 'rb') as foto_premiada:
        bot.send_video(chat, foto_premiada, caption='Grupo com Robô esperando por ti!', reply_markup=link_18()) # send a video with buttons

#MINE TELEGRAM
@bot.message_handler(commands=["mine"])
def responder(mensagem):
    with open('imagens/foto_premiada.jpg', 'rb') as foto_premiada:
        bot.send_photo(chat, foto_premiada, caption='Robo do Mines Pagando muito!', reply_markup=link()) # send a photo with buttons
        bot.send_message(chat, "CORRE! que é por TEMPO LIMITADO!!!")
        bot.send_message(chat, "Entre no ROBÔ para AUMENTAR AS CHANCES DE GANHAR!!!")
        bot.send_message(chat, "Deposite no minimo R$50!")

#HEE PG
@bot.message_handler(commands=["plataformanova1"])
def responder(mensagem):
    with open('imagens/plataformanova1.jpg', 'rb') as foto_premiada: # path da foto
        bot.send_photo(chat, foto_premiada, caption='Plataforma NOVA Pagando muito!', reply_markup=link_plataformanova1()) # send a photo with buttons
        bot.send_message(chat, "CORRE! que é por TEMPO LIMITADO!!!")
        bot.send_message(chat, "Deposite no minimo R$20!")

#MANAUS 777
@bot.message_handler(commands=["manaus777"])
def responder(mensagem):
    with open('imagens/manaus777.jpg', 'rb') as foto_premiada:
        bot.send_photo(chat, foto_premiada, caption='Plataforma Nova PAGANDO MUITO', reply_markup=manaus777())
        bot.send_message(chat, "CORRE! que é por TEMPO LIMITADO!!!")
        bot.send_message(chat, "Deposite no minimo R$50!")

@bot.message_handler(commands=["start"])
def responder(mensagem):
    bot.send_message(chat_dono, "Bot iniciado!")

bot.polling()
