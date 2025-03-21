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

@games.command()
async def add_game(ctx, date, time, location, game):
    embed = discord.Embed(
        title="Board Game Night 🎲",
        description="Join us for a fun-filled night of board games!",
        color=discord.Color.blue()  # You can change this to any color you'd like
    )

    # Adding fields to the embed
    embed.add_field(name="📅 Date", value=date, inline=False)
    embed.add_field(name="⏰ Time", value=time, inline=False)
    embed.add_field(name="📍 Location", value=location, inline=False)
    embed.add_field(name="🎮 Game:", value=game, inline=False)
    embed.set_footer(text="See you there! 🎉")

    # Send the embed to the same channel where the command was used
    await ctx.respond(embed=embed)

# MAIN ENTRY POINT
def main() -> None:
    bot.run(TOKEN)

if __name__ == '__main__':
    main()