""" File to functional tests. """
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class NewVisitorTest(unittest.TestCase):
    """ Class test for New Visitor """

    def setUp(self):
        """ Start browser before tests. """
        self.browser = webdriver.PhantomJS()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        """ Close browser after tests. """
        self.browser.quit()

    def test_can_start_a_list(self):
        """ Assert if browser can start a list """
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main(warnings='ignore')
