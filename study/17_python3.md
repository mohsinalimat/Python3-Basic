# 17_Python



## reference

### [BST PDF 자료](/image/BST.pdf)

---

## BT(BinaryTree), BTS(Binary Search Tree)

 - BT: BTS 의 개념을 잡기위해서, node 에 데이터를 넣어서, tree 형식으로 묶어놓는 방식을 취함. 최대약점은, delete, insert 등이 용이 하지 않음. 

 
```python

class TreeNode:
    
    # tree에 붙일 node 값 설정. 
    # Node 는 양옆을 붙여주고, 데이터를 가지고 있어줌
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None
        
    # 데이터 삭제시 해당값 프린트.   
    def __del__(self):
        print("TreeNode of {} is deleted".format(self.data))
        
class BinaryTree:
    
    def __init__(self):
    # 루트노드를 가르키는 맴버는 하나다.
        self.root = None
    
    # 현재 tree의 root 반환 
    def get_root(self):
        return self.root
    
    # root 설정 
    def set_root(self, r):
        self.root = r
        
    
    # 새로운 노드를 만들고 반환합니다
    def make_node(self):
        new_node = TreeNode()
        return new_node
    
    
    # 현재 노드의 데이터를 반환합니다
    def get_node_data(self, cur):
        return cur.data
    
    # 노드의 데이터 설정
    def set_node_data(self, cur, data):
        cur.data = data
        
        
    # 노드의 왼쪽 설정 -> 노드를 왼쪽 트리에 붙인다.
    def set_node_left(self, cur, left):
        cur.left = left 
        
    # 노드의 오른쪽 설정 -> 노드를 오른쪽 트리에 붙인다
    def set_node_right(self,cur, right):
        cur.right = right
        
    # 왼쪽 노드 반환
    def get_node_left(self, cur):
        return cur.left.data
    
    #오른쪽 노드 반환
    def get_node_right(self, cur):
        return cur.right.data
    
    
    # 전위순회 함수, 니은자로 움직임.
    
    def preodredr_traverse(self, cur, func):
        
        # 이거 무슨의미일까.. 정확히 와닿지가않는다.
        # cur.data 가 None 일때 리커션 종료 
        if not cur:
            return 
        
        func(cur.data)
        self.preodredr_traverse(cur.left, func)
        self.preodredr_traverse(cur.right, func)
     
    
    #중위 순회로 트리를 순회
    def inorder_traverse(self, cur, func):
        if not cur:
            return

        self.inorder_traverse(cur.left, func)
        func(cur.data)
        self.inorder_traverse(cur.right, func)

        
    #후위 순회로 트리를 순회
    def postorder_traverse(self, cur, func):
        if not cur:
            return

        self.postorder_traverse(cur.left, func)
        self.postorder_traverse(cur.right, func)
        func(cur.data)

    ## 전, 중, 후위 순회 의 순서보면, 프린트 하는 함수의 위치에 따라서, 전, 중, 후위 함수 구별 하자.. 아직 이것을 설계하기에는 조금 무리일것 같다.
    
    
#binaryTree 인스턴스 생성
bt = BinaryTree()

## 노드 생성과, 각 노드의 데이터 값을 넣었다.
n1 = bt.make_node()
bt.set_node_data(n1, 1)

n2 = bt.make_node()
bt.set_node_data(n2, 2)

n3 = bt.make_node()
bt.set_node_data(n3, 3)

n4 = bt.make_node()
bt.set_node_data(n4, 4)

n5 = bt.make_node()
bt.set_node_data(n5, 5)

n6 = bt.make_node()
bt.set_node_data(n6, 6)

n7 = bt.make_node()
bt.set_node_data(n7, 7)

# 노드를 붙여보자. 맨처음 root node 설정을 하자 

bt.set_root(n1)

# 2를 1의 왼쪽으로
bt.set_node_left(n1, n2)

# 3을 1의 오른쪽으로 
bt.set_node_right(n1, n3)

# 4를 2의 왼쪽, 5를 2의 오른쪽으로
bt.set_node_left(n2, n4)
bt.set_node_right(n2,n5)

# 6을 3의 왼쪽으로, 7을 3의 오른쪽으로
bt.set_node_left(n3,n6)
bt.set_node_right(n3,n7)

# 잘 붙어 있는지 확인해보자

# root 확인
print(bt.root.data) # 1

# 1의 왼, 오른 쪽
print(n1.left.data, n1.right.data) # 2 3

# 2의 왼, 오른쪽
print(n2.left.data, n2.right.data) # 4 5

#3의 왼, 오른쪽
print(n3.left.data, n3.right.data) # 6 7


# 전, 중, 후 위 순회 값 확인..
f = lambda x: print(x, end = ' ')

bt.preodredr_traverse(bt.root, f) # 1 2 4 5 3 6 7 
bt.inorder_traverse(bt.root, f) # 4 2 5 1 6 3 7
bt.postorder_traverse(bt.root, f) # 4 5 2 6 7 3 1



    


```

---

## BST(Binary Search Tree)



