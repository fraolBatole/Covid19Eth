import mysql.connector
from mysql.connector import Error
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CommandHandler, CallbackQueryHandler

covidReportPic = 'https://flic.kr/p/2iGz477'
symptomPic = 'https://flic.kr/p/2iFLpA6'
preventionPic = 'https://flic.kr/p/2iFM21g'
stopDoingPic = 'https://flic.kr/p/2iGtChP'

def start(bot, update):
    insertIntoUserReport(update.message.from_user.first_name, update.message.from_user.username, update.message.chat_id)
    update.message.reply_text(main_menu_message(),
                              reply_markup=main_menu_keyboard())

############################ KEYBOARDS #########################################

def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Report', callback_data='m1')],
              [InlineKeyboardButton('Symptoms', callback_data='m2')],
              [InlineKeyboardButton('Prevention', callback_data='m3')],
              [InlineKeyboardButton('Tips', callback_data='m4')],
              [InlineKeyboardButton('Recent News',callback_data='m5')],
              [InlineKeyboardButton('Connect with Expert for advice', callback_data='m6')],
              [InlineKeyboardButton('Click, if you start seeing symptoms', callback_data='m7')]]
  return InlineKeyboardMarkup(keyboard)

def location_keyboard():
    location_keyboard = KeyboardButton(text="send_location", request_location=True)
    contact_keyboard = KeyboardButton(text="send_contact", request_contact=True)
    custom_keyboard = [[ location_keyboard, contact_keyboard ]]
    reply_markup = ReplyKeyboardMarkup(custom_keyboard)

    return reply_markup

############################# CHOICES #########################################
def main_menu_message():
  return 'Choose the option in main menu:'

############################ COMMANDS #########################################

def covidReport(bot, update):
    query = update.callback_query
    bot.send_photo(chat_id=query.message.chat_id, photo=covidReportPic)
    query.message.reply_text(main_menu_message(),
                              reply_markup=main_menu_keyboard())

def symptom(bot, update):
    query = update.callback_query
    bot.send_photo(chat_id=query.message.chat_id, photo=symptomPic)
    query.message.reply_text(main_menu_message(),
                              reply_markup=main_menu_keyboard())

def prevention(bot, update):
    query = update.callback_query
    bot.send_photo(chat_id=query.message.chat_id, photo=preventionPic)
    query.message.reply_text(main_menu_message(),
                              reply_markup=main_menu_keyboard())

def stopDoing(bot, update):
    query = update.callback_query
    bot.send_photo(chat_id=query.message.chat_id, photo=stopDoingPic)
    query.message.reply_text(main_menu_message(),
                              reply_markup=main_menu_keyboard())

def news(bot, update):
    query = update.callback_query
    bot.send_photo(chat_id='329655900', photo=stopDoingPic)

def affectedPeople(bot, update):
    query = update.callback_query
    location_keyboard = telegram.KeyboardButton(text="send_location", request_location=True)
    contact_keyboard = telegram.KeyboardButton(text="send_contact", request_contact=True)
    custom_keyboard = [[ location_keyboard, contact_keyboard ]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    query.message.reply_text("Would you mind sharing your location and contact with me?", 
                                reply_markup=location_keyboard)

def connectExpert(bot, update):
    query = update.callback_query

def positiveSymptoms(username):
    try:
        dbConn = mysql.connector.connect(
            host="", 
            user = "",
            passwd = "",
            database = "")
        
        cursor = dbConn.cursor()

        cursor.execute(" UPDATE bot_users SET symptom = %s WHERE username = '%s' " % (True, username))
        dbConn.commit()
        print("success")

    except mysql.connector.Error as error:
        print("failed {}".format(error))

    finally:
        if(dbConn.is_connected()):
            cursor.close()
            dbConn.close()
            print("Connection closed")

def insertIntoUserReport(first_name,username,chat_id):
    try:
        dbConn = mysql.connector.connect(
            host="", 
            user = "",
            passwd = "",
            database = "")
        
        cursor = dbConn.cursor()

        sqlQuery = "INSERT INTO bot_users (first_name,username,chat_id) VALUES (%s,%s,%s)"

        recordTuple = (first_name,username,chat_id)
        cursor.execute(sqlQuery, recordTuple)
        dbConn.commit()
        print("success")

    except mysql.connector.Error as error:
        print("failed {}".format(error))

    finally:
        if(dbConn.is_connected()):
            cursor.close()
            dbConn.close()
            print("Connection closed")
