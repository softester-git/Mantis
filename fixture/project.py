import random
import string
from selenium.webdriver.support.select import Select
from model.project import Project
from time import sleep


class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def create(self, project):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//button[@type='submit']").click()
        self.fill_project_form(project)
        wd.find_element_by_xpath("//input[@value='Добавить проект']").click()
        wd.find_element_by_link_text("Продолжить").click()

    def open_projects_page(self):
        wd = self.app.wd
        if not wd.current_url.endswith("/manage_proj_page.php"):
            wd.find_element_by_xpath("//div[@id='sidebar']/ul/li[7]/a/i").click()
            wd.find_element_by_link_text(u"Управление проектами").click()

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_id("project-name").click()
        wd.find_element_by_id("project-name").clear()
        wd.find_element_by_id("project-name").send_keys(project.name)
        wd.find_element_by_id("project-status").click()
        #Select(wd.find_element_by_id("project-status")).select_by_visible_text(project.status)
        Select(wd.find_element_by_id("project-status")).select_by_value(project.status)
        if not project.enabled:
            wd.find_element_by_xpath("//form[@id='manage-project-create-form']/div/div[2]/div/div/table/tbody/tr[3]/td[2]/label/span").click()
        wd.find_element_by_id("project-view-state").click()
        Select(wd.find_element_by_id("project-view-state")).select_by_value(project.view_state)
        wd.find_element_by_id("project-description").click()
        wd.find_element_by_id("project-description").clear()
        wd.find_element_by_id("project-description").send_keys(project.description)

    def random_string(self, prefix, maxlen):
        symbols = string.ascii_letters + string.digits
        return (prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))]))

    def delete(self, project_id):
        wd = self.app.wd
        self.open_projects_page()
        wd.find_element_by_xpath("//a[@href='manage_proj_edit_page.php?project_id=" + project_id + "']").click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
        wd.find_element_by_xpath("//input[@value='Удалить проект']").click()
