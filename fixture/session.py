from time import sleep


class SessionHelper:

    def __init__(self, app):
        self.app = app

    def login(self, username, password):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id("username").click()
        wd.find_element_by_id("username").clear()
        wd.find_element_by_id("username")
        wd.find_element_by_id("username").send_keys(username)
        wd.find_element_by_xpath("//input[@value='Вход']").click()
        wd.find_element_by_id("password").click()
        wd.find_element_by_id("password").clear()
        wd.find_element_by_id("password").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Вход']").click()

    def logout(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//div[@id='navbar-container']/div[2]/ul/li[3]/a/i[2]").click()
        wd.find_element_by_link_text("Выход").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.logout()

    def is_logged_in(self):
        wd = self.app.wd
        try:
            len(wd.find_element_by_xpath("//div[@id='breadcrumbs']/ul/li/a").text)
            return(True)
        except:
            return(False)

    def is_logged_in_as(self, username):
        wd = self.app.wd
        return(self.get_logged_user() == username)

    def get_logged_user(self):
        wd = self.app.wd
        user_link = (wd.find_element_by_xpath("//div[@id='breadcrumbs']/ul/li/a").text).split(" ( ")
        return(user_link[0])

    def ensure_login(self, username, password):
        if self.is_logged_in():
            if self.is_logged_in_as(username):
                return
            else:
                self.logout()
        self.login(username, password)
