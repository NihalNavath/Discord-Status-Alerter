# Discord-Status-Alerter
A bot that notifies/Alerts a server through a message when another bot goes down.

The main use is to let users know when a bot goes offline and becomes unusable.

# Setup configuration 
Edit the values in settings.py to change the bots behavior! An example is given below:
```python
#Settings
token = "Obv_real_.token" #your bot token here
prefixes = ["!"] #prefix here

#Data
ids = [397835629192413184, 658566989077544970] #List of bots that is to be monitored, will accept multiple bots
channelsIds = [877562439049281617] #your channel id(s) here, will accept multiple channels
online_alert = True #whether to send a info message if bot is found to be up

alert_mes_cont = "Bot is down! <@Developers>" #Message that gets sent along with the embed if a bot is found to be down (add a ping using the format <@RoleID> if you want here)
up_mes_cont = "Bot is up and running, no problems detected:" #Message that gets sent along with the embed if a bot is found to be up
embed_color = None #Overides all embed colors
```

## Note
Bot still WIP will more features that will get later with further updates, also will write a better readme later, lazzy hehe.