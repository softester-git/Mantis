from model.project import Project


def test_add_project(app, db, config):
    project_name = app.project.random_string("proj_name_",10)
    project = Project(name=project_name, status="50", enabled=True, view_state="50", description="Project description")
    old_projects = app.soap.get_projects(config["mantis"]["username"], config["mantis"]["password"], config["mantis"]["base_url"])
    app.project.create(project)
    new_projects = app.soap.get_projects(config["mantis"]["username"], config["mantis"]["password"], config["mantis"]["base_url"])
    old_projects.append(project)
    assert sorted(old_projects, key=Project.id_or_max) == sorted(new_projects, key=Project.id_or_max)
