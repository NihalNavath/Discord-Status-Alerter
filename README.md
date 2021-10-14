# Discord-Status-Alerter
A bot that notifies/Alerts a server through a message when another bot goes down.

The main use is to let users know when a bot goes offline and becomes unusable.

[Note]: **Bot requires discord.py 2.0 and `presence` and `member` intent to be enabled.**

# Setup configuration 
1. Install dependencies 
Run `pip install -U -r requirements.txt` to install all the dependencies

2. Settings
Edit the values in settings.py to change the bots behavior! An example is given below:
```python
#Settings
token = "Obv_real_.token"  #your bot token here
prefixes = ["up!"]  #prefix here

#Data
ids = [397835629192413184, 666981084936011776]  #List of bots that is to be monitored 
channelsIds = [895512249542795294]  #your channel id(s) here, will accept multiple channels

alert_message = "Bot is down! <@developers>"  #Message that gets sent along with the embed if a bot is found to be down (add a ping if you want here)
up_message = "yay it do be back"  #Message that gets sent along with the embed when the bot is found to be back up
embed_color = None  #Overides all embed colors
```

3. Run bot
Run `python main.py` to run the python file 

and voila you should now see that the bot is up and running 

## Upgrading
To upgrade your version of the bot, run `git pull` (make sure you have git installed)