```python
from binary_tree import *

class BinarySearchTree(BinaryTree):
    def insert(self, data):
        #삽입할 노드 생성 및 데이터 설정
        new_node = self.make_node()
        self.set_node_data(new_node, data)

        cur = self.get_root()
        #루트 노드가 없을 때
        if cur == None:
            self.set_root(new_node)
            return

        #삽입할 노드의 위치를 찾아 삽입
        while True:
            #삽입할 데이터가 현재 노드 데이터보다 작을 때
            if data < self.get_node_data(cur):
                #왼쪽 자식 노드 존재하면
                if self.get_left_sub_tree(cur):
                    cur = self.get_left_sub_tree(cur)
                #존재하지 않으면 노드 삽입
                else:
                    self.make_left_sub_tree(
                        cur, new_node)
                    break
            #삽입할 데이터가 현재 노드 데이터보다 클 때
            elif data > self.get_node_data(cur):
                #오른쪽 자식 노드 존재하면
                if self.get_right_sub_tree(cur):
                    cur = self.get_right_sub_tree(cur)
                #존재하지 않으면 노드 삽입
                else:
                    self.make_right_sub_tree(
                        cur, new_node)
                    break

    def search(self, target):
        cur = self.get_root()
        
        while cur != None:
            #target 데이터를 찾으면 노드를 반환
            if target == self.get_node_data(cur):
                return cur
            #target 데이터가 노드 데이터보다 작으면
            #왼쪽 자식 노드로 이동
            elif target < self.get_node_data(cur):
                cur = self.get_left_sub_tree(cur)
            #target 데이터가 노드 데이터보다 크면
            #오른쪽 자식 노드로 이동
            elif target > self.get_node_data(cur):
                cur = self.get_right_sub_tree(cur)
        return cur
    
    #리프 노드일 때
    def remove_leaf(self, parent, del_node):
        #삭제 노드가 루트 노드일 때
        if del_node == self.get_root():
            self.set_root(None)
            return del_node

        if self.get_left_sub_tree(parent) == del_node:
            self.make_left_sub_tree(parent, None)
        else:
            self.make_right_sub_tree(parent, None)
            
        return del_node  
    
    #자식 노드가 하나일 때
    def remove_one_child(self, parent, del_node):
        #삭제 노드가 루트 노드일 때
        if del_node == self.get_root():
            if self.get_left_sub_tree(del_node):
                self.set_root(
                    self.get_left_sub_tree(del_node))
            else:
                self.set_root(
                    self.get_right_sub_tree(del_node))

            return del_node
        
        #삭제 노드의 자식 노드를 받아와서 
        del_child = None
        if self.get_left_sub_tree(del_node):
            del_child = \
            self.get_left_sub_tree(del_node)
        else:
            del_child = \
            self.get_right_sub_tree(del_node)

        #삭제 노드의 부모 노드에 연결
        if self.get_left_sub_tree(parent) == del_node:
            self.make_left_sub_tree(parent, del_child)
        else:
            self.make_right_sub_tree(parent, del_child)

        return del_node

    #자식 노드가 두 개일 때
    def remove_two_children(self, del_node):
        #루트 노드를 실제로 삭제하는 게 아니므로
        #루트 노드에 대한 경우가 필요 없다.

        rep_parent = del_node
        #삭제 노드의 왼쪽 서브 트리에서
        replace = \
        self.get_left_sub_tree(rep_parent)

        #가장 큰 데이터를 가진 노드를 찾는다.        
        while self.get_right_sub_tree(replace):
            rep_parent = replace
            replace = \
            self.get_right_sub_tree(replace)

        #삭제 노드와 대체 노드의 데이터 교환
        temp_data = \
        self.get_node_data(replace)
        self.set_node_data(replace,
                    self.get_node_data(del_node))
        self.set_node_data(del_node, temp_data)

        #대체 노드에 왼쪽 서브 트리가 있는 경우
        if self.get_left_sub_tree(rep_parent) == replace:
            self.make_left_sub_tree(rep_parent,
                self.get_left_sub_tree(replace))
        else:
            self.make_right_sub_tree(rep_parent,
                self.get_left_sub_tree(replace))

        return replace    

    def remove(self, target):
        #삭제 노드를 찾는다.
        del_parent = self.get_root()
        del_node = self.get_root()

        while True:
            #target이 존재하지 않는다.
            if del_node == None:
                return None

            if target == \
               self.get_node_data(del_node):
                break
            
            elif target < \
                 self.get_node_data(del_node):
                del_parent = del_node
                del_node = \
                self.get_left_sub_tree(del_node)
                
            elif target > \
                 self.get_node_data(del_node):
                del_parent = del_node
                del_node = \
                self.get_right_sub_tree(del_node)
                
        #삭제 노드가 리프 노드일 때
        if self.get_left_sub_tree(del_node) == None and \
           self.get_right_sub_tree(del_node) == None:
            return self.remove_leaf(del_parent, del_node)
        #삭제 노드의 자식 노드가 하나일 때
        elif self.get_left_sub_tree(del_node) == None or \
             self.get_right_sub_tree(del_node) == None:
            return self.remove_one_child(del_parent, del_node)
        #삭제 노드의 자식 노드가 두 개일 때
        else:
            return self.remove_two_children(del_node)  

if __name__ == "__main__":
    bst = BinarySearchTree()
    
    #insert
    bst.insert(6)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(8)
    bst.insert(10)
    bst.insert(9)
    bst.insert(11)

    f = lambda x: print(x, end = '  ')
    #전위 순회
    bst.preorder_traverse(bst.get_root(), f)
    print("")
    
    #search
    print("searched data : {}".format(bst.search(8).data))

    #remove - 1 : 리프 노드일 때
    bst.remove(9)

    #remove - 2 : 자식 노드 하나일 때
    #bst.remove(8)

    #remove - 3: 자식 노드 두 개일 때
    #bst.remove(6)
    
    bst.preorder_traverse(bst.get_root(), f)


    
    
```

> 위의 BST의 최대 약점은, root를 설정하면, root 내가 집어넣는 데이터에 따라서 유동적으로 변하지 않음. 현업에서 가장 많이쓰는 데이터 저장 방식이라고 하는데, 설계하기가 매우 까다롭고 어렵다.. 맨처음 설계한 BT 의 데이터를 import 해서 만듬... remove의 경우가 경우의수가 가장 많았고 까다로웠다. 
>
> 나중에 swift 로도 한번 만들어보자.


