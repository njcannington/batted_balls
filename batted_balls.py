import pandas as pd

class Batted_Balls:

    data_file = 'uploads/BattedBallData.xlsx'
    batted_balls = None
    column_heading_index = 0 # index for the column_headings in usable_columns()
    column_description_index = 1 # index for the readable column description in usable_columns()

    def __init__(self):
        column_headings = self.columns_headings()
        self.batted_balls = pd.read_excel(self.data_file, usecols=column_headings)

    def columns_headings(self):
        column_headings = []
        for column_heading in self.usable_columns():
            column_headings.append(column_heading[self.column_heading_index])
        return column_headings

    def get_all_batted_balls(self):
        return self.batted_balls

    def get_pitchers(self):
        return self.batted_balls.PITCHER.unique()

    def get_batters(self):
        return self.batted_balls.BATTER.unique()

    def get_by_pitcher(self, pitcher):
        return self.batted_balls.loc[self.batted_balls['PITCHER'] == pitcher]

    def get_by_batter(self, batter):
        return self.batted_balls.loc[self.batted_balls['BATTER'] == batter]

    def get_by_matchup(self, batter, pitcher):
        return self.batted_balls.loc[(self.batted_balls['BATTER'] == batter) & (self.batted_balls['PITCHER'] == pitcher)]

    def sort_by_column(self, column_heading, is_asc = True):
        # alters the dataframe in self.batted_balls
        self.batted_balls.sort_values(column_heading, ascending=is_asc, inplace=True)
        return self.batted_balls.reset_index()

    @staticmethod
    def usable_columns():
        return [['BATTER','Batter'],
           ['PITCHER', 'Pitcher'],
           ['GAME_DATE', 'Game Date'],
           ['LAUNCH_ANGLE', 'Launch Angle'],
           ['EXIT_SPEED', 'Exit Speed'],
           ['EXIT_DIRECTION', 'Exit Direction'],
           ['HIT_DISTANCE', 'Hit Distance'],
           ['HANG_TIME', 'Hang Time'],
           ['HIT_SPIN_RATE', 'Hit Spin Rate'],
           ['PLAY_OUTCOME', 'Play Outcome'],
           ['VIDEO_LINK', 'Video Link']]