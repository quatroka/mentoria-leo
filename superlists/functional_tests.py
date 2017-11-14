""" File to functional tests. """
import unittest
from selenium import webdriver

class NewVisitorTest(unittest.TestCase):
    """ Class test for New Visitor """

    def setUp(self):
        """ Start browser before tests. """
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """ Close browser after tests. """
        self.browser.quit()

    def test_can_start_a_list(self):
        """ Assert if browser shows 'To-Do' in the title """
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
