import unittest
from selenium import webdriver


class SearchTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.imgur.com")

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        driver = self.driver
        search_param = 'tempus'

        search_field_path = '//input'
        search_btn_path = '//img[@class="search"]'

        search_btn = driver.find_element_by_xpath(search_btn_path)
        search_field = driver.find_element_by_xpath(search_field_path)

        search_field.send_keys(search_param)
        search_btn.click()

        self.verify_search_results(search_param)

    def verify_search_results(self, search_param):
        driver = self.driver
        search_result_path = '//*[@class="search-term-text sorting-text-align"]'
        search_result = driver.find_element_by_xpath(search_result_path)
        self.assertEqual(search_result.text, search_param)


if __name__ == '__main__':
    unittest.main()
