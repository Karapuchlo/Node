from unittest import TestCase
from main import Node, Stack

class TestNode(TestCase):
    n1 = Node(5)
    def test_data(self):
        self.assertEqual(self.n1.data, 5)


class TestStack(TestCase):

    def test_push(self):
        stack = Stack()
        self.assertEqual(stack.push('data2'), None)


