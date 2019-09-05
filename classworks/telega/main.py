import  telebot
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(content_types=['text'])
# def hello(message):
#     print(message)
#     bot.send_message(message.chat.id, message.text)
#     print('new message')

@bot.message_handler(commands=['start'])
def key_exmpl(message):
    inline_kb = telebot.types.InlineKeyboardMarkup()

    button_list = []
    for i in  range(21):
        button_list.append(telebot.types.InlineKeyboardButton(text=str(i), callback_data=str(i)))

    inline_kb.add(*button_list)

    bot.send_message(chat_id=message.chat.id, text='keyboard_exampl', reply_markup=inline_kb)



@bot.callback_query_handler(func=lambda call: True)
def call_exampl(message):
    print(message.data)


if __name__ == "__main__":
    print('Bot starter')
    bot.polling()