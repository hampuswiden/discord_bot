# discord_bot.py
import os
import random

from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.group(help='Killgissar saker, t.ex. tal, namn, etc...')
async def killgissa(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send('Vad vill du killgissa? Vänlig ange typ, använd !help killgissa om du är osäker.')

@killgissa.command(help='Killgissar ett tal mellan low och high')
async def tal(ctx, low: int = 1, high: int = 1000):
	if low > high:
		msg = f'Undre gränsen ({low}) måste vara lägre än den övre gränsen ({high})'
	else:
		number = random.randint(low, high)
		msg = 'Killgissning: ' + str(number)
	await ctx.send(msg)

@killgissa.command(help='Killgissar ett namn [från kön]')
async def namn(ctx, gender: str = None):
	if gender in ['man', 'kille', 'pojke']:
		gender = 'male'
	elif gender in ['kvinna', 'tjej', 'flicka']:
		gender = 'female'

	if gender == None:
		gender = random.choice(['male','female'])

	dir_path = os.path.dirname(os.path.realpath(__file__))
	file_path = dir_path + '\\data\\' + gender + '_names.txt'

	with open(file_path) as f:
		names = [name.rstrip('\n') for name in f]

	random_name = random.choice(names)
	await ctx.send('Killgissning: ' + random_name)

@bot.command(name='pearl', help='Används när det är dags att pärla')
async def pearl(ctx):
	msg = 'Dags att pärla? Fram med pärljuicen och lyssna på: \
	https://www.youtube.com/watch?v=xa_PDVNKPvo'
	await ctx.send(msg)

@bot.command(name='pearl2019', help='Ger ett nytt perspektiv på pärlan')
async def pearl2019(ctx):
	msg = 'Trött på klassikern? Pärla med bangers från 2019 istället! \
	https://www.youtube.com/watch?v=1i118j7zHTQ'
	await ctx.send(msg)

@bot.command(name='coinflip', help='Utför en coinflip')
async def coinflip(ctx):
	coin = random.choice(['Krona', 'Klave'])
	msg = 'Vinnare: ' + coin
	await ctx.send(msg)

@bot.command(name='logout', help='Logging out the bot, dev stuff')
@commands.has_role('Admin')
async def logout(ctx):
	print("Logging off now!")
	await bot.close()

bot.run(token)