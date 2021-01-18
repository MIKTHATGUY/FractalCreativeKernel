#this file is in the description !
import urllib.request
import urllib.parse
import re

import youtube_dl
import asyncio
import discord

ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class Youtube():
    async def FindVideo(Video):
        query_string = urllib.parse.urlencode({"search_query" : Video})
        html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
        search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
        Link = "http://www.youtube.com/watch?v=" + search_results[0]
        return Link
    
    async def ExtractAudio(URL):
        loop = asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(URL, download=False))

        fl = data['url']
        title = data['title']

        ms = discord.FFmpegPCMAudio(fl, **ffmpeg_options)
        return ms, title