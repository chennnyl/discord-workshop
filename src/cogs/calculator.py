import discord.ext.commands as commands

class CalculatorCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="eval")
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