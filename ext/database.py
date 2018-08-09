import os
import psycopg2
import discord
from discord.ext import commands

class database:
    def __init__(self, client):
        self.client = client
        self.conn = None

    @commands.command(pass_context=True)
    async def scan(self, ctx):
        await self.load()
        self.cur = self.conn.cursor()
        for member in ctx.message.guild.members:
            print(member)
        self.cur.close()
        self.unload.invoke(ctx)

    @commands.group(pass_context=True)
    async def db(self, ctx):
        await self.client.send_message(ctx.message.channel ,"database command recieved")
        if ctx.invoked_subcommand is None:
            await self.client.say("incorrect subcommand")
    

    async def load(self):
        if self.conn is None:
            self.conn = psycopg2.connect(os.environ["DATABASE_URL"], sslmode="require")

    @db.command()
    async def unload(self):
        if self.conn is not None:
            self.conn.close()
            self.conn = None








def setup(client):
    client.add_cog(database(client))