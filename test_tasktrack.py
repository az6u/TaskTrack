import unittest

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


if __name__ == "__main__":
    unittest.main()
