class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

class UnorderedList:
    
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True

            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    def show_list(self):
        l=UnorderedList.size(self)
        current = self.head
        temp = current.getData()
        print(temp,end=' -> ')
        for i in range(l-1):
            current = current.getNext()
            temp = current.getData()
            print(temp,end=' -> ')
        print('None')

    def show_item(self,pos):
        current = self.head
        for i in range(pos-1):
            current=current.getNext()
            
        return(current.getData())
    
    def append(self,item):

        l=UnorderedList.size(self)
        current = self.head

        for i in range(l-1):
            current = current.getNext()
        temp=Node(item)
        current.setNext(temp)

    def insert(self,item,pos):

        current = self.head
        temp=Node(item)
        l=UnorderedList.size(self)
        
        if pos == l:
            for i in range(pos-1):
                current = current.getNext()
            current.setNext(temp)
        
        elif pos>=2:
            for i in range(pos-2):
                current = current.getNext()
            rest=current.getNext()
            current.setNext(temp)
            temp.setNext(rest)
        else:
            UnorderedList.add(self,item)
        
    def pop(self,pos):
        current = self.head
        l=UnorderedList.size(self)

        if pos == l:
            for i in range(pos-2):
                current = current.getNext()
            toPOP=current.getNext()
            value = toPOP.getData()
            current.setNext(None)
            return value
            
        elif pos>=2:
            for i in range(pos-2):
                current = current.getNext()
            toPOP = current.getNext()
            rest = toPOP.getNext()
            current.setNext(rest)
            value = toPOP.getData()
            return value
        else:
            current = current.getData()
            UnorderedList.remove(self,current)
            return current

    def index(self,item):
        l=UnorderedList.size(self)
        count=1
        current = self.head
        
        while(count<=l):
            if current.getData() == item:
                return count           
            else:
                count+=1
                current = current.getNext()
        return('Nie ma takiego elementu na liście')

