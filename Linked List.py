class Node:
    def __init__(self, data=None, next=None):
        self.data=data
        self.next=next


class LinkedList:
    def __init__(self):
        self.head=None

    def insert_at_beginning(self,val):
        node = Node(val,self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Empty")
            return
        itr = self.head
        ll=''
        while itr:
            ll+=str(itr.data)
            ll+='-->'
            itr=itr.next

        print(ll)

if __name__=='__main__':
    l = LinkedList()
    l.insert_at_beginning(5)
    l.insert_at_beginning(10)
    l.print()


        
