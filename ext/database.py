import os
import psycopg2
import discord
from discord.ext import commands
import re
import aiohttp


class database:
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def scan(self, ctx):
        self.conn = await self.load()
        self.cur = self.conn.cursor()
        for member in ctx.message.guild.members:
            self.cur.execute("""UPDATE users SET u_name=E'{name}' WHERE user_id={userID}""".format(userID = member.id, name = re.escape(member.name)))
            self.conn.commit()
        print("Members in {} registered on database".format(ctx.message.guild))
        self.cur.close()
        self.conn.close()
    


    async def load(self):
            return psycopg2.connect(os.environ["DATABASE_URL"], sslmode="require")

    async def sendFile(self, ctx ,filename ,extension):
        with open(f"{filename}.{extension}", "rb") as upload:
            if os.path.getsize(f"{filename}.{extension}")/1048576 < 7:
                return await ctx.send(file=discord.File(upload))
            else:
                async with aiohttp.ClientSession() as session:
                    resp = await session.post('https://transfer.sh/', data={'filedata': upload})
                return await ctx.send(await resp.text())





def setup(client):
    client.add_cog(database(client))
