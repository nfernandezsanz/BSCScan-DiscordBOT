import asyncio
import discord
from discord.ext  import commands
from bscscan      import *
from config       import *


async def update_task(bot, contract):
    counter = 0
    while(True):
        data  = token_info(contract)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name= str(data) + " holders 🚀"))
        await asyncio.sleep(500)


class Price_Tracker(commands.Bot):
    
    def __init__(self, command_prefix, self_bot, contract):
        commands.Bot.__init__(self, command_prefix=command_prefix, self_bot=self_bot, contract=contract)
        self.message1 = "[INFO]: Bot now online"
        self.coin     = str(contract)
    
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
    bot_token  = bot[bot_name][0]
    print("Initializing: " + bot_name + " ...")
    #Create Bot
    bot_list.append(Price_Tracker(command_prefix="~", self_bot=False, contract=bot[bot_name][1]))
    task.append(loop.create_task(bot_list[i].start(bot_token))) 
    i+=1

try:
    loop.run_forever()
finally:
    loop.stop()
