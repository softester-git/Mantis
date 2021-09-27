from model.project import Project


def test_add_project(app, db):
    project_name = app.project.random_string("proj_name_",10)
    project = Project(name=project_name, status="50", enabled="1", view_state="50", description="Project description")
    old_projects = db.get_project_list()
    app.project.create(project)
    new_projects = db.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
