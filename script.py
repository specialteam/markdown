#-*-coding:utf8;-*-
ch = "@special_programming"
import telebot
API_TOKEN = '288894414:AAEIdvaPN-I8DSlcXw7RIosjkGdUw84y0mc'
bot = telebot.TeleBot(API_TOKEN)
import androidhelper
droid = androidhelper.Android()
line = droid.dialogGetInput("please enter your text with markdown")
s = "%s" % (line.result,)
droid.makeToast(s)
bot.send_message(ch, "{}".format(s), parse_mode="Markdown", disable_web_page_preview=True)      
