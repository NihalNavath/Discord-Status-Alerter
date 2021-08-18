#Settings
token = "" #your bot token here
prefixes = ["!"] #prefix here

#Data
ids = [] #List of bots that is to be monitored 
channelsIds = [] #your channel id(s) here, will accept multiple channels
online_alert = False #whether to send a info message if bot is found to be up

alert_mes_cont = "Bot is down!" #Message that gets sent along with the embed if a bot is found to be down (add a ping if you want here)
up_mes_cont = "" #Message that gets sent along with the embed if a bot is found to be up
embed_color = None #Overides all embed colors