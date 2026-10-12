import unittest
from tasktrack import remove_task_by_number
import tasktrack


class RemoveTaskTests(unittest.TestCase):
    def test_remove_valid_task(self):
        tasks = ["Write essay", "Study for exam", "Buy groceries"]

        result = tasktrack.remove_task(tasks, "2")

        self.assertTrue(result)
        self.assertEqual(tasks, ["Write essay", "Buy groceries"])

    def test_remove_empty_list(self):
        tasks = []

        result = tasktrack.remove_task(tasks, "1")

        self.assertFalse(result)
        self.assertEqual(tasks, [])

    def test_reject_nonnumeric_selection(self):
        tasks = ["Write essay", "Study for exam"]

        result = tasktrack.remove_task(tasks, "abc")

        self.assertFalse(result)
        self.assertEqual(tasks, ["Write essay", "Study for exam"])

    def test_reject_out_of_range_selection(self):
        tasks = ["Write essay", "Study for exam"]

        result = tasktrack.remove_task(tasks, "99")

        self.assertFalse(result)
        self.assertEqual(tasks, ["Write essay", "Study for exam"])

    def test_remove_task_by_number_valid_selection(self):
        tasks = ["Write essay", "Study for exam", "Buy groceries"]

        removed = tasktrack.remove_task_by_number(tasks, 2)

        self.assertEqual(removed, "Study for exam")
        self.assertEqual(tasks, ["Write essay", "Buy groceries"])

    def test_remove_task_by_number_out_of_range(self):
        tasks = ["Write essay", "Study for exam"]

        removed = tasktrack.remove_task_by_number(tasks, 99)

        self.assertIsNone(removed)
        self.assertEqual(tasks, ["Write essay", "Study for exam"])

    def test_remove_first_task(self):
        """Removing task 1 should remove the first task."""
        # Arrange
        tasks = ["Study", "Exercise", "Read"]
        expected_task = "Study"

        # Act
        removed_task = remove_task_by_number(tasks, 1)

        # Assert
        assert removed_task == expected_task
        assert tasks == ["Exercise", "Read"]

    def test_remove_task_number_too_large(self):
        """A number beyond the list length should not change the list."""
        # Arrange
        tasks = ["Study", "Exercise"]
        expected_tasks = ["Study", "Exercise"]

        # Act
        removed_task = remove_task_by_number(tasks, 5)

        # Assert
        assert removed_task is None
        assert tasks == expected_tasks

    def test_remove_task_number_negative(self):
        """A negative task number should be rejected without changing the list."""
        # Arrange
        tasks = ["Study", "Exercise", "Read"]
        expected_tasks = ["Study", "Exercise", "Read"]

        # Act
        removed_task = remove_task_by_number(tasks, -1)

        # Assert
        assert removed_task is None
        assert tasks == expected_tasks


if __name__ == "__main__":
    unittest.main()
