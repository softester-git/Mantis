# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper
from selenium.webdriver.support.select import Select
import re


class Application:

    def __init__(self, browser, baseUrl):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser == "chrome":
            options = Options()
            options.binary_location = "/usr/bin/google-chrome-stable"
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            self.wd = webdriver.Chrome(chrome_options=options, executable_path=r'/usr/local/bin/chromedriver')
        elif browser == "ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.wd.implicitly_wait(1)
        self.session = SessionHelper(self)
        self.project = ProjectHelper(self)
        self.james = JamesHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        self.baseUrl = baseUrl

    # common
    def open_home_page(self):
        wd = self.wd
        wd.get(self.baseUrl)

    def destroy(self):
        self.wd.quit()

    def change_field(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_photo(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_field_select(self, field_name, text):
        wd = self.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            Select(wd.find_element_by_name(field_name)).select_by_visible_text(text)

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
