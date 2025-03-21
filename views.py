import discord
import main

class BoardgameEventView(discord.ui.View):
    def __init__(self, date, time, location, game, attendees=[]):
        super().__init__()
        self.date = date
        self.time =  time
        self.location = location
        self.game = game
        self.attendees = attendees
    
    @discord.ui.button(label="I\'m coming!", style=discord.ButtonStyle.green)
    async def rsvp_button(self, button, interaction):
        user = interaction.user
        user_mention = f"<@{user.id}>"

        if user.name in self.attendees:
            await interaction.response.send_message("You have already joined!", ephemeral=True)
            return

        self.attendees.append(user_mention)

        embed = create_boardgame_embed(self.date, self.time, self.location, self.game, self.attendees)
        await interaction.response.edit_message(embed=embed, view=self)
        await interaction.followup.send(f"Thank you for RSVPing!", ephemeral=True)

    @discord.ui.button(label="I\'m leaving!", style=discord.ButtonStyle.danger)
    async def leave_button(self, button, interaction):
        user = interaction.user
        user_mention = f"<@{user.id}>"

        if user_mention not in self.attendees:
            return

        self.attendees.remove(user_mention)
        embed = create_boardgame_embed(self.date, self.time, self.location, self.game, self.attendees)

        await interaction.response.edit_message(embed=embed, view=self)
        await interaction.followup.send(f"Sorry to hear you're not coming!", ephemeral=True)

def create_boardgame_embed(date, time, location, game, attendees):
    # create embed object
    embed = discord.Embed(
        title="Board Game Night",
        description="Join us for another classic board game night!!",
        color=discord.Color.blue()
    )
    
    # append appropriate fields to embed
    embed.add_field(name="📅 Date", value=date, inline=True)
    embed.add_field(name="⏰ Time", value=time, inline=True)
    embed.add_field(name="📍 Location", value=location, inline=False)
    embed.add_field(name="🎮 Games Featured", value=game, inline=False)

    # add attendees, if any
    if attendees:
        embed.add_field(name="👥 Attendees", value=", ".join(attendees), inline=False)
    else:
        embed.add_field(name="👥 Attendees", value="No attendees yet D:", inline=False)

    embed.set_footer(text="Be there or be square!")
    
    return embed