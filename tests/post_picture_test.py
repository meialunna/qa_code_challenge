import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class NewPost(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.imgur.com")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_post_new_picture(self):
        driver = self.driver

        new_post_path = "//span[text()='New post']"
        url_input_id = "paste-url-input"
        image_path = "//img[@style]"
        verification_element_path = "//li[@class='extra-option delete']"
        image_url = 'https://s.imgur.com/images/upload-giraffe.png'


        new_post_button = driver.find_element_by_xpath(new_post_path)

        new_post_button.click()
        driver.find_element_by_id(url_input_id).send_keys(image_url)


        self.wait.until(EC.visibility_of_element_located((By.XPATH, image_path)))


        verification_element = driver.find_element_by_xpath(verification_element_path)
        self.assertTrue(verification_element.is_displayed())



if __name__ == '__main__':
    unittest.main()



