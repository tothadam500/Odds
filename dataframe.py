from database import Database


sub_tables = {
    'date': ['ID', 'Season', 'Quarter'],
    'location': ['ID', 'Country', 'League'],
    'teams': ['ID', 'Home Team', 'Away Team', 'Winner Team'],
    'result': ['ID', 'Home Goals', 'Away Goals', 'Result'],
    'odds': ['ID', 'Home Odds', 'Draw Odds', 'Away Odds', 'Winner Odds', 'Greatest Odds',
             'Is Winner Odds Greatest']
}


class Dataframe:
    def __init__(self, df):
        self.df = df
        self.db = Database()
        for name, col in sub_tables.items():
            sub_df = self.get_sub_df(col)
            self.db.import_to_database(df=sub_df, name=name)

    def get_sub_df(self, columns):
        sub_df = self.df[columns]
        sub_df.columns = [col.lower().replace(' ', '_') for col in sub_df.columns]
        return sub_df

