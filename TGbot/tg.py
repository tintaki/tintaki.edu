import telebot
telegram_token = "5926966360:AAF2CPo15JMAaRWhdeAvPk4s5DGzE2dIYq4"
bot = telebot.TeleBot(telegram_token)
@bot.message_handler(commands=["start"])

def starteengs(message):
    
    # Получение данных с сервера
    bot.send.message(message.chat.id, "Hello, how can I help you?")
    
    
    
    
    
#     if message.text == ("Hi"):
#         bot.send.message(message.from_user.id, "Hello, how can I help you?")
#     elif message.text == "/help":
#         bot.send.message(message.from_user.id, "Write hello")
#     else:
#         bot.send.message(message.from_user.id, "I don't understand you. Write /help.")  
    
# bot.polling(none_stop=True, interval=0)                 