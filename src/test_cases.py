from selenium import webdriver


class DemoQaTests():

    def setUp(self):

        # create new firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to aplication page
        self.driver.get("http://demoqa.com/")

    def tearDown(self):
        self.driver.quit()

    def test_widget_area(self):

        elements = self.driver.find_elements_by_xpath("//div[@id='secondary']/aside")
        try:
            assert len(elements) == 4
            print("Test pass")
        except AssertionError:
            print("Assertion failed")

    def test_widget_list(self):

        elements = self.driver.find_elements_by_xpath("//ul[@id='menu-widget']/li")
        try:
            assert len(elements) == 7
            print("Test pass")
        except AssertionError:
            print("Assertion failed")

    def test_interaction(self):

        elements = self.driver.find_elements_by_xpath("//ul[@id='menu-interactions']/li")
        try:
            assert len(elements) == 5
            print("Test pass")
        except AssertionError:
            print("Assertion failed")

    def test_contact_form(self):

        element = self.driver.find_element_by_xpath("//li[@id='menu-item-64']/a")
        element.click()
        elements = self.driver.find_elements_by_xpath("//form[@class='wpcf7-form']/p")
        try:
            assert len(elements) == 5
            print("Test pass")
        except AssertionError:
            print("Assertion failed")

    def main(self):
        self.setUp()
        self.test_widget_area()
        self.test_widget_list()
        self.test_interaction()
        self.test_contact_form()
        self.tearDown()

if __name__ == '__main__':
    new = DemoQaTests()
    new.main()
