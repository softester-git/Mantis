from suds.client import Client
from suds import WebFault
from model.project import Project


class SoapHelper:

    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client("http://localhost/mantisbt-2.25.2/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return(True)
        except WebFault:
            return(False)

    def get_projects(self, username, password):
        client = Client("http://localhost/mantisbt-2.25.2/api/soap/mantisconnect.php?wsdl")
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
