import telebot, random
from telebot import types
from time import sleep

bot = telebot.TeleBot('1922118154:AAGTrDR4jtfP7rEhszhQ4BsQWVNKpDj0Hpg', parse_mode='MarkdownV2')
print("Bot started successfully! Running now...")
user = bot.get_me()

knwn = [] #Save UserIDs in a list
with open('userids.txt', 'r') as uids:
    knwn = uids.read()
knwn = knwn.split()

#Listener message, will print user's text in terminal:
def newmsg(messages):
    for m in messages:
        if m.content_type == 'text':
            print(str(m.chat.first_name) + " sent this message: " + m.text)
        elif m.content_type in ['audio', 'video', 'document', 'sticker', 'location', 'voice', 'photo']:
            print(str(m.chat.first_name) + " sent a misc file")

bot.set_update_listener(newmsg) #To turn on listener

@bot.message_handler(commands=['start'])
def wlcm_msg(message):
    cid = (message.chat.id)
    ccid = str(cid)
    if ccid not in knwn:
        knwn.append(ccid)
        bot.send_message(cid, "Ciao " + message.from_user.first_name + "\! I'mma *bot* made by @advik\_143\! \nI can perform various tasks, type /help to view all available commands & features")
        with open("userids.txt", 'w') as uids:
            for each_uid in knwn:
                each_mod_uid = each_uid + ' '
                uids.write(each_mod_uid)
        sleep(0.7)
        bot.send_message(cid, "UserID saved\!")
    else:
        bot.send_message(cid, 'Heya ' + message.from_user.first_name + ', Welcome again\!')

@bot.message_handler(commands=['anime', 'animes'])
def animes_list(message):
    bot.reply_to(message, "List of good animes to watch:\nBlack clover, fire force, one piece, the duke of death and his maid, girlfriend girlfriend , JoJo \(if you haven't watched it\) , mob psycho 100 , one punch man , the rising of the shield hero , konosuba , that time i got reincarnated as a slime , slime diaries , grand blue , love chunibyo and other delusions , free\!dive , burning kabaddi , clean freak aoyama kun , haikyuu\nHava Nice day\!")

@bot.message_handler(commands=['help'])
def all_cmds(message):
    bot.send_message(message.from_user.id, """🔰 *Following features:*
Features list is still being updated, lmao get fcked\!""")
    '''mrkp = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    btn1 = types.KeyboardButton('Hi')
    btn2 = types.KeyboardButton('Who tf are you?')
    mrkp.row(btn1, btn2)
    bot.send_message(message.from_user.id, "Click one\!", reply_markup=mrkp)
    hideboard = types.ReplyKeyboardRemove()'''

@bot.message_handler(content_types=['location'])
def doc_msg(message):
    bot.reply_to(message, "I know your location now, I shall come & get you soon\!")


@bot.message_handler(content_types=['text'])
def hi_msg(message):
    cid = message.chat.id
    hallo = message.text.lower()

    if hallo in ('hi', 'hey', 'hello', 'hola', 'halo'):
        himsgs = ["Heyo, Wassup\?", "Halo\!", "Yo man, how's it going\?", "Hey\!"]
        himsg = random.choice(himsgs)
        bot.send_message(cid, himsg)
    elif hallo in ('namaste', 'nmste', 'namste', 'nmaste'):
        bot.send_message(cid, "Namaste 🙏")
    elif hallo in ('ciao'):
        bot.send_message(cid, "Ciao bruh\!")
    else:
        bot.send_message(cid, "I don't get it what you mean:/")

bot.infinity_polling()
