import lib.bot_helper.resources.spreadsheet as spreadsheet
from typing import List, Tuple

# Log Page Information
log_info = {
    'page': 'PRLog',
    'first_column': 'B',
    'last_column': 'E',
    'first_row': '3'
}

# PR Page information
pr_info = {
    'page': 'CurrentPR',
    'first_row': '2',
    'last_row': '12',
    'country_column': 'A',
    'pr_column': 'B',
    'capitol_column': 'C'
}

# Display Page Information
display_info = {
    'page': 'DisplayPR',
    'first_row': "4",
    'last_row': "10",
    'country_column': 'B',
    'score_column': 'C'
}


class PRTable(spreadsheet.Spreadsheet):
    """
    Modifications to the Sheets Spreadsheet to include WTS Specific functionality
    """

    def __init__(self, *kwargs):
        super().__init__(*kwargs)

    def get_countries(self) -> List[str]:
        """
        Gets the list of scores in alphabetical order by country
        """
        return self.read_column(pr_info['page'], pr_info['country_column'], pr_info['first_row'], pr_info['last_row'])

    def get_scores(self) -> List[str]:
        """
        Gets the list of scores in alphabetical order by country
        """
        return self.read_column(pr_info['page'], pr_info['pr_column'], pr_info['first_row'], pr_info['last_row'])

    def get_capitol(self) -> List[str]:
        """
        Gets the list of capitol in alphabetical order by country
        """
        return self.read_column(pr_info['page'], pr_info['capitol_column'], pr_info['first_row'], pr_info['last_row'])

    def write_display(self) -> None:
        """
        Writes current scores to the display page, with an x in the ones place
        """
        def comparator(x):
            # x: (name, pr, capitol)
            return (int(x[1]), int(x[2]), x[0])

        # Sort the Scores By PR/C/Name
        scores = list(zip(self.get_countries(),
                          self.get_scores(),
                          self.get_capitol()
                          )
                      )
        scores.sort(key=comparator, reverse=True)

        # Get the Top Scores
        top2 = [[scores[0][0], scores[0][1]], [scores[1][0], scores[1][1]]]

        # Get the Bottom Scores
        bottom2 = [[scores[-2][0], scores[-2][1]],
                   [scores[-1][0], scores[-1][1]]]

        self.write_block(
            display_info['page'],
            display_info['country_column'],
            display_info['score_column'],
            display_info['first_row'],
            str(int(display_info['first_row']) + 1),
            top2
        )
        self.write_block(
            display_info['page'],
            display_info['country_column'],
            display_info['score_column'],
            display_info['last_row'],
            str(int(display_info['last_row']) + 1),
            bottom2
        )

    def write_entry(self, country, score, author, time) -> str:
        """
        Writes the associated row in the PR table for a PR change
        """
        next_row = str(self.find_empty_cell_in_column(
            log_info['page'],
            log_info['first_column'],
            log_info['first_row']
        ))

        time = self._convert_time(time)
        data = [time, country, score, author]

        self.write_row(
            log_info['page'],
            log_info['first_column'],
            log_info['last_column'],
            next_row,
            data
        )
        return '{0} gets {1} PR from {2}\n'.format(country, score, author)

    @staticmethod
    def _convert_time(time: str) -> str:
        """
        Converts the time from UTC to EST
        """

        time = time[11:-10]
        hours_str = time[:2]
        minutes = time[2:]
        hours = int(hours_str)
        hours -= 5
        if hours > 12:
            hours -= 12
        if hours <= 0:
            hours += 12
        hours_str = str(hours)
        return hours_str + minutes
