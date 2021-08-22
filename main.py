import os
#import discord
from dotenv import load_dotenv
from discord.ext import commands


def load_cogs(client):
    print("Loading cogs, please wait...")
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            try:
                client.load_extension(f'cogs.{filename[:-3]}')
            except Exception as e:
                print(e)
                print(f"We couldn't load {filename[:-3]} cog properly D:")
                return False
    return True


def main():
    load_dotenv()
    bot = commands.Bot(command_prefix="!")
    if load_cogs(bot):
        bot.run(os.getenv("DISCORD_TOKEN"))
    else:
        print("Check errors, bye!")
        exit()


if __name__ == "__main__":
    main()
