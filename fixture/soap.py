from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password, base_url):
        client = Client(base_url)
        try:
            client.service.mc_login(username, password)
            return(True)
        except WebFault:
            return(False)

    def get_projects(self):
        username = self.app.config["mantis"]["username"]
        password = self.app.config["mantis"]["password"]
        base_url = self.app.config["mantis"]["base_url"]

        client = Client(base_url)
        try:
            l = client.service.mc_projects_get_user_accessible(username, password)
        except WebFault:
            return(False)

        list = []
        for proj in l:
            list.append(Project(id=proj["id"],
                                name=proj["name"],
                                status=str(proj["status"]["id"]),
                                enabled=proj["enabled"],
                                view_state=str(proj["view_state"]["id"]),
                                description=proj["description"]))
        return(list)
