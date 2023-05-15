class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        current = self.head
        llstr = ''
        while current:
            llstr += str(current.data) + ' --> '
            current = current.next
        print(llstr)

    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        current = last_node
        llstr = ''
        while current:
            llstr += current.data + '-->'
            current = current.prev
        print("Link list in reverse: ", llstr)

    def get_last_node(self):
        current = self.head
        while current.next:
            current = current.next

        return current

    def get_length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next

        return count
    
    

    def insert_at_begining(self, data):
        if self.head == None:
            node = Node(data, self.head, None)
            self.head = node
        else:
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None, None)
            return

        current = self.head

        while current.next:
            current = current.next

        current.next = Node(data, None, current)

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.insert_at_begining(data)
            return

        count = 0
        current = self.head
        while current:
            if count == index - 1:
                node = Node(data, current.next, current)
                if node.next:
                    node.next.prev = node
                current.next = node
                break

            current = current.next
            count += 1

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        count = 0
        current = self.head
        while current:
            if count == index:
                current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                break

            current = current.next
            count += 1

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert_values(["banana", "mango", "grapes", "orange"])
    ll.print_forward()
    ll.print_backward()
    ll.insert_at_end("figs")
    ll.print_forward()
    ll.insert_at(0, "jackfruit")
    ll.print_forward()
    ll.insert_at(6, "dates")
    ll.print_forward()
    ll.insert_at(2, "kiwi")
    ll.print_forward()
