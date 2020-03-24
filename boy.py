from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)
    print(chat_id,url)

def main():
    updater = Updater('983842105:AAFd2AItU3O03cACwFHaps2T5EH0Qj6ytVc')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('dog',bop)) 
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


