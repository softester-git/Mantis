# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
from selenium.webdriver.support.select import Select
import re
import random
import string


class Application:

    def __init__(self, browser, baseUrl, photoPath):
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
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.baseUrl = baseUrl
        self.photoPath = photoPath


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

    def merge_phones_like_on_home_page(self, cont):
        cont.home = "+" + cont.home[2:] if cont.home.startswith("00") else cont.home
        cont.mobile = "+" + cont.mobile[2:] if cont.mobile.startswith("00") else cont.mobile
        cont.work = "+" + cont.work[2:] if cont.work.startswith("00") else cont.work
        cont.phone2 = "+" + cont.phone2[2:] if cont.phone2.startswith("00") else cont.phone2
        merg_phones = "\n".join(filter(lambda x: x != "",
                                map(lambda x: self.clear(x),
                                    filter(lambda x: x is not None,
                                           [self.merge_text_like_on_home_page(cont.home), self.merge_text_like_on_home_page(cont.mobile), self.merge_text_like_on_home_page(cont.work), self.merge_text_like_on_home_page(cont.phone2)]))))
        return(merg_phones)

    def merge_emails_like_on_home_page(self, cont):
        merg_emails = "\n".join(filter(lambda x: x != "",
                                       filter(lambda x: x is not None,
                                              [self.merge_text_like_on_home_page(cont.email), self.merge_text_like_on_home_page(cont.email2), self.merge_text_like_on_home_page(cont.email3)])))
        return(merg_emails)

    def clear(self, s):
        return (re.sub("[() -]", "", s))

    def merge_text_like_on_home_page(self, text):
        merge_text = ' '.join(text.split())
        return(merge_text)
