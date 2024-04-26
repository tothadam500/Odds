from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


class Webdriver:
    def __init__(self):
        try:
            self.driver_service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=self.driver_service)
        except Exception as e:
            print("Webriver error! ", str(e))

    def get_driver(self):
        return self.driver
