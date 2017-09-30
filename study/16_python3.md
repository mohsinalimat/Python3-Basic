# 16_Python3

---

## linked_list 

---

 - linked_list 원리 

 	- node class 와, link 클레스를 나누어서, link 클레스는 각 node 클레스의 인스턴스를 참조를 하고, node 인스턴스에 데이터를 담아서 사용한다. 

 	- liken_list 의 장점은, 데이터를 생성,삭제 할때, list에서의 생성,삭제 할때보다 리소스 낭비가 적다는 장점이 있다. 

 
 ```python
 # linked_list 구현해보자!!!!!!!

class Node :
    
    def __init__(self, data):
        
        self.data = data
        self.next = None
        
        

class Linkedlist:

    # 필요한 member 들 초기화, 예외처리 할때필요함. 
    def __init__(self):
        
        # 값을 insert 할때, 값의 크기와, 맨처음 값, 끝값을 참조해주기 위한 포인터(?) 같은 역활
        self.head = None
        self.tail = None
        
        # 넣은 값을 순차적으로 돌면서 어떤 값이 들어있나를 확인하기 위한 포인터(?) 같은 역활이다.
        self.current = None
        self.before = None
        
        # 내가 넣은 값으 총 크기를 알기 위한...?
        self.num_data = 0
        
        
        
    # insert를 하기전에, linked_list 가 아무것도 없다면, head,tail,current,before 를 맨처음 head 에 몰아 넣고 실행함..    
    def empty(self):
        if self.num_data == 0:
            return True
        else:
            return False 
        
    def size(self):
        return self.num_data
    
    ## 계속 연결 시켜주면서, 값을 넣는것 구현 
    def insert(self, data):
        
        new_node = Node(data)
        
        if self.empty() :
            
            self.head = new_node
            self.tail = new_node
            
            self.num_data += 1 
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.num_data += 1
            
    ## 값이 어떻게 들어있고 그값을 어떻게 찾을것인지 구현
    
    def findData(self, mode = 'next'):
        
        
        if self.empty():#1
            return None
        
        if mode == 'first':#2
            self.before = self.head
            self.current = self.head
            
            return self.current.data
        else:#3
            if self.current.next == None:#4
                return None

            self.before = self.current#5
            self.current = self.current.next

        return self.current.data#6
            
        
     ## delete 구현해보자! 
    
    # 각데이터들은, next에 의해서 연결이 되어있다. 중간의 next를 끊어주면, 그 안에 있는 data가 사라지게됨!
    # remove 하기위한 조건은, finData로 내가 지우고자하는 데이터를 찾아서 지우는것, taget을 설정해서 지우지는 못한다.. 그렇게 설정하려면 다시 설계해야함.. 조금 까다롭다고한다!
    
    def removeData(self):
        
        returnValue = self.current.data
        
        # 예외처리를 해주어야함. 데이터의 개수가 1개 일때
        if self.size() == 1 :
            
            # 현재 가르키고 있는 reference를 모두 None으로 만들어주면, 현재 데이터가 사라짐..!
            self.head = None
            self.tail = None
            
            self.current = None
            self.tail = None
            
        # 데이터가 여러개가 있고, 현재 지우려고 하는 데이터가 head 데이터 일때.
        elif self.current == self.head :
            self.head = self.head.next
            self.before = self.before.next
            self.current = self.current.next
            
        
        
        else :
            # 데이터가 여러개가 있고, 현재 지우려고 하는 데이터가 tail 데이터 일때.
            if self.current == self.tail :
                self.tail = self.before
                
            # 이제 나머지 일반적인 모든 경우
            self.before.next = self.current.next
            self.current = self.before
        
        return print("%s 데이터를 지웠습니다." %(returnValue))
            
            
            
            
        
        
        
----------------------------            
    
    

# insert 원리는 Linkedlist 인스턴스를 만들고, 그 인스턴스에 insert기능을 만들어서, 데이터 값을 넣는데, 값을 넣을때마다 node 인스턴스를, 그 인스턴스 안에 집에 넣고, 각 인스턴스를 참조하는 방식으로     
n1 = Linkedlist()

n1.insert(1)
n1.insert(2)
n1.insert(3)
n1.insert(4)
n1.insert(5)
n1.insert(6)
n1.insert(7)
n1.insert(8)

# 현재 들어가 있는 데이터 출력. 

while n1.findData() != None :
    print(n1.current.data)
    
# removeData 사용방법은, 현재 current가 가르키는 곳을 삭제함!
        
     
 
 ```
 
 ---------------------------
 
 - 정답

 
 ```python
 class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __del__(self):
        print("data of {} is deleted".format(self.data))

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        self.current = None
        self.before = None

        self.num_data = 0

    def empty(self):
        if self.num_data == 0:
            return True
        else:
            return False

    def size(self):
        return self.num_data

    def append(self, data):
        new_node = Node(data)
        
        if self.empty():
            self.head = new_node
            self.tail = new_node
            self.num_data += 1
        else:
            self.tail.next = new_node
            self.tail = new_node
            self.num_data += 1

    def traverse(self, mode = 'next'):
        if self.empty():#1
            return None
        
        if mode == 'first':#2
            self.before = self.head
            self.current = self.head
        else:#3
            if self.current.next == None:#4
                return None

            self.before = self.current#5
            self.current = self.current.next

        return self.current.data#6

    def remove(self):
        ret_data = self.current.data#1
        
        
        #1. 데이터가 하나일 때     
        if self.size() == 1:#2
            self.head = None
            self.tail = None
            self.before = None
            self.current = None
        #2. current == head
        elif self.current is self.head:#3
            self.head = self.head.next
            self.before = self.before.next
            self.current = self.current.next
        else:
            #current == tail
            if self.current is self.tail:#4
                self.tail = self.before
            #일반적인 경우 
            self.before.next = self.current.next#5
            self.current = self.before
            
        self.num_data -= 1
        return ret_data#6

def show_list(slist):
    data = slist.traverse('first')

    if data:
        print(data, end = '  ')
        data = slist.traverse()
        while data:
            print(data, end = '  ')
            data = slist.traverse()
    else:
        print("There is no data")
                
if __name__ == "__main__":
    slist = LinkedList()#1
    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print("\n")

    slist.append(2)#2
    slist.append(3)
    slist.append(1)
    slist.append(5)
    slist.append(2)
    slist.append(10)
    slist.append(7)
    slist.append(2)
    
    
    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print("\n")
    
    
    data = slist.traverse('first')#3
    while data:        
        if data == 2:
            slist.remove()
        data = slist.traverse()

    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)
    print("\n")

    slist.append(3)

    print("데이터의 개수 : {}".format(slist.size()))
    show_list(slist)

   
 
 ```
 
 


## Reference

[linkde_List PDF 자료](/image/single_linked_list_python.pdf)





 