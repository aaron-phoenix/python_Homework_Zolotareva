import requests

api = "https://yougile.com/api-v2"
token = "Bearer your token"
my_headers = {"Content-Type": "application/json", "Authorization": token}


def test_yougile_auth_positive():
    logs = {
        "login": "your e-mail",
        "password": "your password",
        "name": "Поток_109.2"
    }
    resp = requests.post(api + '/auth/companies/', json = logs)
    assert resp.status_code == 200


def test_yougile_projects_positive():
    new_company = {
        "title": "Elena",
        "users": {
        "d2a23ce5-e879-4ec0-997c-9f035c1f3ded": "admin"
        },
    }

    resp = requests.post(api + f'/projects/', json = new_company, headers = my_headers)
    project_id = resp.json()["id"]
    assert resp.status_code == 201
    resp = requests.put(api + f'/projects/{project_id}', json = {"deleted":True}, headers = my_headers)
    resp = requests.get(api + f'/projects/{project_id}', headers = my_headers)
    print(resp.text)
    assert resp.status_code ==200


def test_yougile_projects_negative():
    new_company = {
        "title": "",
        "users": {
        "d2a23ce5-e879-4ec0-997c-9f035c1f3ded": "user"
        }
    }

    resp = requests.post(api + f'/projects/', json = new_company, headers = my_headers)
    assert resp.status_code == 400


def test_yougile_project_get_id_positive():
    new_company1 = {
        "title": "Elena1",
        "users": {
        "d2a23ce5-e879-4ec0-997c-9f035c1f3ded": "admin"
        }
    }

    resp = requests.post(api + f'/projects/', json = new_company1, headers = my_headers)
    project_id1 = resp.json()["id"]
    assert resp.status_code == 201
    resp = requests.get(api + f'/projects/{project_id1}', headers = my_headers)
    assert resp.status_code == 200
    resp = requests.put(api + f'/projects/{project_id1}', json = {"deleted":True}, headers = my_headers)
    assert resp.status_code ==200


def test_yougile_project_get_id_negative():
    new_company1 = {
        "title": "Elena1",
        "users": {
        "d2a23ce5-e879-4ec0-997c-9f035c1f3ded": "admin"
        }
    }

    resp = requests.post(api + f'/projects/', json = new_company1, headers = my_headers)
    project_id2 = 0
    resp = requests.get(api + f'/projects/{project_id2}', headers = my_headers)
    assert resp.status_code == 404


def test_yougile_project_change_positive():
    new_company = {
        "title": "Elena2",
        "users": {
        "d2a23ce5-e879-4ec0-997c-9f035c1f3ded": "admin"
        }
    }

    resp = requests.post(api + f'/projects/', json = new_company, headers = my_headers)
    project_id3 = resp.json()["id"]
    resp = requests.get(api + f'/projects/{project_id3}', headers = my_headers)
    title = resp.json()["title"]
    assert resp.status_code == 200
    assert title == "Elena2"

    resp = requests.put(api + f'/projects/{project_id3}', json ={"title":"Elena3"}, headers = my_headers)
    resp = requests.get(api + f'/projects/{project_id3}', headers = my_headers)
    new_title = resp.json()["title"]
    assert new_title == "Elena3"
    resp = requests.put(api + f'/projects/{project_id3}', json = {"deleted":True}, headers = my_headers)
    assert resp.status_code ==200


def test_yougile_project_change_negative():
    new_company = {
        "title": "Elena2",
        "users": {
        "d2a23ce5-e879-4ec0-997c-9f035c1f3ded": "admin"
        }
    }

    resp = requests.post(api + f'/projects/', json = new_company, headers = my_headers)
    project_id3 = 0
    resp = requests.get(api + f'/projects/{project_id3}', headers = my_headers)
    assert resp.status_code == 404

    resp = requests.put(api + f'/projects/{project_id3}', json ={"title":"Elena3"}, headers = my_headers)
    resp = requests.get(api + f'/projects/{project_id3}', headers = my_headers)
    assert resp.status_code == 404
