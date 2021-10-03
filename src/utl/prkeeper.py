import json
from typing import List, Tuple, Dict
import re
import utl.pr_table as pr_table
from .pr_table import PRTable


class PRKeeper:

    def __init__(self, data_file: str, spreadsheet: PRTable):

        # Open Data for Country Information
        data_in = open(data_file, 'r')
        data: dict = json.loads(data_in.read())
        data_in.close()

        self.country_names: List[str] = _get_country_names(data['countries'])
        self.countries: List[str] = _get_country_acronyms(data['countries'])
        self.spreadsheet: PRTable = spreadsheet

        # Generate Country Regex
        reg_ex_str = '('
        for country in self.countries:
            reg_ex_str += country + '|'
        reg_ex_str += 'ALL)'

        # Save Regex's
        self.country_regex = re.compile(reg_ex_str)
        self.score_regex = re.compile(r'\+?-?\d+')

    def process_score_message(self, message: str, author: str, time: str) -> str:
        """
        Process a message to see if it invokes a PR change, and make the associated change.
        """

        # Check for Countries, and record them
        matches = re.findall(self.country_regex, message)
        countries = [str(match) for match in matches]

        # Check for Score changes
        match = re.search(self.score_regex, message)
        score_change = None
        if(match is not None):
            score_change = match.group()

        # Loop over Countries marked, and make the changes
        response = ''
        if score_change is not None and len(countries) > 0:
            for country in countries:
                response += self.spreadsheet.write_entry(
                    country,
                    score_change,
                    author,
                    time
                )
        self.spreadsheet.write_display()
        return response

    def display_scores(self) -> str:
        """
        Constructs a display for the scores of each country with there scores
        """
        scores = self.spreadsheet.get_scores()
        response = ''
        for country, score in zip(self.country_names, scores):
            response += '{0}: {1}\n'.format(country, score)
        return response

    def display_capitol(self) -> str:
        """
        Constructs a display for the capitol of each country with there capitols
        """
        scores = self.spreadsheet.get_capitol()
        response = ''
        for country, score in zip(self.country_names, scores):
            response += '{0}: {1}\n'.format(country, score)
        return response


def get_inst(spreadsheet):
    return PRKeeper('data/score_data.json', spreadsheet)


def _get_country_names(data: List[Dict]) -> List[str]:
    """get the country names from the score data

    Args:
        data (List[Dict]): the list of countries

    Returns:
        List[str]: the country names
    """
    country_names = []
    for country in data:
        country_names.append(country['country_name'])
    return country_names


def _get_country_acronyms(data: List[Dict]) -> List[str]:
    """get the country acroymns from the score data

    Args:
        data (List[Dict]): the list of countries

    Returns:
        List[str]: the country acronyms
    """
    country_acronyms = []
    for country in data:
        country_acronyms.append(country['country_acronym'])
    return country_acronyms
