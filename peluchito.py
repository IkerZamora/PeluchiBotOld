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


reload(sys)
sys.setdefaultencoding("utf-8") # This will prevent errors with special characters

commands = { # command description used in the 'ayuda' command, keep this up to date
    'ayuda' : 'Obtener información acerca de los comandos',
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
                    logfile.write("Log file of %s\n___\n" % (m.chat.first_name))
            log = "[%s] %s (%d): %s\n" % (now, m.from_user.first_name, m.from_user.id, m.text)
            with open(logfile_dir, "a") as logfile:
                logfile.write(log)

bot = telebot.TeleBot(TOKEN)
bot.set_update_listener(logger)

# help page
@bot.message_handler(commands=['ayuda'])
def command_help(m):
    cid = m.chat.id
    help_text = "Lista de comandos disponibles: \n"
    for key in commands:  # generate help text out of the commands dictionary defined at the top
        help_text += "/" + key + ": "
        help_text += commands[key] + "\n"
    bot.send_message(cid, help_text)  # send the generated help page
    note = '''
*NOTA:* La lista de comandos es tan corta porque estoy de vacaciones.
Pero no te preocupes, porque pronto volveré más fuerte que nunca. :)
    '''
    bot.send_message(cid, note , parse_mode="Markdown")                

bot.polling()
