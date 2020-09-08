from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

consumer_key = "3rJOl1ODzm9yZy63FACdg"
consumer_secret = "5jPoQ5kQvMJFDYRNE8bQ4rHuds4xJqhvgNJM4awaE8"
access_key = "1102213133123244032-icdOhshoUWDd0pDKB0j1liJ8EW1Tu6"
access_secret = "AuRa4i2ArNBK6miufT4DotkrsQDHdU1bjyVvLmySej0gf"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@client.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.id == 752892157995647006:
        api.update_status(message.content)


bot.run(token)
