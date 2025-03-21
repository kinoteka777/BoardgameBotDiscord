from typing import Final
import os
import sys
from dotenv import load_dotenv
import discord
import views

# LOAD TOKEN
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

# BOT SETUP
bot = discord.Bot()
games = bot.create_group("games", "Commands related to board games")

@bot.slash_command(description="Shows the bot\'s latency.")
async def ping(ctx: discord.ApplicationContext):
    await ctx.respond(f"Pong! latency is {bot.latency}")

# STARTUP HANDLING
@bot.event
async def on_ready() -> None:
    await bot.sync_commands()
    print(f'{bot.user} is now running!')

# MAIN COMMANDS
@bot.slash_command(name="restart", description="Restarts the bot")
async def restart(ctx):
    await ctx.respond("Restarting...")
    os.execv(sys.executable, ['python']+sys.argv)

# BOARD GAME COMMAND + HELPERS
@games.command()
async def add_game(ctx, date, time, location, game):
    view = views.BoardgameEventView(date, time, location, game)
    embed = views.create_boardgame_embed(date, time, location, game, [])
    await ctx.respond(embed=embed, view=view)


# MAIN ENTRY POINT
def main() -> None:
    bot.run(TOKEN)

if __name__ == '__main__':
    main()