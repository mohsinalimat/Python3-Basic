# 10_Python3


**Reference: <https://github.com/ythwork>**

---

## Class, constructor, destructor, instance method, class member, message passing

---

## class
 - class의 구조
 ```python
 #class
class Account:
   #constructor
    def __init__(self, name, money):
        #instance member
        self.user = name
        self.balance = money
    #instance method 
    def deposit(self, money):
        if money < 0:
            return
        self.balance += money
 ```
---

## constructor
  - 생성자 
    - 객체 생성할 때 호출
    - 멤버 초기화
```python
def __init__(self, name, money):
        #instance member
        self.user = name
        self.balance = money
```
---

##  destructor
  - 소멸자
  - 객체 소멸할 때 호출
  - 주 목적은 메모리 해제
```python
#destructor
    def __del__(self):
        pass
```
---

## instance member
  - variable in object
```python
def __init__(self, name, money):
        #instance member
        self.user = name
        self.balance = money
```
---

## instance method
  - function used by object
  - 객체 생선 전에는 호출할 수 없다.
```python
def deposit(self, money):
        if money < 0:
            return
        
        self.balance += money
```
---

## class member
  - variable in class
  - 모든 객체가 공유
```python
class Account:
    #class member
    name = 'Good life'
    interest_rate = 7.0
    kind = 'demand deposit'
```
---

## class method
  - function used as global function
  - 객체 생성 전에도 호출할 수 있다.
```python
    #class method
    @classmethod
    def get_account_info(cls):
        '''
        cls.get_account_info()
        -> (name, interest_rate, kind)
        '''
        return cls.name,\
        cls.interest_rate,\
        cls.kind
```
---

## object 생성
```python
my_acnt = Account('greg', 5000)
```
---

## instance method 호출
```python
#1. by object
my_acnt.deposit(500)
#2. by class : 쓰이지 않음
Account.deposit(my_acnt, 500)
```
---

## class member 접근
```python
#1.by class 
print(Account.name, Account.interest_rate, Account.kind)    
#2.by object
print(my_acnt.name, my_acnt.interest_rate, my_acnt.kind)
```
---

## class method 호출
```python
#1.by class
info = Account.get_account_info()
#2.by object
info = my_acnt.get_account_info()
```
---

## message passing
  - interacts with other objects
    - by calling methods
    - changes the state of the object(member)
    - asks the receiver to call a specific method
```python
def transfer(self, other, money):
        mon = self.withdraw(money)
        if mon:
            #상대 객체의 메서드를 호출
            other.deposit(mon)
            return True
        else:
            return False
```



 - message passing 예제

 
```python

class Account:
    def __init__(self, name, money):
        
        self.name = name
        self.money = money
        
     # 입금 기능   
    def deposit(self, money):
        
        if money < 0:
            return
        else:
            self.money += money
            print("%s 님 계좌로 %s 원 입금됨. 통장 잔액은 %s 입니다" %(self.name, money, self.money))
            
    # 출금 기능
    
    def withdrawal(self, money):
        
        if money > self.money :
            return "출금 금액이 통장 잔고보다 많습니다"
        else:
            
            self.money -= money
            print("%s 님 계좌에서 %s원 출금합니다. 현재 통장 잔액은 %s 입니다." %(self.name, money, self.money))
            
    ## 현재 금액 확인 
    
    def check_my_money(self):
        
        print("%s 님 계좌의 잔액은 %s 입니다" %(self.name, self.money))
        
    ## message passing 
    
    def transfer(self, you, money):
        
        if self.money < you.money :
            print("잔액이 부족합니다.")
        else:
            self.money -= money
            you.money += money
            
            print("%s 님계좌에서 %s 님 계좌로 이체합니다, %s님 현재 잔액은 %s 입니다." %(self.name, you.name, self.name, self.money))


minjun = Account("민준", 2000)
sunghee = Account("성희", 5000)

minjun.deposit(5000) # 민준 님 계좌로 5000 원 입금됨. 통장 잔액은 9000 입니다
minjun.withdrawal(1000) # 민준 님 계좌에서 1000원 출금합니다. 현재 통장 잔액은 8000 입니다.
minjun.check_my_money() # 민준 님 계좌의 잔액은 8000 입니다
minjun.transfer(sunghee, 2000)민준 님 계좌에서 성희 님 계좌로 이체합니다, 민준님 현재 잔액은 6000 입니다. 


```

> message passing 원리는, 객체가 가지고 있는 내부정보를 내가 입력한 input값을 가지고 어떻게 변경 해주느냐를 컨트롤 하는 문제인것 같다.!