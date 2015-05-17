# -*- coding: utf-8 -*-
import unittest
import nose

from selenium.webdriver.firefox.webdriver import WebDriver
from group import UserLogin, Group, GroupTestBase

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class Precondition(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def tearDown(self):
        # We should delete all created test form
        self.deete_group()

        self.wd.find_element_by_link_text("Logout").click()
        self.wd.quit()


class TestGroup(GroupTestBase, Precondition):

    def test_create_group(self):
        """Validation of correct create test group"""

        wd = self.wd
        self.open_home_page(wd)

        self.login(wd, UserLogin.name, UserLogin.password)
        self.create_group(wd, Group(group_name='test', group_header='test', group_footer='test'))

        wd.find_element_by_css_selector("div.msgbox").click()
        wd.find_element_by_link_text("group page").click()


if __name__ == "__main__":
    nose.run(argv=["nosetests", "first_task.py", "--verbosity=2"])