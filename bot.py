import discord
from discord.ext import commands
#from boto.s3.connection import S3Connection

TOKEN = "NDc2MzgzMzQ4OTY5OTYzNTMx.Dkt04A.domVQsP2bNT9by9m17dQIbC_6wo"  #S3Connection(os.environ['TOKEN'])

client = commands.Bot(command_prefix = ";hs;")

@client.event
async def on_ready():
    print ("Bot is ready")

client.run(TOKEN)
