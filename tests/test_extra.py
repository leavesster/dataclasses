from dataclass.extra import Person
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

        d = {
            "name": "Alice",
            "age": 30,
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
            Person(**d)

    def test_serialize_person_with_extra_field(self):
        d = {
            "name": "Alice",
            "age": 30,
            "city": "New York",
            "extra": "extra"
        }

        p = Person(**d)
        self.assertEqual(p.name, "Alice")
        self.assertEqual(p.age, 30)
        self.assertEqual(p.city, "New York")
        self.assertFalse(hasattr(p, "extra"))