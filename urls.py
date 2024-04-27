from data import country_dict
import os

url_path = "usedURLs.txt"
base_url = "https://www.hatharomhun.com/livescore/"
urls_list = []


class usedURLs:
    def __init__(self, url):
        self.url = url

    def is_url_in_file(self):
        if not os.path.exists(url_path):
            open(url_path, 'w').close()

        else:
            with open(url_path, 'r') as file:
                is_used = any(map(lambda line: self.url in line, file))
                if is_used:
                    return True

        return False


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

        # In the 2018-2019 laliga season the url uses primera_division rather then laliga
        def primera_division_to_laliga():
            primera_division = "https://www.hatharomhun.com/livescore/esp-spain_1-2018-2019-primera_division"
            laliga = "https://www.hatharomhun.com/livescore/esp-spain_1-2018-2019-laliga"
            return list(map(lambda url: primera_division if url == laliga else url, urls_list))

        is_single_country = isinstance(country, str)

        if is_single_country:
            create_url()
        else:
            for country in country:
                create_url()

        laliga_filtered_urls_list = primera_division_to_laliga()

        used_urls_list = list(map(lambda url: usedURLs(url).is_url_in_file(), laliga_filtered_urls_list))
        self.new_urls_list = [url for url, used in zip(laliga_filtered_urls_list, used_urls_list) if not used]

        for item in urls_list:
            print(item)
        print(f"\nTotal URLs: {len(used_urls_list)}")
        print(f"Total used URLs: {sum(used_urls_list)}")
        print(f"Total new URLs: {len(self.new_urls_list)}\n")

    def get_urls_list(self):
        return self.new_urls_list


class CaptureUsedURLs:
    def __init__(self, url):
        self.url = url
        self.append_to_file()

    def append_to_file(self):
        with open(url_path, 'a') as file:
            file.write(self.url + '\n')













