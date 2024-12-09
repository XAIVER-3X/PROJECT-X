import os
import telebot
from telebot import Telebot,types

Admin = {7233221453}
Token = "7996743693:AAF1KVeutgHZwX3961oGfI85ajlXmoP7VYA"

bot = Telebot(Token)
users = set()

import keep_alive
keep_alive.keep_alive()

@bot.message_handler(commands=["start"])
def welcome(message):
    user_id = message.from_user.id
    username = message.from_user.username if message.from_user.username else "No Username"
    user_welcome_message = (f"""
┏━━━━━
┃ USER ID : {user_id}
┃ USER NAME : {username}
┗━━━━━━━━━━━

┏━━━━━
┃ WELCOME TO THE HELP CENTRE
┃ PLEASE TELL ME YOUR PROBLEMS
┗━━━━━━━━━━━""")
    admin_welcome_message = (f"""
┏━━━━━
┃ USER ID : {user_id}
┃ USER NAME : {username}
┗━━━━━━━━━━━

┏━━━━━
┃ YOUR ARE THE ADMIN OF HELP CENTRE
┗━━━━━━━━━━━""")
    if user_id in Admin:
        markup = types.InlineKeyboardMarkup()
        button = types.InlineKeyboardButton("SEND NOTIFICATION", callback_data="notify_users")
        markup.add(button)
        bot.reply_to(message, admin_welcome_message, reply_markup=markup)
    else:
        users.add(user_id)
        bot.reply_to(message,user_welcome_message)

@bot.message_handler(commands=["help"])
def help_message(message):
    usage_list = (f"""
┏━━━━━
┃ 
┃ 
┗━━━━━━━━━━━""")

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "notify_users" and call.from_user.id in admins:
        notification_message = "Admin has sent a notification!"
        for user_id in users:
            bot.send_message(user_id, notification_message)
        bot.answer_callback_query(call.id, "Notification sent to all users.")
    else:
        bot.answer_callback_query(call.id, "You do not have permission to do this.")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_id = message.from_user.id
    if user_id in admins:
        bot.reply_to(message, "Admin: What's your question?")
    else:
        bot.reply_to(message, "User: I'm here to help! What's your question?")

# Run the bot
if __name__ == '__main__':
    bot.polling(none_stop=True)
