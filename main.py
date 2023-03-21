#Для начала создать класс узла в виде:

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None 

#Затем создать класс Stack, который будет содержать атрибут top, хранящий ссылку на верхний узел стека:

class Stack:
    def __init__(self):
        self.top = None 

    def push(self, data):
        node = Node(data)
        node.next = self.top
        self.top = node
#Здесь мы создаем экземпляр класса Node с аргументом data и добавляем его к стеку путем создания связи


