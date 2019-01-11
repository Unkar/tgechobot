# -*- Coding: utf-8 -*-
import config
import telebot

#telebot.apihelper.proxy = {'http':'http://192.168.1.198:51229'}

bot = telebot.TeleBot(config.token)

@bot.message_handler(content_types=["text"])
def repeat_all_message(message):
    bot.send_message(message.chat.id, message.text)

if __name__ == "__main__":
    bot.polling(none_stop = True)