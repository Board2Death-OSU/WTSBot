import bot_helper.resources.spreadsheet as spreadsheet
from typing import List, Tuple


class PRTable(spreadsheet.Spreadsheet):
    """
    Modifications to the Sheets Spreadsheet to include WTS Specific functionality
    """

    def __init__(self, *kwargs):

        super().__init__(*kwargs)
        self.next_row = self.find_empty_cell_in_column(
            'PRLog', 'C', '3')
        self.bad_guy_index = [
            "RUSSIA",
            "US",
            "FRANCE",
            "INDIA",
            "JAPAN",
            "CHINA",
            "EGYPT",
            "GERMANY",
            "SOUTH AFRICA",
            "BRAZIL",
            "UK",
        ]

    def get_countries(self) -> List[str]:
        """
        Gets the list of scores in alphabetical order by country
        """
        return self.read_column('CurrentPR/C', 'A', '2', '12')

    def get_scores(self) -> List[str]:
        """
        Gets the list of scores in alphabetical order by country
        """
        return self.read_column('CurrentPR/C', 'B', '2', '12')

    def get_capitol(self) -> List[str]:
        """
        Gets the list of capitol in alphabetical order by country
        """
        return self.read_column('CurrentPR/C', 'C', '2', '12')

    def write_display(self) -> None:
        """
        Writes current scores to the display page, with an x in the ones place
        """
        def comparator(x):

            return (x[1], x[2], self.bad_guy_index.index(x[0]))

        # Sort the Scores By PR/C/BGI
        scores = list(zip(self.get_countries(),
                          self.get_scores(), self.get_capitol()))
        scores.sort(key=comparator, reverse=True)

        # Get the Top 2
        top2 = [(scores[0][0], scores[0][1]), (scores[1][0], scores[1][1])]
        # Get the Bottom
        bottom2 = [(scores[-2][0], scores[-2][1]),
                   (scores[-1][0], scores[-1][1])]
        self.write_block('DisplayPR', 'A', 'B', '4', '5', top2)
        self.write_block('DisplayPR', 'A', 'B', '8', '9', bottom2)

    def write_entry(self, country, score, author, time) -> str:
        """
        Writes the associated row in the PR table for a PR change
        """
        self.next_row = self.find_empty_cell_in_column(
            'PRLog', 'C', '3')
        time = self._convert_time(time)
        data = [time, country, score, author]
        self.write_row(
            'PRLog', 'B', 'E', str(self.next_row), data)
        self.next_row += 1
        return '{0} gets {1} PR from {2}\n'.format(country, score, author)

    @staticmethod
    def _convert_time(time: str) -> str:
        """
        Converts the time from UTC to EST
        """

        time = time[11:-10]
        hours = time[:2]
        minutes = time[2:]
        hours = int(hours)
        hours -= 5
        if hours > 12:
            hours -= 12
        if hours <= 0:
            hours += 12
        hours = str(hours)
        return hours + minutes
