from commands import *
from telegram.ext import Updater, InlineQueryHandler
import requests
import re
# from visualReports import *

def main():
    updater = Updater('YOUR TOKEN')
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CallbackQueryHandler(covidReport, pattern='m1'))
    dp.add_handler(CallbackQueryHandler(symptom, pattern='m2'))
    dp.add_handler(CallbackQueryHandler(prevention, pattern='m3'))
    dp.add_handler(CallbackQueryHandler(stopDoing,pattern='m4'))
    dp.add_handler(CallbackQueryHandler(news, pattern='m5'))
    dp.add_handler(CallbackQueryHandler(connectExpert, pattern='m6'))
    dp.add_handler(CallbackQueryHandler(affectedPeople, pattern='m7'))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()