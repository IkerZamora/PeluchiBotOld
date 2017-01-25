#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is PeluchiBot, a Telegram bot for the @EuskalEncounter Telegram group
"""

import telebot
import datetime
import sys
import os.path
from secret import TOKEN
from encounters import Encounter, EE, AE, GE

# This will prevent errors with special characters
reload(sys)
sys.setdefaultencoding("utf-8")

commands = {
    # command description used in the 'ayuda' command, keep these up to date
    'apastar': 'Manda a alguien a pastar',
    'ayuda': 'Obtener información acerca de los comandos',
    'ayylmao': 'ayyy lmao',
    'ban': 'Ban hammer!',
    'drama': 'Drama :O',
    'fichas': 'Fichas, fichas!',
    'hype': 'Tiempo restante para la próxima EE ó AE ó GE',
    'kappa': 'Kappa',
    'lag': 'Lag, lag everywhere',
    'rip': 'RIP',
    'spam': 'Spam',
    'thug': 'Thug life'
}
LOG_DIR = "log/"


# Log every text message we receive
def logger(messages):
    for m in messages:
        if m.content_type == 'text':
            # Log only text type messages
            chat_id = m.chat.id
            now = datetime.datetime.now()
            logfile_dir = LOG_DIR + str(chat_id) + ".log"
            if not os.path.isfile(logfile_dir):
                with open(logfile_dir, "a") as logfile:
                    logfile.write("Log file of %s\n___\n" %
                                  (m.chat.first_name))
            log = "[%s] %s (%d): %s\n" % (
                now, m.from_user.first_name, m.from_user.id, m.text)
            with open(logfile_dir, "a") as logfile:
                logfile.write(log)


bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(logger)


# Help page
@bot.message_handler(commands=['ayuda'])
def command_help(m):
    cid = m.chat.id
    help_text = "Lista de comandos disponibles: \n"
    for key in sorted(commands):
        # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page


# Displays remaining days for the next LAN party
@bot.message_handler(commands=['hype'])
def command_hype(m):
    cid = m.chat.id
    param = ""
    try:
        param = m.text.split()[1].lower()
    except IndexError:
        bot.send_message(
            cid, "Se necesita un atributo. Uso: /hype ( AE | GE | AE )")
        return
    if param == 'ee':
        encounter = Encounter(EE)
    elif param == 'ge':
        encounter = Encounter(GE)
    elif param == 'ae':
        encounter = Encounter(AE)
    else:
        bot.send_message(
            cid, "No conozco esa encounter. Uso: /hype ( AE | GE | AE )")
        return
    days, hours, minutes, seconds = encounter.time_left()
    text = "Tiempo restante para la %s%d " % (
        encounter.acronym, encounter.edition)
    text += "(%d-%d-%d):\n" % (
        encounter.date.year, encounter.date.month, encounter.date.day)
    text += " %d días, %d horas, %d minutos y %d segundos" % (
        days, hours, minutes, seconds)
    bot.send_message(cid, text)


################################################################
#                        STICKERS                              #
################################################################


# Send RIP sticker
@bot.message_handler(commands=['rip'])
def command_rip(m):
    cid = m.chat.id
    with open('stickers/rip.webp', 'rb') as sticker:
        bot.send_sticker(cid, sticker)


# Send lag sticker
@bot.message_handler(commands=['lag'])
def command_lag(m):
    cid = m.chat.id
    with open('stickers/lag.webp', 'rb') as sticker:
        bot.send_sticker(cid, sticker)


# Send fichas sticker
@bot.message_handler(commands=['fichas'])
def command_fichas(m):
    cid = m.chat.id
    with open('stickers/fichas.webp', 'rb') as sticker:
        bot.send_sticker(cid, sticker)


# Send apastar sticker
@bot.message_handler(commands=['apastar'])
def command_apastar(m):
    cid = m.chat.id
    with open('stickers/apastar.webp', 'rb') as sticker:
        bot.send_sticker(cid, sticker)


# Send ayylmao sticker
@bot.message_handler(commands=['ayylmao'])
def command_ayylmao(m):
    cid = m.chat.id
    with open('stickers/ayylmao.webp', 'rb') as sticker:
        bot.send_sticker(cid, sticker)


# Send ban sticker
@bot.message_handler(commands=['ban'])
def command_ban(m):
    cid = m.chat.id
    with open('stickers/ban.webp', 'rb') as sticker:
        bot.send_sticker(cid, sticker)


# Send drama sticker
@bot.message_handler(commands=['drama'])
def command_drama(m):
    cid = m.chat.id
    with open('stickers/drama.webp', 'rb') as sticker:
        bot.send_sticker(cid, sticker)


# Send kappa sticker
@bot.message_handler(commands=['kappa'])
def command_kappa(m):
    cid = m.chat.id
    with open('stickers/kappa.webp', 'rb') as sticker:
        bot.send_sticker(cid, sticker)


# Send spam sticker
@bot.message_handler(commands=['spam'])
def command_spam(m):
    cid = m.chat.id
    with open('stickers/spam.webp', 'rb') as sticker:
        bot.send_sticker(cid, sticker)


# Send thug sticker
@bot.message_handler(commands=['thug'])
def command_thug(m):
    cid = m.chat.id
    with open('stickers/thug.webp', 'rb') as sticker:
        bot.send_sticker(cid, sticker)


bot.polling()
