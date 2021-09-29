from model.project import Project
import random


def test_del_project(app, db, config):
    if db.project_count() == 0:
        app.project.create(Project(name="Project_for_delete"))
    old_projects = app.soap.get_projects(config["mantis"]["username"], config["mantis"]["password"], config["mantis"]["base_url"])
    project = random.choice(old_projects)
    app.project.delete(project.id)
    assert len(old_projects) - 1 == db.project_count()
    new_projects = app.soap.get_projects(config["mantis"]["username"], config["mantis"]["password"], config["mantis"]["base_url"])
    old_projects.remove(project)
    assert old_projects == new_projects
