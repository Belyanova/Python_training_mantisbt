from model.Project import Configurations_Project

def test_add_project(app, db, json_project):
    username = "administrator"
    password = "root"
    app.session.login(username, password)
    old_project = app.soap.get_list_project(username, password)
    app.project.create_new_project(json_project)
    new_project = app.soap.get_list_project(username, password)
    #assert len(old_project) == len(new_project)
    #assert len(old_project) + 1 == len(app.soap.get_list_project(username, password))
    assert len(old_project) == len(new_project)
    assert sorted(old_project, key=Configurations_Project.id_or_max) == sorted(new_project, key=Configurations_Project.id_or_max)