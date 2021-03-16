import os
import dotenv

import discord.ext.commands as commands
from cogs.calculator import CalculatorCog


dotenv.load_dotenv()

bot = commands.Bot(command_prefix="calc!")
bot.add_cog(CalculatorCog(bot))

@bot.event
async def on_ready():
    print("Connected to Discord!")

bot.run(os.getenv("WORKSHOP_BOT_TOKEN"))




