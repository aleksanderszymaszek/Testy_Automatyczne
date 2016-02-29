import unittest
from selenium import webdriver
from builtins import classmethod


class WidgetArea(unittest.TestCase):

    @classmethod
    def setUp(cls):

        # create new firefox session
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to aplication page
        cls.driver.get("http://demoqa.com/")
        cls.driver.title

    def test_widget_area(self):

        elements = self.driver.find_elements_by_xpath("//div[@id='secondary']/aside")
        self.assertEqual(4, len(elements))

    def test_widget_list(self):

        elements = self.driver.find_elements_by_xpath("//ul[@id='menu-widget']/li")
        self.assertEqual(7, len(elements))

    def test_interaction(self):

        elements = self.driver.find_elements_by_xpath("//ul[@id='menu-interactions']/li")
        self.assertEqual(5, len(elements))

    @classmethod
    def tearDown(cls):
        cls.driver.quit()

    if __name__ == '__main__':
        unittest.main
