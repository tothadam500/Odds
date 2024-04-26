from data import country_dict

base_url = "https://www.hatharomhun.com/livescore/"
urls_list = []

primera_division = "https://www.hatharomhun.com/livescore/esp-spain_1-2018-2019-primera_division"
laliga = "https://www.hatharomhun.com/livescore/esp-spain_1-2018-2019-laliga"


class Urls:
    def __init__(self, start_of_season, end_of_season, country):
        season_list = []
        for i in range(0, end_of_season - start_of_season):
            current_year = start_of_season + i
            season = str(current_year) + '-' + str(current_year + 1)
            season_list.append(season)

        def create_url():
            iso = country_dict[country]["iso"]
            league = country_dict[country]["league"]

            for _season in season_list:
                url = f"{base_url}{iso}-{country}_1-{_season}-{league}"
                if url not in urls_list:
                    urls_list.append(url)

        is_single_country = isinstance(country, str)

        if is_single_country:
            create_url()
        else:
            for country in country:
                create_url()

        self.filtered_urls_list = list(map(lambda
                                           url: primera_division if url == laliga else url,
                                           urls_list))

        for item in self.filtered_urls_list:
            print(item)
        print(f"Total urls: {len(self.filtered_urls_list)}")

    def get_urls_list(self):
        return self.filtered_urls_list
