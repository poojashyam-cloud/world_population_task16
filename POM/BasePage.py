
from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url ="https://www.theworldcounts.com/challenges/planet-earth/state-of-the-planet/world-population-clock-live"
        self.world_pop = (By.XPATH,"//div[@class='counter-ticker is-size-2-mobile']")

    def open(self):
        self.driver.get(self.url)

    def get_population(self):
        return self.driver.find_element(*self.world_pop).text
