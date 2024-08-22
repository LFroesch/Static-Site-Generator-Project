import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_props_one(self):
        prop1 = {}

    def test_props_two(self):
        prop1 = {
            "href": "https://www.google.com",
            "target": "_blank"
        }
        prop2 = {
            "href": "https://www.google.com"
        }

    def test_props_three(self):
        prop1 = {
            "href": "https://www.google.com"
        }

    def test_props_four(self):
        prop1 = 0

class TestLeafHTMLNode(unittest.TestCase):
    def test_normal(self):
        test1 = ("p", "Hello")
    def test_all(self):
        LeafNode2 = ("a", "Click", {"href": "https://example.com"})
    def test_med(self):
        LeafNode3 = ("img", "", {"src": "image.jpg", "alt": "An image"})

if __name__ == "__main__":
    unittest.main()