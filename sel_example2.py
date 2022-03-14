from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

url = "https://ezweb.easycard.com.tw/search/CardSearch.php"
CARD_NUMBER = "0939856005"
BIRTHDAY = "0517"
CHROMEDRIVER = 'chromedriver.exe'


class Card:
    def __init__(self):
        self.driver = webdriver.Chrome(CHROMEDRIVER)
        self.driver.maximize_window()

    def run(self):
        self.go_to_website()
        self.enter_card_number()
        self.enter_birthday()
        self.select_search_range()
        self.wait_for_robot_check()
        self.click_search()


    def go_to_website(self):
        self.driver.get(url)

    def enter_card_number(self):
        card_number_input = self.driver.find_element(By.XPATH, "/html/body/form/div/div[1]/div[2]/div[2]/div/ul/li[1]/input")
        card_number_input.send_keys(CARD_NUMBER)

    def enter_birthday(self):
        birthday_input = self.driver.find_element(By.XPATH, "/html/body/form/div/div[1]/div[2]/div[2]/div/ul/li[2]/input")
        birthday_input.send_keys(BIRTHDAY)

    def select_search_range(self):
        button = self.driver.find_element(By.ID, "date3m")
        button.send_keys(Keys.SPACE)

    def wait_for_robot_check(self):
        input("press enter when done with robot check...")

    def click_search(self):
        self.driver.find_element(By.ID, "btnSearch").click()


if __name__ == "__main__":
    c = Card()
    c.run()
