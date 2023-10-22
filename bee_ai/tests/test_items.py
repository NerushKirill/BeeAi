from fastapi.testclient import TestClient

from bee_ai.src.main import app


class Response:
    def __init__(self, client: TestClient, questions_num: int = 1):
        self.response = client.post(
            url="/items/",
            headers={"accept": "application/json"},
            json={"questions_num": questions_num},
        )

    def status(self):
        return self.response.status_code

    def __len__(self):
        return len(self.response.json())


def test_items():
    client = TestClient(app)
    assert Response(client).status() == 200
    assert len(Response(client, questions_num=1)) == 1
    assert len(Response(client, questions_num=10)) == 10
    assert len(Response(client, questions_num=50)) == 50
