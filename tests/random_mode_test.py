import unittest

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.imgur.com")


    def tearDown(self):
        self.driver.quit()


    def test_random_mode(self):
        driver = self.driver

        dropdown_path = '(//*[@class="Dropdown-title"])[2]//span'
        option_random_path = '//div[text()="Random"]'


        dropdown = driver.find_element_by_xpath(dropdown_path)
        options_random = driver.find_element_by_xpath(option_random_path)

        dropdown.click()
        options_random.click()

        self.assertEqual(dropdown.text, "RANDOM")


if __name__ == '__main__':
    unittest.main()

