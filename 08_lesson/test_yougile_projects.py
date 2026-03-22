import pytest
from yougileApi import YougileApi
from configuration import BASE_URL, TOKEN


@pytest.fixture
def api():
    return YougileApi(BASE_URL, TOKEN)


def test_create_project_positive(api):
    response = api.create_project("New Test Project")
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative_empty_title(api):
    response = api.create_project("")
    assert response.status_code == 400


def test_get_project_positive(api):
    new_id = api.create_project("Project to Get").json()["id"]
    response = api.get_project(new_id)
    assert response.status_code == 200
    assert response.json()["title"] == "Project to Get"


def test_get_project_negative_invalid_id(api):
    response = api.get_project("invalid-uuid-123")
    assert response.status_code in [400, 404]


def test_update_project_positive(api):
    new_id = api.create_project("Initial Title").json()["id"]
    response = api.update_project(new_id, "Updated Title")
    assert response.status_code == 200

    check_resp = api.get_project(new_id)
    assert check_resp.json()["title"] == "Updated Title"


def test_update_project_negative_non_existent(api):
    response = api.update_project(
        "00000000-0000-0000-0000-000000000000", "New Title")
    assert response.status_code == 404
