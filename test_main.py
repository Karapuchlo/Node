from unittest import TestCase
from main import Node, Stack

class TestNode(TestCase):
    n1 = Node(5)
    assert n1 == 5
    pass


class TestStack(TestCase):
    stack = Stack()
    def test_push(self):
        stack.test_push('data2') == 'data3'

