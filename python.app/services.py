
class TaskService:
    """Logika pengelolaan data tugas."""

    _tasks = []
    _next_id = 1

    @classmethod
    def list_tasks(cls):
        return [
            task.copy() for task in cls._tasks
        ]

    @classmethod
    def add_task(cls, title):
        task = {
            "id": cls._next_id,
            "title": title,
            "completed": False
        }

        cls._tasks.append(task)
        cls._next_id += 1

        return task.copy()

    @classmethod
    def delete_task(cls, task_id):
        for index, task in enumerate(cls._tasks):
            if task["id"] == task_id:
                del cls._tasks[index]
                return True

        return False

    @classmethod
    def reset(cls):
        """Mengosongkan data untuk pengujian."""
        cls._tasks = []
        cls._next_id = 1
