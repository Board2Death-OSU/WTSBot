import json
import sys
sys.path.append('lib/')

import bot_helper.bot.client as client
import bot_helper.resources.image_handler as image_handler
import utl.pr_table as pr_table
import utl.prkeeper as prkeeper
import signal
import sys

fun = True  # Controls whether or not the image handling processes are run


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

# Add Cat Image Handler
cat_images = image_handler.ImageHandler.get_files('data/img/cat')
cat_handler = image_handler.ImageHandler(
    cat_images, "cat", "off-topic")
if fun:
    client.register_on_message_send_file_callback(
        cat_handler.get_call_back(), [])

# Add Dog Image Handler
dog_images = image_handler.ImageHandler.get_files('data/img/dog')
dog_handler = image_handler.ImageHandler(dog_images, "dog", "off-topic")
if fun:
    client.register_on_message_send_file_callback(
        dog_handler.get_call_back(), [])

# Add Penguin Image Handler
penguin_images = image_handler.ImageHandler.get_files('data/img/penguin')
penguin_handler = image_handler.ImageHandler(
    penguin_images, "penguin", "off-topic")
if fun:
    client.register_on_message_send_file_callback(
        penguin_handler.get_call_back(), [])

# Start Client
client.run(keys['discord_token'])
