
import discord
from discord.ext import commands
import logging
from gpt_module import generate_gpt_sql_query 
from database_module import query_database

# Logging setup
logging.basicConfig(level=logging.INFO, filename='bot.log', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

# Define intents including the message content intent for reading message content
intents = discord.Intents.default()
intents.message_content = True  # Ensure your bot has the message content intent enabled

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    logging.info(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_message(message):
    # Don't respond to messages from the bot itself
    if message.author == bot.user:
        return
    logging.info(f'Message from {message.author}: {message.content}')
    # Important: Without this line, your commands won't get processed
    await bot.process_commands(message)

@bot.command(name='suggest_meal')
async def suggest_meal(ctx, *, user_input: str):
    logging.info(f'Received suggest_meal command with arguments: {user_input}')
    try:
        # Generate SQL query using GPT module
        generated_sql_query = generate_gpt_sql_query(user_input)
        # Query the database using the generated SQL query
        results = query_database(generated_sql_query)
        
        # Check if results were found and format the response using an embed
        if results:
            embed = discord.Embed(title="Meal Suggestions", description="Here are some meal suggestions based on your preferences:", color=0x00ff00)
            # Add a counter for meal options
            for index, result in enumerate(results, start=1):
                embed.add_field(name=f"Option {index}", value=result[0], inline=False)
            embed.set_footer(text=f"Total suggestions: {len(results)}")
            await ctx.send(embed=embed)
        else:
            await ctx.send("Sorry, I couldn't find any meals matching your criteria.")
        logging.info('Suggest_meal command processed successfully.')
    except Exception as e:
        logging.exception('An error occurred while processing the suggest_meal command.')
        await ctx.send('An error occurred while processing your request.')

DISCORD_TOKEN = 'YOUR_TOKEN'

if __name__ == '__main__':
    bot.run(DISCORD_TOKEN)
