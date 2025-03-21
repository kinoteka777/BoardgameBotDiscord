from typing import Final
import os
from dotenv import load_dotenv
import discord

# LOAD TOKEN
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# BOT SETUP
bot = discord.Bot()

@bot.slash_command(name="ping", description="Shows the bot\'s latency.")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f"Pong! latency is {bot.latency}")

# STARTUP HANDLING
@bot.event
async def on_ready() -> None:
    print(f'{bot.user} is now running!')

# MAIN ENTRY POINT
def main() -> None:
    bot.run(token=TOKEN)

if __name__ == '__main__':
    main()