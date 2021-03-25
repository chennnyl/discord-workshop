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

@bot.command(name="eval")
async def evaluate_calculation(self, ctx, num1: float, op, num2: float):
    result = 0
    
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    elif op == "^" or op == "**":
        result = num1**num2
        
    await ctx.send("The result is " + str(result) + "!")

bot.run(os.getenv("WORKSHOP_BOT_TOKEN"))




