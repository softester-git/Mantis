import mysql.connector
from model.project import Project


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_project_list(self):
        project_list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, name, status, enabled, view_state, description from mantis_project_table")
            for row in cursor:
                (id, name, status, enabled, view_state, description) = row
                project_list.append(Project(id=str(id), name=str(name).strip(), status=str(status), enabled=str(enabled), view_state=str(view_state), description=str(description)))
        finally:
            cursor.close()
        return(project_list)

    def project_count(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("select count(*) as cnt from mantis_project_table")
            row = cursor.fetchone()
            out = row[0]
        except:
            out = False
        finally:
            cursor.close()
        return(out)


    def destroy(self):
        self.connection.close()