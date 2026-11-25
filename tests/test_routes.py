import pytest

from app import create_app


@pytest.mark.parametrize(
    "url",
    [
        "/",
        "/history",
        "/documentation",
        "/hill/",
        "/playfair/",
        "/cryptanalysis/hill",
        "/cryptanalysis/playfair",
    ],
)
def test_pages_ok(url):
    client = create_app().test_client()
    assert client.get(url).status_code == 200
