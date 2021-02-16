import telebot
import schedule
from time import sleep
from threading import Thread
import json
bot = telebot.TeleBot("1608467125:AAFcK5ojSjzDqb10gT2gRDUr5pQHffU8BGk")
Time_Table={
    '0':{
        '10:05':"Model Checking https://meet.google.com/lookup/f7mserusla?authuser=2&hs=179",
        '11:10':"Compiler Design http://meet.google.com/vrp-tron-smz",
        '2:05':"FOCS https://meet.google.com/lookup/fuu2mt3642?authuser=2&hs=179",
        '3:05':"Optimization https://meet.google.com/lookup/b24uvlqe4j?authuser=2&hs=179",
        '4:15':"IVP https://meet.google.com/lookup/dgbr7vdw3e?authuser=2&hs=179"
    },
    '1': {
        '9:00': "Compiler Design http://meet.google.com/vrp-tron-smz",
        '10:05':"RE https://meet.google.com/lookup/hvnukyh3yj?authuser=2&hs=179",
        '11:10': "IVP https://meet.google.com/lookup/dgbr7vdw3e?authuser=2&hs=179",
        '12:15': "DATA MINING https://meet.google.com/lookup/dihntijjea?authuser=2&hs=179",
        '2:05': "MicroController https://zoom.us/j/94645740622?pwd=THRycXNDbHZZNThsc3RSWVZPUHd2dz09",
        '3:10': "Optimization https://meet.google.com/lookup/b24uvlqe4j?authuser=2&hs=179"
    },
    '2': {
        '9:00': "Compiler Design http://meet.google.com/vrp-tron-smz",
        '11:10': "FOCS https://meet.google.com/lookup/fuu2mt3642?authuser=2&hs=179",
        '12:15': "Model Checking https://meet.google.com/lookup/f7mserusla?authuser=2&hs=179",
        '2:05': "Optimization https://meet.google.com/lookup/b24uvlqe4j?authuser=2&hs=179",
        '3:10': "MicroController https://zoom.us/j/94645740622?pwd=THRycXNDbHZZNThsc3RSWVZPUHd2dz09"
    },
    '3': {
        '10:05': "IVP https://meet.google.com/lookup/dgbr7vdw3e?authuser=2&hs=179",
        '11:10': "DATA MINING https://meet.google.com/lookup/dihntijjea?authuser=2&hs=179",
        '12:15': "RE https://meet.google.com/lookup/hvnukyh3yj?authuser=2&hs=179",
        '2:05': "MicroController https://zoom.us/j/94645740622?pwd=THRycXNDbHZZNThsc3RSWVZPUHd2dz09",
        '3:10': "Compiler Design http://meet.google.com/vrp-tron-smz",
        '4:15':"FOCS https://meet.google.com/lookup/fuu2mt3642?authuser=2&hs=179"
},
    '4': {
        '10:05': "DATA MINING https://meet.google.com/lookup/dihntijjea?authuser=2&hs=179",
        '11:10': "IVP https://meet.google.com/lookup/dgbr7vdw3e?authuser=2&hs=179",
        '12:15': "RE https://meet.google.com/lookup/hvnukyh3yj?authuser=2&hs=179",
        '2:05': "Model Checking https://meet.google.com/lookup/f7mserusla?authuser=2&hs=179",
        '3:10': "Microcontroller LAB https://meet.google.com/lookup/epgqghcnc6?authuser=2&hs=179"
}
}
import time,datetime
timing=str(datetime.datetime.now()).split(" ")[1][:5]
@bot.message_handler(commands=['start'])
def handle_command(message):
    bot.reply_to(message, f"Hii {message.from_user.first_name} \n Welcome to the Bot")
    data_json=json.load(open('id.json'))
    if message.from_user.id in data_json.keys():
        pass
    else:
        data_json[message.from_user.id]="YES"
        writer=json.dumps(data_json)
        with open('id.json',"w") as d:
            d.write(writer)
@bot.message_handler(commands=['now'])
def handle_command(message):
    bot.reply_to(message, f"{datetime.datetime.now()}")
@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    if message.text=="now":
        bot.reply_to(message,"Hiii Abhinav Pajii")
    elif message.text=="today" or message.text=="Today" or message.text=="TODAY":
        day=str(datetime.datetime.today().weekday())
        string=""
        for i in Time_Table[day].keys():
            string=string+i+":"+Time_Table[day][i]+"\n\n"
        if datetime.datetime.today()==5 or datetime.datetime.today()==6:
            bot.reply_to(message,"No class today.......\n\n So chilll!!!!!!")
        else:
            bot.reply_to(message,f"Hello {message.from_user.first_name} {message.from_user.last_name} !\n\n"+string)
    elif message.text=="cd":
        bot.reply_to(message,"http://meet.google.com/vrp-tron-smz")
    elif message.text=="mc":
        bot.reply_to(message,"https://meet.google.com/lookup/f7mserusla?authuser=2&hs=179")
    elif message.text=="ivp":
        bot.reply_to(message,"https://meet.google.com/lookup/dgbr7vdw3e?authuser=2&hs=179")
    elif message.text=="focs":
        bot.reply_to(message,"https://meet.google.com/lookup/fuu2mt3642?authuser=2&hs=179")
    elif message.text=="re":
        bot.reply_to(message,"https://meet.google.com/lookup/hvnukyh3yj?authuser=2&hs=179")
    elif message.text=="dm":
        bot.reply_to(message,"https://meet.google.com/lookup/dihntijjea?authuser=2&hs=179")
    elif message.text=="miot":
        bot.reply_to(message,"https://zoom.us/j/94645740622?pwd=THRycXNDbHZZNThsc3RSWVZPUHd2dz09")
    elif message.text=="miotlab":
        bot.reply_to(message,"https://meet.google.com/lookup/epgqghcnc6?authuser=2&hs=179")
    else:
        bot.reply_to(message,"Sorry Didnt Understand the Command")
