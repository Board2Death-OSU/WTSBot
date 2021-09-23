import json
import sys
sys.path.append("./")
import lib.bot_helper.bot.client as client
import lib.bot_helper.resources.image_handler as image_handler
import utl.pr_table as pr_table
import utl.prkeeper as prkeeper
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

    if '!CAPITOL' in message:
        response += keeper.display_capitol()
    return response, channel


# Get API Keys
keys = {}
with open('data/secret.json', 'r') as fp:
    keys = json.load(fp)

# Create Bot
client = client.Client()

# Make Spreadsheet
sheet = pr_table.PRTable(
    keys['sheet_id'],
    'data/token.json',
    'data/credentials.json'
)

# Create Score Keeper
keeper = prkeeper.get_inst(sheet)

# Register Score Keeping Callback
client.register_on_message_callback(score_callback, [keeper])

# Start Client
client.run(keys['discord_token'])
