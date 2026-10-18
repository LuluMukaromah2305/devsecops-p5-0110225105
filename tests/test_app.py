
import unittest

from app import create_app
from services import TaskService


class TaskManagerApiTests(unittest.TestCase):

    def setUp(self):
        TaskService.reset()
        self.client = create_app(
            testing=True
        ).test_client()

    def test_home_endpoint(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["application"],
            "Task Manager API"
        )

    def test_health_endpoint(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_json()["status"],
            "ok"
        )

    def test_create_and_list_task(self):
        response = self.client.post(
            "/tasks",
            json={"title": "Finish assignment"}
        )

        self.assertEqual(response.status_code, 201)

        listed = self.client.get("/tasks")

        self.assertEqual(
            len(listed.get_json()["tasks"]),
            1
        )

    def test_reject_empty_title(self):
        response = self.client.post(
            "/tasks",
            json={"title": "   "}
        )

        self.assertEqual(response.status_code, 400)

    def test_delete_missing_task(self):
        response = self.client.delete("/tasks/999")

        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()
