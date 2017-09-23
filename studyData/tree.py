class TreeNode:
    def __init__(self):
        self._data =None
        self.left = None
        self.right = None
        
    def __del__(self):
        print( 'TreeNode of {} is deleted'.format(self._data))
        
    @property # 그냥 property 를 하면 getter이 됨.
    def data(self):
        return self._data # 트리에서 가지고 있는 진짜 데이터를 반홤
    
    @data.setter # 함수의 이름이 같음.
    def data(self, data):
        self._data = data

# binary tree -> 기능만 모아둔 클래스 
# BST 에서 ADT  ???

class BinaryTree:
    def __init__(self):
        self.root = None # 맨 위의 최상위 노드
        
    def get_root(self):
        return self.root
    
    def set_root(self, r):
        self.root = r # 새로운 root..? 최상위 노드를 설정하는것?(취상위 노드도 참조 해야한다..로 이해해야하나?)
        
    def make_node(self):
        return TreeNode() # 굳이 mkae_node 함수를 만들어서 TreeNode()를 넣어서 해야하나..? 트리노드를 통해서 만들어도 되지만, 바이너리 트리 클래스가 OOP에서는 관련된 모든 기능을 한번에 모아서 사용한다 라는 의미..?
    
    def get_node_data(self, cur): # current node는 ,
        return cur.data # 캡슐화를 해서 함수로 접근하는거다?
    
    def set_node_data(self, cur, data):
        cur.data = data
        
    def get_left_sub_tree(self, cur):
        return cur.left # 이거는 생으로 맴버로 접근하는것 oop에서는 굉장히 싫어함.(함수로 접근해야함..?)
    
    def get_right_sub_tree(self, cur):
        return cur.right
    
    def make_left_sub_tree(self, cur, left):
        cur.left = left
        
    def make_right_sub_tree(self, cur, right):
        cur.right = right
        
    # 전위 순회 함수 
    
    def preorder_traverse(self, cur, func):
        if not cur: # 만약에 cur이 없으면 함수 탈출해.
            return 
        
        #func --> data 처리 함수?
        
        func(cur.data)
        self.preorder_traverse(cur.left, func)
        self.preorder_traverse(cur.right, func)
        
    def inorder_traverse(self, cur, func):
        if not cur:
            return 
        
        self.inorder_traverse(cur.left, func)
        func(cur.data) # 두번쨰인이유는 트리 3개 중에 가운데가 함수...?
        self.inorder_traverse(cur.right, func)
        
    def postorder_tracrese(self, cur, func):
        if not cur:
            return
        
        self.postorder_tracrese(cur.left, func)
        self.postorder_tracrese(cur.right, func)
        func(cur.data)
                 
        
