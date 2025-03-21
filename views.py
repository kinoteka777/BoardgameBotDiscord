import discord

class BoardgameView(discord.ui.View):
    async def button_callback(self, button, interaction):
        await interaction.response.send_message("Clicked!")