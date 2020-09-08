from discord.ext import commands
import os
import traceback
import tweepy

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']

consumer_key = os.environ['CONSUMER_KEY']
consumer_secret = os.environ['CONSUMER_SECRET']
access_key = os.environ['ACCESS_KEY']
access_secret = os.environ['ACCESS_SECRET']

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if message.channel.id == 752892157995647006:
        api.update_status(message.content)
        await message.channel.send('ツイートしました:「' + message.content + '」')


bot.run(token)
