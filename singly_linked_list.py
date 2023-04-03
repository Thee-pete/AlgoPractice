class Node:
    def __init__(self,data = None, next= None):
        self.data = data
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def print(self):
        if self.head is None:
            print("List is empty")
            return
        current = self.head
        llstr = ""
        while current:
            llstr += str(current.data) + "-->" if current.next else str(current.data)
            current = current.next
        print(llstr)
        
    def get_length(self):
        count =0
        current = self.head
        while current:
            count+=1
            current = current.next
        return count
    
    def insert_at_beginning(self,data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data, None)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data, None)
        
    def insert_at(self,data,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        current = self.head
        count = 0
        while current:
            if count == index -1:
                node = Node(data, current)
                current.next = node
                break
            count += 1
            current = current.next
            
    def remove_at(self,data,index):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")
        if index == 0 :
            self.head = self.head.next
            return
        count = 0 
        current = self.head
        while current:
            if count == index - 1:
                current.next = current.next.next
                break
            count +=1
            current = current.next
            
    def insert_values(self,data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
            
            
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return
        current = self.head
        while current: 
            if current.data == data_after:
                current.next = Node(data_to_insert,current.next)
                break
            current = current.next
            
    def remove_by_value(self,data):
        if self.head is None:
            return 
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                break
            current = current.next
            
if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_values(["banana","mango","grapes","orange"])
    ll.print()
    ll.insert_after_value("mango","apple")
    ll.print()
    ll.remove_by_value("orange")
    ll.print()
