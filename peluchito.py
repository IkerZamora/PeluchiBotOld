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
    'ayuda': 'Obtener información acerca de los comandos',
    'hype': 'Tiempo restante para la próxima EE ó AE ó GE'
}
LOG_DIR = "log/"

# Next encounter dates
next_ee_date = datetime.datetime(2017, 7, 21, 16, 0)
next_ae_date = datetime.datetime(2016, 10, 6, 16, 0)
next_ge_date = datetime.datetime(2016, 4, 14, 16, 0)


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
    for key in commands:
        # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page
    note = '''
*NOTA:* La lista de comandos es tan corta porque estoy de vacaciones.
Pero no te preocupes, porque pronto volveré más fuerte que nunca. :)
    '''
    bot.send_message(cid, note, parse_mode="Markdown")


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
        encounter = Encounter(next_ee_date, EE, 25)
    elif param == 'ge':
        encounter = Encounter(next_ge_date, GE, 10)
    elif param == 'ae':
        encounter = Encounter(next_ae_date, AE, 3)
    else:
        bot.send_message(
            cid, "No conozco esa encounter. Uso: /hype ( AE | GE | AE )")
        return
    days, hours, minutes, seconds = encounter.time_left()
    text = "Tiempo restante para la %s%d:\n" % (
        encounter.acronym, encounter.edition)
    text += " %d días, %d horas, %d minutos y %d segundos" % (
        days, hours, minutes, seconds)
    bot.send_message(cid, text)


bot.polling()
