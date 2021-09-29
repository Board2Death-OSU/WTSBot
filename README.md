# WTSBot

This is a bot designed to manage the PR and Capital Distribution in Watch The Skies.

## How to Use

### Install Dependencies

This project uses [Pipenv](https://pipenv.pypa.io/en/latest/) to manage it's python dependencies. To install, make sure you install pipenv with the following command.

```bash
python -m pip install pipenv
```

and then to set up your pipenv environment and enter it, run

```bash
pipenv install

pipenv shell
```

### Setup Google Sheets API

First, you will need to set up the spreadsheet that is designed for this project in google sheets. A template can be found in templates/spreadsheet.xlsx.

Then, get the spreadsheet ID which can be found after the /d/ in the URL for your sheet. An example id from the url <https://docs.google.com/spreadsheets/d/abc1234567/edit#gid=0> would be abc1234567.

Lastly, you will need to setup an application through the Google sheets api, and get the necessary credentials file, which a tutorial to do this can be found [here](https://developers.google.com/sheets/api/guides/authorizing).

### Set up Discord API

You will need to create a Discord Application the their developer portal. This can be done at the link found [here](https://discord.com/developers/applications). You will then need to get the private token from that bot.

To add the bot to a given discord server, navigate to the OAuth2 section of your bot you made above, and use the OAuth2 URL Generator to generate a URL with the "bot" scope. You will need to have admin permissions in the server to do this.

## Necessary Data to Run

### Secret Data

The necessary secrets should be placed in a file "data/secrets.json", with the following format

```json
{
    "discord_token": "SAMPLE TOKEN",
    "sheet_id": "SAMPLE SHEET ID"
}
```

### Scoring Data

There is a small amount of additional data needed to run this application. This data will need to be placed in "data/score_data.json", with the following format

```json
{
 "countries": [
  { "country_name": "Brazil", "country_acroynm": "BR" },
  { "country_name": "China", "country_acroynm": "CH" },
  { "country_name": "Egypt", "country_acroynm": "EG" },
  { "country_name": "France", "country_acroynm": "FR" },
  { "country_name": "Germany", "country_acroynm": "GE" },
  { "country_name": "India", "country_acroynm": "IN" },
  { "country_name": "Japan", "country_acroynm": "JA" },
  { "country_name": "Russia", "country_acroynm": "RU" },
  { "country_name": "South Africa", "country_acroynm": "SA" },
  { "country_name": "United Kingdom", "country_acroynm": "UK" },
  { "country_name": "United States", "country_acroynm": "US" }
 ]
}
```

## Questions?

Any questions can be posted into this github repo, or to the original author [jklypchak13](https://github.com/jklypchak13).
