import unittest
from selenium import webdriver
from builtins import classmethod


class ContactSend(unittest.TestCase):

    @classmethod
    def setUp(cls):

        # create new firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to aplication page
        cls.driver.get("http://demoqa.com/")
        cls.driver.title

    def test_contact_send(self):

        element = self.driver.find_element_by_xpath("//li[@id='menu-item-64']/a")
        element.click()
        # self.driver.implicitly_wait(30)
        elements = self.driver.find_elements_by_xpath("//form[@class='wpcf7-form']/p")
        self.assertEqual(5, len(elements))

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main