def schedule_checker():
    while True:
        schedule.run_pending()
        sleep(1)
def function_to_run():
    djson=json.load(open('id.json'))
    day = str(datetime.datetime.today().weekday())
    string = ""
    if day==5 or day==6:
        string="No class Today Chill!!!!!!!!"
    else:
        for i in Time_Table[day].keys():
            string = string + i + ":" + Time_Table[day][i] + "\n\n"
    for i in djson.keys():
        bot.send_message(i,f"Good Morning {bot.get_chat(i).first_name} {bot.get_chat(i).last_name} \n\n Today you have these classes \n {string}")
def mc():
    djson=json.load(open('id.json'))
    for i in djson.keys():
        bot.send_message(i,f"Hello {bot.get_chat(i).first_name} You have Model Checking Class in 10 mins \n\nLink is https://meet.google.com/lookup/f7mserusla?authuser=2&hs=179")
def cd():
    djson=json.load(open('id.json'))
    for i in djson.keys():
        bot.send_message(i,f"Hello {bot.get_chat(i).first_name} You have Compiler Design Class in 10 mins \n\nLink is http://meet.google.com/vrp-tron-smz")
def focs():
    djson=json.load(open('id.json'))
    for i in djson.keys():
        bot.send_message(i,f"Hello {bot.get_chat(i).first_name} You have FOCS Class in 10 mins \n\nLink is https://meet.google.com/lookup/fuu2mt3642?authuser=2&hs=179")
def oe():
    djson=json.load(open('id.json'))
    for i in djson.keys():
        bot.send_message(i,f"Hello {bot.get_chat(i).first_name} You have OE Class in 10 mins \n\nLink is https://meet.google.com/lookup/b24uvlqe4j?authuser=2&hs=179")
def ivp():
    djson=json.load(open('id.json'))
    for i in djson.keys():
        bot.send_message(i,f"Hello {bot.get_chat(i).first_name} You have IVP Class in 10 mins \n\nLink is https://meet.google.com/lookup/dgbr7vdw3e?authuser=2&hs=179")
def re():
    djson=json.load(open('id.json'))
    for i in djson.keys():
        bot.send_message(i,f"Hello {bot.get_chat(i).first_name} You have RE Class in 10 mins \n\nLink is https://meet.google.com/lookup/hvnukyh3yj?authuser=2&hs=179")
def dm():
    djson=json.load(open('id.json'))
    for i in djson.keys():
        bot.send_message(i,f"Hello {bot.get_chat(i).first_name} You have Data Mining Class in 10 mins \n\nLink is https://meet.google.com/lookup/dihntijjea?authuser=2&hs=179")
def miot():
    djson=json.load(open('id.json'))
    for i in djson.keys():
        bot.send_message(i,f"Hello {bot.get_chat(i).first_name} You have Microcontroller Class in 10 mins \n\nLink is https://zoom.us/j/94645740622?pwd=THRycXNDbHZZNThsc3RSWVZPUHd2dz09")
def miotlab():
    djson=json.load(open('id.json'))
    for i in djson.keys():
        bot.send_message(i,f"Hello {bot.get_chat(i).first_name} You have MIOT LAB Class in 10 mins \n\nLink is https://meet.google.com/lookup/epgqghcnc6?authuser=2&hs=179")
schedule.every().monday.at("02:30").do(function_to_run)
schedule.every().tuesday.at("02:30").do(function_to_run)
schedule.every().wednesday.at("02:30").do(function_to_run)
schedule.every().thursday.at("02:30").do(function_to_run)
schedule.every().friday.at("02:30").do(function_to_run)
# scheduling for monday
schedule.every().monday.at("04:25").do(mc)
schedule.every().monday.at("05:30").do(cd)
schedule.every().monday.at("08:25").do(focs)
schedule.every().monday.at("09:30").do(oe)
schedule.every().monday.at("10:35").do(ivp)
# scheduling for tuesday
schedule.every().tuesday.at("03:20").do(cd)
schedule.every().tuesday.at("04:25").do(re)
schedule.every().tuesday.at("05:30").do(dm)
schedule.every().tuesday.at("06:35").do(ivp)
schedule.every().tuesday.at("08:25").do(miot)
schedule.every().tuesday.at("09:30").do(oe)
# scheduling for wednesday
schedule.every().wednesday.at("03:20").do(cd)
schedule.every().wednesday.at("05:30").do(focs)
schedule.every().wednesday.at("06:35").do(mc)
schedule.every().wednesday.at("08:25").do(oe)
schedule.every().wednesday.at("09:30").do(miot)
# scheduling for thursday
schedule.every().thursday.at("04:25").do(ivp)
schedule.every().thursday.at("05:30").do(dm)
schedule.every().thursday.at("06:35").do(re)
schedule.every().thursday.at("08:25").do(miot)
schedule.every().thursday.at("09:30").do(cd)
schedule.every().thursday.at("10:35").do(focs)
# scheduling for friday
schedule.every().friday.at("04:25").do(dm)
schedule.every().friday.at("05:30").do(ivp)
schedule.every().friday.at("06:35").do(re)
schedule.every().friday.at("08:25").do(mc)
schedule.every().friday.at("09:30").do(miotlab)
Thread(target=schedule_checker).start()
bot.polling()
