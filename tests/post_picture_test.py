import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class NewPostTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.imgur.com")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_picture_from_url(self):
        driver = self.driver

        # the following xpaths and elements should be stored in a page object model
        new_post_path = "//span[text()='New post']"
        url_input_id = "paste-url-input"
        image_url = 'https://www.decibio.com/wp-content/uploads/2017/06/tempus-logo.png'

        new_post_button = driver.find_element_by_xpath(new_post_path)
        new_post_button.click()
        driver.find_element_by_id(url_input_id).send_keys(image_url)

        self.verify_image_upload()


    def test_upload_picture(self):
        driver = self.driver

        new_post_path = "//span[text()='New post']"
        driver.find_element_by_xpath(new_post_path).click()

        input_field_path = '//input[@type="file"]'
        # couldn't make it work with relative path
        image_path = '/Users/olenapoltoratska/qa_code_challenge/tempus-logo.png'
        driver.find_element_by_xpath(input_field_path).send_keys(image_path)

        self.verify_image_upload()

    def verify_image_upload(self):
        driver = self.driver

        image_path = '//div[@class="image post-image"]//img'
        upload_complete_popup_path = '//*[text()="Upload complete ✔"]'
        # making sure file is fully uploaded before asserting
        self.wait.until(EC.visibility_of_element_located((By.XPATH, upload_complete_popup_path)))

        self.assertTrue(driver.find_element_by_xpath(image_path).is_displayed())

if __name__ == '__main__':
    unittest.main()



