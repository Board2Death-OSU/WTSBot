# WTSBot

This is a bot designed to manage the PR and Capital Distribution in Watch The Skies.

## How to Use

### Install Dependencies

This project uses [Pipenv](https://pipenv.pypa.io/en/latest/) to manage it's python dependencies. To install, make sure you install pipenv with the following command.

```bash
python -m pip install pipenv
```

pipenv is a very powerful depencancy management tool. In order to install the dependencacy's you can run:

```bash
python -m "pipenv" install
```

or if you have your python scripts in your global PATH variable, described [here](https://datatofish.com/add-python-to-windows-path/) you can just run

```bash
pipenv install
```

this will create a virtual environment, that your shell must enter whenever you want to run the bot. to enter the shell, simply run one of the two commands, based off of if you have the python scripts in your PATH.

```bash
python -m "pipenv" shell

pipenv install
```

### Setup Google Sheets API

First, you will need to set up the spreadsheet that is designed for this project in google sheets. A template can be found in templates/spreadsheet.xlsx. Be sure if  you upload the .xlsx file that you re-save it as a Google Sheets file type and use that one.

Then, get the spreadsheet ID which can be found after the /d/ in the URL for your sheet. An example id from the url <https://docs.google.com/spreadsheets/d/abc1234567/edit#gid=0> would be abc1234567.

Lastly, you will need to setup an application through the Google sheets api, and get the necessary credentials file, which a tutorial to do this can be found [here](https://developers.google.com/sheets/api/guides/authorizing).

#### Creating Credentials Files

The above tutorial is useful, but here are the important steps you'll need to follow to get your credentials.

First, navigate [here](https://console.cloud.google.com/apis/dashboard), google cloud's api dashboard. If you do not have a project yet, create one in the steps described above.

Then, click the link for "Enable API's and Services" (or something similar, incase it changed.). This should pull up a search bar. Search for "Google Sheets" and enable it.

This should redirect you to a page, that has a "create credential" link. Follow that, which should pull up a form. Select Google Sheets as the API, and make sure it has access to user data. (This is so it can access your spreadsheet that you specify.) Then hit continue.

The next section is OAuth Consent Screen. This doesn't really matter, and can whatever you want.

Next is scopes. Make sure you allow the "./auth/spreadsheets" scope.

For OAuth Client ID, make it a desktop app and name it anything you wish. Then it should provide you a link to download your credentials. Simply rename it to credentials.json, and move it to the data folder.

#### Error 403: access_denied

If you get an error 403 when trying to authorize the app through google, you most likely need to list yourself as a test user. From the Google Cloud Platform API dashboard, go to the OAuth consent screen section, then under the Test users section, click add users, and provide the email address that owns the sheet you created.

### Set up Discord API

You will need to create a Discord Application the their developer portal. This can be done at the link found [here](https://discord.com/developers/applications). You will then need to get the private token from that bot.

To add the bot to a given discord server, navigate to the OAuth2 section of your bot you made above, and use the OAuth2 URL Generator to generate a URL with the "bot" scope. You will need to have admin permissions in the server to do this.

## Necessary Data to Run

### Secret Data

The necessary secrets should be placed in a file "data/secret.json", with the following format

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
  { "country_name": "Brazil", "country_acronym": "BR" },
  { "country_name": "China", "country_acronym": "CH" },
  { "country_name": "Egypt", "country_acronym": "EG" },
  { "country_name": "France", "country_acronym": "FR" },
  { "country_name": "Germany", "country_acronym": "GE" },
  { "country_name": "India", "country_acronym": "IN" },
  { "country_name": "Japan", "country_acronym": "JA" },
  { "country_name": "Russia", "country_acronym": "RU" },
  { "country_name": "South Africa", "country_acronym": "SA" },
  { "country_name": "United Kingdom", "country_acronym": "UK" },
  { "country_name": "United States", "country_acronym": "US" }
 ]
}
```

## Questions?

Any questions can be posted into this github repo, or to the original author [jklypchak13](https://github.com/jklypchak13).
