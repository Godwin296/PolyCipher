from app import create_app


def test_index_ok():
    client = create_app().test_client()
    response = client.get("/")
    assert response.status_code == 200
