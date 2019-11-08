import json
import sys
sys.path.append('lib/')

import bot_helper.bot.client as client
import utl.pr_table as pr_table
import utl.prkeeper as prkeeper
import signal
import sys


def score_callback(msg, keeper):
    """
    The Callbaquck to handle message processing for the score keeping functionality.
    """

    # Gather information from the message object
    channel = msg.channel
    message = msg.content.upper()
    time = str(msg.created_at)

    author = str(msg.author.display_name)
    if author is None:
        author = str(msg.author)
    response = ''

    # Check if this is a kill command
    if str(msg.channel) == 'human':
        if '!' not in message:
            response += keeper.process_score_message(
                message, author, time)

    # Check if a score table was requested.
    if '!SCORE' in message:
        response += keeper.display_scores()
    return response, channel


# Get API Keys
secret_input = open('data/secret.json')
keys = json.load(secret_input)
secret_input.close()

# Create Bot
client = client.Client()

# Make Spreadsheet
sheet = pr_table.PRTable(
    keys['sheet_id'], 'data/token.json', 'data/credentials.json')

# Create Score Keeper
keeper = prkeeper.get_inst(sheet)

# Register Score Keeping Callback
client.register_on_message_callback(score_callback, [keeper])

# Start Client
client.run(keys['discord_token'])
