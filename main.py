import asyncio
import discord
from discord.ext  import commands
from bscscan      import *

async def update_task(bot, coin):
    counter = 0
    while(True):
        data  = get_coin_status(coin)
        emoji = "➡️"

        if(data['Change'] < 0):
            emoji = "⏬"
        elif(data['Change'] > 0):
            emoji = "⏫"

        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name= "$" + str(data['Price']) + " " + emoji + " " + str(data['Change']) + "%"))
        await asyncio.sleep(60)


class Price_Tracker(commands.Bot):
    
    def __init__(self, command_prefix, self_bot, coin_id):
        commands.Bot.__init__(self, command_prefix=command_prefix, self_bot=self_bot, coin_id=coin_id)
        self.message1 = "[INFO]: Bot now online"
        self.message2 = "Bot still online"
        self.coin     = str(coin_id)
    
    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')
        self.loop.create_task(update_task(self, self.coin))


bot_info_list  = read_bots()

loop     = asyncio.get_event_loop()
task     = list()
bot_list = list()
i        = 0

for bot in bot_info_list:
    bot_name   = list(bot.keys())[0]
    bot_token  = bot[bot_name]
    print("Initializing: " + bot_name + " ...")
    #Create Bot
    bot_list.append(Price_Tracker(command_prefix="!", self_bot=False, coin_id=bot_name))
    task.append(loop.create_task(bot_list[i].start(bot_token))) 
    i+=1

try:
    loop.run_forever()
finally:
    loop.stop()
