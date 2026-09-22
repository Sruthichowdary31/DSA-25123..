def insert_begin(self, data):
    new = node(data)
    new.next = self.head
    self.head = new
def insert_end(self, data):
    new = node(data)
    if self.head is none:
        self.head = new
    else:
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new
