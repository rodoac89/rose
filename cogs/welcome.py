import discord
from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, c):
        self.client = c
        self.allowed_mentions = discord.AllowedMentions(everyone=True)

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Welcome cog is online")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name="welcome")
        await channel.send(f"Hey @everyone! {member} se ha unido a la fiesta :D", allowed_mentions=self.allowed_mentions)


def setup(client):
    client.add_cog(Welcome(client))
