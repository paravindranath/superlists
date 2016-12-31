from .base import FunctionalTest
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import sys
from unittest import skip
#from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):
    def test_layout_and_styling(self):
        # Edith goes to the home page
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)
        ## import pdb; pdb.set_trace()
        # She notices the input box is nicely centered
        inputbox = self.browser.find_element_by_id('id_new_item')
        #import pdb; pdb.set_trace()
        self.assertAlmostEqual( inputbox.location['x'] + (inputbox.size['width']/2),
                                512,
                                delta=5
                                )
        # She starts a new list and sees the input is nicely
        # centered there too
        inputbox.send_keys('testing\n')
        #import pdb; pdb.set_trace()
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual( inputbox.location['x'] + inputbox.size['width']/2,
                                512,
                                delta=5
                                )

        
        # Edith wonders whether the site will remember her list. Then she sees
        # that the site has generated a unique URL for her -- there is some
        # explanatory text to that effect.
        ##self.fail('Finish the test!')
        # She visits that URL - her to-do list is still there.
