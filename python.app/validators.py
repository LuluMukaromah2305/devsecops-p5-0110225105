
def validate_task_title(value):
    """Memvalidasi judul tugas."""

    if not isinstance(value, str):
        return None, "Title must be a string"

    title = value.strip()

    if not title:
        return None, "Title cannot be empty"

    if len(title) > 120:
        return None, "Title must be 120 characters or fewer"

    return title, None
