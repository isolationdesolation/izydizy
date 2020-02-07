from selenium.webdriver.common.by import By
from .base_page import BasePage
import time


class LandosPage(BasePage):
    down_button = (By.XPATH, '//div[@data-elem-id="1555762461131"]')
    pole_email = (By.XPATH, '//div[@class="t-input-block"]//input[@name="email"]')
    pole_name = (By.XPATH,'//div[@class="t-input-block"]//input[@name="firstName"]')
    pole_surname = (By.XPATH, '//div[@class="t-input-block"]//input[@name="lastName"]')
    pole_phone = (By.XPATH, '//div[@class="t-input-block"]//input[@name="phone"]')
    pole_city = (By.XPATH, '//div[@class="t-input-block"]//textarea[@name="city"]')
    pole_story = (By.XPATH, '//div[@class="t-input-block"]//textarea[@name="shortStory"]')
    galka_btn = (By.XPATH, '//div[@data-input-lid="1559296402643"]/div/label[@class="t-checkbox__control"]/div[@class="t-checkbox__indicator"]')
    send_btn = (By.XPATH, '//div/button[@type="submit"]')
    no = (By.XPATH, '//div[@data-input-lid="1559036333864"]/div[@class="t-input-block"]/div[@class="t-input-error"]')

    def jumpdown_button(self):
        time.sleep(7)
        self.driver.find_element(*self.down_button).click()

    def choose_email(self):
        self.driver.find_element(*self.pole_email).send_keys("thekingofroad0@gmail.com")

    def choose_name(self):
        self.driver.find_element(*self.pole_name).send_keys("1111")


    def choose_surname(self):
        self.driver.find_element(*self.pole_surname).send_keys("22")


    def choose_phone(self):
        self.driver.find_element(*self.pole_phone).send_keys("hello")


    def choose_city(self):
        self.driver.find_element(*self.pole_city).send_keys("ff")


    def choose_info(self):
        self.driver.find_element(*self.pole_story).send_keys("test will be done in 2 sec")


    def press_galka(self):
        time.sleep(2)
        self.driver.find_element(*self.galka_btn).click()

    def press_ok(self):
        self.driver.find_element(*self.send_btn).click()


    def see_notification(self):
        self.driver.find_element(*self.no)
