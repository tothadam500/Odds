from dataframe import Dataframe


class TransformData:
    def __init__(self, df):
        self.df = df
        self.transform()

    def transform(self):
        self.season()
        self.country()
        self.league()
        self.id()
        self.df.drop(columns=["URL"], inplace=True)

        self.home_goals()
        self.away_goals()
        self.result()
        self.winner_team()

        self.quarter()
        self.greatest_odds()
        self.winner_odds()
        self.is_winner_odds_greatest_odds()

        print(self.df.head(10), '\n')
        Dataframe(self.df)

    def season(self):
        self.df["Season"] = self.df["URL"].apply(lambda url: "-".join(url.split('-')[2:4]))

    def country(self):
        self.df["Country"] = self.df["URL"].apply(lambda url: url.split('-')[1].split("_")[0])

    def league(self):
        self.df["League"] = self.df["URL"].apply(lambda url: url.split('-')[-1])

    def id(self):
        self.df["ID"] = self.df.apply(lambda
                                      row: f"{row['URL'].split('/')[-1].split('-')[0]}_{row['Season']}_{row.name}",
                                      axis=1)

    def home_goals(self):
        self.df["Home Goals"] = self.df["Result"].apply(lambda x: int(x.split("-")[0]))

    def away_goals(self):
        self.df["Away Goals"] = self.df["Result"].apply(lambda x: int(x.split("-")[1]))

    def result(self):
        self.df["Result"] = self.df.apply(
            lambda row: "draw" if row["Home Goals"] == row["Away Goals"] else "home" if row["Home Goals"] > row[
                "Away Goals"] else "away", axis=1)

    def winner_team(self):
        self.df["Winner Team"] = self.df.apply(
            lambda row: row["Home Team"] if row["Result"] == 'home'
            else (row["Away Team"] if row["Result"] == 'away'
                  else None),
            axis=1
        )

    def quarter(self):
        total_matches = len(self.df)
        first_quarter = total_matches / 4
        second_quarter = total_matches / 4 * 2
        third_quarter = total_matches / 4 * 3

        def get_quarter(index):
            index = int(index)
            if index <= first_quarter:
                return "1"
            elif first_quarter < index <= second_quarter:
                return "2"
            elif second_quarter < index <= third_quarter:
                return "3"
            else:
                return "4"

        self.df["Quarter"] = self.df.index.to_series().apply(get_quarter)

    def winner_odds(self):
        self.df['Winner Odds'] = self.df.apply(
            lambda row: row['Home Odds'] if row['Result'] == 'home'
            else (row['Draw Odds'] if row['Result'] == 'draw'
                  else row['Away Odds']),
            axis=1)

    def greatest_odds(self):
        self.df['Greatest Odds'] = self.df[['Home Odds', 'Draw Odds', 'Away Odds']].max(axis=1)

    def is_winner_odds_greatest_odds(self):
        self.df['Is Winner Odds Greatest'] = self.df['Winner Odds'] == self.df['Greatest Odds']
