from dataclass.person import Person
import unittest

class TestData(unittest.TestCase):
        
    def test_serialize_person(self):
        d = {
            "name": "Alice",
            "age": 30,
            "city": "New York"
        }

        p = Person(**d)
        self.assertEqual(p.name, "Alice")
        self.assertEqual(p.age, 30)
        self.assertEqual(p.city, "New York")

    def test_serialize_person_without_city(self):
        d = {
            "name": "Alice",
            "age": 30
        }

        p = Person(**d)
        self.assertEqual(p.name, "Alice")
        self.assertEqual(p.age, 30)
        self.assertIsNone(p.city)

    def test_serialize_person_missing_require(self):
        d = {
            "name": "Alice"
        }

        with self.assertRaises(TypeError):
            Person(**d) # type: ignore

    def test_serialize_person_with_extra_field(self):
        d = {
            "name": "Alice",
            "age": 30,
            "city": "New York",
            "extra": "extra"
        }

        with self.assertRaises(TypeError):
            p = Person(**d)
            self.assertIsNone(p)