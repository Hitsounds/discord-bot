import discord
import youtube_dl
from discord.ext import commands
import aiohttp
import os
import asyncio
from ext.database import database
import random
import functools



class voice:
    def __init__(self, client):
        self.client = client

"""    @commands.command()
    async def join(self, ctx):
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(ctx.message.author.voice.channel)
        await ctx.message.author.voice.channel.connect()

    @commands.command()
    async def leave(self, ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self, ctx, url):
        async with ctx.typing():
            player = await YTDLSource.create_source(ctx, url, loop=self.client.loop)
            ctx.voice_client.play(player, after=lambda e: print('Player error: %s' % e) if e else None)
        await ctx.send('Now playing: {}'.format(player.title))


    @play.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")
        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()"""


#---------------------------------------------YOUTUBE---------------------------------------------------------------------------------
    @commands.command()
    async def ytdl(self, ctx, url, Cext="mp3"):
        msg = await ctx.send("Nep is trying her hardest to get your file. https://i.kym-cdn.com/photos/images/original/001/283/141/58e.gif")
        name = random.getrandbits(64)
        if Cext == "mp4":
            Cext = "mp4"
            process = await asyncio.create_subprocess_shell("youtube-dl --no-playlist --default-search \"ytsearch\" -f 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/bestvideo+bestaudio' --merge-output-format mp4 -o {}.mp4 \"{}\"".format(name, url), stdout=asyncio.subprocess.PIPE)
            await process.communicate()
        else:
            Cext = "mp3"
            process = await asyncio.create_subprocess_shell("youtube-dl --no-playlist --default-search \"ytsearch\" --embed-thumbnail --audio-quality 0 --extract-audio --audio-format mp3 -o {}.mp3 \"{}\"".format(name,url), stdout=asyncio.subprocess.PIPE)
            await process.communicate()
        with open(f"{name}.{Cext}", "rb") as f:
            await database.sendFile(self, ctx, f)
        os.remove(f"{name}.{Cext}")
        await msg.delete()




def setup(client):
    discord.opus.load_opus("vendor/lib/libopus.so.0")
    if discord.opus.is_loaded():
        print("Opus loaded!")
    client.add_cog(voice(client))
