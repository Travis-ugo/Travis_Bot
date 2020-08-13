import telebot
import os 
import flask
from flask import request

server = flask.Flask(__name__)

debug = False
token = "1251418314:AAGaPAc7pcpKWzluP-PYYhGk9LbcSMtbcCM"

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    id = message.from_user.id
    bot.send_message(chat_id=id , text= 'Hello, welcome to Travis_Bot')

@bot.message_handler(commands=['help'])
def handle_start_help(message):
    print(message)
    id = message.from_user.id
    bot.send_message(chat_id=id , text= 'How can help you ')

    
@bot.message_handler(commands=['hey'])
def handle_docs_hot(message):
    print(message)
    id = message.from_user.id
    bot.send_message(chat_id=id , text= 'hey there ')

@bot.message_handler(commands=['images'])
def handle_docs_image(message):
    print(message)
    id = message.from_user.id
    bot.send_photo(chat_id=id , photo= 'http://www.imaging-resource.com/PRODS/canon-6d/Z_canon_6D_beauty2.JPG')

@bot.message_handler(commands=['audio'])
def handle_docs_audio(message):
    (message)
    id = message.from_user.id
    bot.send_audio(chat_id=id , audio= 'https://d274.cdn-me.net/tb/e/89/pop_smoke_dior_official_video_mp3_19067.mp3?play')


@bot.message_handler(commands=['video'])
def handle_video(message):
    print(message)
    id = message.from_user.id
    bot.send_video(chat_id=id , data = 'https://res.cloudinary.com/thrinitee/video/upload/v1597241738/meek_mill_dangerous_feat._jeremih_pnb_rock_h264_50611_xogq88.mp4')


@server.route('/' + token, methods=['POST'])
def getMessage():
    request_object = request.stream.read().decode('utf-8')
    update_to_json = [telebot.types.Update.de_json(request_object)]
    bot.process_new_updates(update_to_json)
    return 'whats good'


@server.route('/hook')
def Webhook():
    url = 'https://okonicha-bot.herokuapp.com/'
    bot.remove_webhook()
    bot.set_webhook(url + token)
    return f'webhook set to url {url}'

@server.route('/')
def good():
    return f"hello funny boy"

if debug == True:
    bot.remove_webhook()
    bot.polling()
else:
    if __name__== "_main_":
        server.run(host="0.0.0.0", port=int(os.environ.get('POST', 5000)))