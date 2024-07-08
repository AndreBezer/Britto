import telebot as tb
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

chave = "Sua_chave_telegram"
bot = tb.TeleBot(chave)

#Botão com redirecionador para sites
def link():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Link do Mines 💣", url="https://jonbet.cxclick.com/visit/?bta=36278&brand=jonbet"), 
        InlineKeyboardButton("Link do Robo 🤖", url="https://t.me/robominespremium1")
    )
    return markup 

#Botão com redirecionador para canal Telegram
def link_18():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1
    markup.add(
        InlineKeyboardButton("Link do Grupo", url="https://https://t.me/+M1ChcWWFuRVmN2Zh"), 
        )
    return markup

#Comando 'Video' envia um video para o canal
@bot.message_handler(commands=["video"])
def video_premiado(mensagem):
    with open('video_premiado.mp4', 'rb') as foto_premiada:
        bot.send_video(mensagem.chat.id, foto_premiada, caption='Grupo com varias Gostosas esperando por ti!', reply_markup=link_18()) # send a video with buttons

#Comando 'start' envia uma foto para o canal
@bot.message_handler(commands=["start"])
def responder(mensagem):
    with open('foto_premiada.jpg', 'rb') as foto_premiada:
        bot.send_photo(mensagem.chat.id, foto_premiada, caption='Robo do Mines Pagando muito!', reply_markup=link()) # send a photo with buttons
        bot.send_message(mensagem.chat.id, "também temos o comando /video (Conteudo 🔞)")

bot.polling()
