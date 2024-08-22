import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_noteq(self):
        node = TextNode("This isn't a text node", "italics")
        node2 = TextNode("This isn't a text node", "bold")
        self.assertNotEqual(node, node2)

    def test_noteqtwo(self):
        node = TextNode("These aren't the droids you're looking for", "italics")
        node2 = TextNode("This isn't a text node", "italics")
        self.assertNotEqual(node, node2)

    def test_equal(self):
        node = TextNode("These aren't the droids you're looking for", "italics")
        node2 = TextNode("These aren't the droids you're looking for", "italics")
        self.assertEqual(node, node2)
    
    def test_equalized(self):
        node = TextNode("!@#$%^(*@#$)", "italics")
        node2 = TextNode("!@#$%^(*@#$)", "italics")
        self.assertEqual(node, node2)

if __name__ == "__main__":
    unittest.main()