import json
from typing import List, Tuple
import re
import utl.pr_table as pr_table


class PRKeeper:

    def __init__(self, data_file: str, spreadsheet):

        # Open Data for Country Information
        data_in = open(data_file, 'r')
        data: dict = json.loads(data_in.read())
        data_in.close()

        self.country_names: List[str] = data['country_names']
        self.countries: List[str] = data['countries']
        self.spreadsheet = spreadsheet
        self.scores = {}
        # Generate Country Regex
        reg_ex_str = '('
        for country in self.countries:
            reg_ex_str += country + '|'
        reg_ex_str += 'ALL)'

        # Save Regex's
        self.country_regex = re.compile(reg_ex_str)
        self.score_regex = re.compile('\+?-?\d+')
        self.read_scores()

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

        def calc_score(new_score):
            return min(max(new_score, 0), 10)

        # Loop over Countries marked, and make the changes
        response = ''
        if score_change is not None and len(countries) > 0:
            for country in countries:
                if country == 'ALL':
                    for val in self.scores.keys():
                        self.scores[val] = calc_score(
                            self.scores[val] + int(score_change))
                else:
                    self.scores[country] = calc_score(
                        self.scores[country] + int(score_change))
                response += self.spreadsheet.write_entry(
                    country, score_change, author, time)
        self.spreadsheet.write_display()
        self.write_scores()
        return response

    def read_scores(self) -> None:
        """
        Initializes score dictionary with the current scores in the spreadsheet
        """
        print('Reading scores')
        values = self.spreadsheet.read_column('ScoreTest', 'B', '4', '14')
        for country, value in zip(self.countries, values):
            self.scores[country] = int(value)

    def write_scores(self) -> None:
        """
        Saves current scores to the score table on the spreadsheet
        """
        print('Writing Scores')
        values = []
        for value in self.scores.values():
            values.append(value)
        self.spreadsheet.write_column('ScoreTest', 'B', '4', '14', values)

    def display_scores(self) -> List[Tuple[str, str]]:
        """
        Constructs a display for the scores of each country with there scores
        """
        scores = self.spreadsheet.get_scores()
        response = ''
        for country, score in zip(self.country_names, scores):
            response += '{0}: {1}\n'.format(country, score)
        return response

    def display_capitol(self) -> List[Tuple[str, str]]:
        """
        Constructs a display for the scores of each country with there scores
        """
        scores = self.spreadsheet.get_capitol()
        response = ''
        for country, score in zip(self.country_names, scores):
            response += '{0}: {1}\n'.format(country, score)
        return response


def get_inst(spreadsheet):
    return PRKeeper('data/score_data.json', spreadsheet)
