# 9_Python3


**Reference: <https://github.com/ythwork>**

---

## OOP

---

## OOP 

- 개념 
	- Abstraction(추상화)
	- Encapsulation(캡슐화)
	- information hidning(정보 은닉)
	- Inheritance(상속성)
	- Polymorphism(다형성)

---


## Object-oriented
  - 실제 세계의 객체를 어떻게 모델링하는가?
    - member 
      -  무엇이 이 객체를 다르게 하는가?
    - method  
      - 이 객체는 무엇을 하는가?
      - 이 객체를 이용하면 무엇을 할 수 있는가?
---

## Encapsulation
  - 멤버(변수)와 메서드(함수)를 클래스로 묶는 것
  - the bundling of data with methods
  - 정보 은닉을 포함 
---

## information hiding
  - restrict direct access to member or method
  - hide a member from user
  - allow access by access functions
```python
>>> class Base:
	def __init__(self, data):
		self.data = data
	def get_data(self):
		return self.data
	def set_data(self, data):
		self.data = data
```
---
## information hiding
  - access modifiers
    - public, protected, private in C++
```C++
class Base{
private:
	int x;
public:
	int get_x() { return x; }
	void set_x(int n) { x = n; }
};
```  
---
---
## information hiding
  - python DO NOT support Information hiding
```python
>>> class Base:
	def __init__(self, n):
        #looks like information hiding......
		self.__x = n	
>>> b = Base(5)
>>> b.__x
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    b.__x
AttributeError: 'Base' object has no attribute '__x'
```
---
## information hiding
```python
# it is not information hiding
>>> b.__dict__
{'_Base__x': 5}
>>> b._Base__x
5
```
---
## information hiding
```python
>>> class Base:
	def __f(self):
		print('__f executed')		
>>> b = Base()
>>> b.__f()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    b.__f()
AttributeError: 'Base' object has no attribute '__f'
```
---
## information hiding
```python
>>> dir(b)
['_Base__f', '__class__', ...]
>>> b._Base__f()
__f executed
```
---


## Inheritance

  -  relations between classes
  - choose either inheritance or composition
---

## IS-A 
  - A laptop IS-A computer
  - ~은 ~의 한 종류이다.
  - Inheritance
    - reusability
      - has members and methods of base classes
      - adds members and methods

```python
#base, parent class
class Computer:
    pass
    
#derived, child class
class Laptop(Computer):
    pass 
```
---
## HAS-A
  - A policeman has a gun
  - ~이 ~을 가지고 있다. or 포함하고 있다.
  - Composition(합성) or Aggregation(통합)

```python
class Gun:
	pass
        
class Police:
    def __init__(self):
        self.gun = Gun()
```
---
## Polymorphism
  - 다형성
  - Inheritance에서 가장 중요한 개념
```python
from abc import *
class Animal(metaclass = ABCMeta):
    @abstractmethod
    def say(self):
        pass
class Dog(Animal):
    def say(self):
        print('BOW-WOW')
class Cat(Animal):
    def say(self):
        print('MEW MEW')
class Duck(Animal):
    def say(self):
        print('QUACK QUACK')
```
---
## Polymorphism
  - In inheritance, 
    the same instance method of
    objects from different classes
    results in different behaviors.
    
---
## Method overriding
  - overrides(replaces) a method provided by base class
  - same name, args
  - execution : by the object 
---
## abstract class
  - 추상 클래스
    - 인스턴스를 만들 수 없다.
    - abstract method
      - pure virtual method
       : 몸체(body)가 없는 함수
      - 파생 클래스에서 반드시 overriding 해야 함

## simple example of polymorphism

 - 추상 클래스
 - 인스턴스를 만들 수 없다.
 - 인터페이스를 제공한다.


```python
from abc import *


class Animal(metaclass = ABCMeta):
    @abstractmethod
    def say(self):
        pass

class Dog(Animal):
    def say(self):
        print('BOW-WOW')

class Cat(Animal):
    def say(self):
        print('MEW MEW')

class Duck(Animal):
    def say(self):
        print('QUACK QUACK')
    
if __name__ == "__main__":
    animals = []
    
    animals.append(Dog())
    animals.append(Cat())
    animals.append(Duck())

    #어떤 동물인지 알 필요 없다.
    #객체에 따라 그에 맞는 메서드가 호출됨
    for animal in animals:
        animal.say()
```
 	
 	

 	