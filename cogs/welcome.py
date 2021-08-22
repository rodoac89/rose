import discord
from discord.ext import commands


class Welcome(commands.Cog):
    def __init__(self, c):
        self.client = c

    # Events
    @commands.Cog.listener()
    async def on_ready(self):
        print("Welcome cog is online")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined')
        log_channel = self.client.get_channel(878788309906784273)
        embed = discord.Embed(color=0x00FF00)
        embed.set_author(
            name=f"{member} has joined the server.", icon_url=f"{member.avatar_url}")
        await log_channel.send(content=None, embed=embed)
    # Commands

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')


def setup(client):
    client.add_cog(Welcome(client))
