import telebot
 

Bot_API_TOKEN = "1251418314:AAGaPAc7pcpKWzluP-PYYhGk9LbcSMtbcCM"
bot = telebot.TeleBot(Bot_API_TOKEN)

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

bot.polling()