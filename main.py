import telebot
from dotenv import load_dotenv
from telebot import types

from panda_data_games import took_data, create_data
import parser
import os


def took_env_data(user_data):
    '''Функция для того, что бы вытаскивать значение из файла .env'''
    load_dotenv()
    a = os.getenv(user_data)
    return a


bot = telebot.TeleBot(took_env_data("TOCKEN"))
print("Бот запустился успешно!")


def user_answer(message):
    if message.text.lower() == "да":
        data_about_games = took_data()
        games_names = data_about_games[0]
        link_games = data_about_games[1]
        for i in range(len(games_names)):
            create_inline_buttons(message, games_names[i], link_games[i], i)


def create_inline_buttons(message, game_name, href_game, imgs_index):
    inline_markup = types.InlineKeyboardMarkup()
    bot.send_photo(message.chat.id, open(f'imgs/image{imgs_index}.png', 'rb'))
    inline_markup.add(types.InlineKeyboardButton(text=game_name, url=href_game))
    bot.send_message(message.chat.id, "Выбирай игру", reply_markup=inline_markup)


def exam_password(message):
    if message.text == took_env_data("ADMIN"):
        create_data()
        bot.send_message(message.chat.id, text='Данные обновились, введите /start')


@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.send_message(message.chat.id, f"Добро пожаловать!")
    user_data = bot.send_message(message.chat.id, "Показать игры? (Да)")
    bot.register_next_step_handler(user_data, user_answer)


@bot.message_handler(commands=["refresh"])
def refresh_data(message):
    user_data = bot.send_message(message.chat.id, text="Введите пароль для refresh и записи данных")
    bot.register_next_step_handler(user_data, exam_password)


bot.polling(none_stop=True)
