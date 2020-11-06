import time
from urllib2 import urlopen
import telepot

def handle(message):
    content_type, chat_type, chat_id = telepot.glance(message)
    #print content_type, chat_type, chat_id
    chat_id = message['chat']['id']
    command = message['text']
    my_ip = urlopen('http://ip.42.pl/raw').read()
    if(command == '/start'):
        bot.sendMessage(chat_id, "Thanks for using brancraftip!")
    if(command == '/start@brancraftipbot'):
        bot.sendMessage(chat_id, "Thanks for using brancraftip!")
    if(command == '/getip'):
        bot.sendMessage(chat_id, my_ip+":45565")

def __main__():
    bot = telepot.Bot('😏')
    #bot.getMe()
    bot.message_loop(handle)
    print "Ready!"

    while 1:
        time.sleep(3)


if __name__ == '__main__':
    main()
