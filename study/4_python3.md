# 4_Python3

---

## First Function, Closure, Decorator

---

## First Function 

 - First Function 의 조건

 	- 함수를 인자로 전달이 가능 한가?
 	- 함수를 반환 하는가?
 	- 함수를 변수에 저장이 가능 한가?

```python

# 함수를 인자로 전달이 가능 한가? 

def f(a,b):
    return a+b

pass_func = f

#함수를 변수에 저장이 가능한가? 

f(10,20) # 30


# 함수를 반환 하는가?

def f(a,b):
    return a+b
    

def g(funt, a, b):
    
    return funt(a,b)


g(f,20,30) # 50

 -> f 함수가 g 함수의 인자로 들어가서, 함수 자체로 반환이 되었다.
 

```

> 위의 3가지 조건을 만족하는 함수라면, 그것을 First Function(1급 함수) 이라고 한다.


---

## Closure

 - Closure 

함수내 함수를 반환 받아서 사용한다.

FirstFunction 을 만족 한다.

free variable : 서로 다른 정보를 가진다(함수인데, 내부정보를 가지고 있다. 엄밀하게 얘기하면 객체 내부에 있는 객체가 data 를 가지고 있다고 생각 할수 있다.)

```python


# account 함수를 객체로 생성하면, return 으로 other_name 함수를 호출한다. 그래서 사실상 account함수에 name이라는 값을 받아 놓고, other_name 함수의 호출을 기다리는 '상태' 라고 생각할수 있다. 
def account(name):
    
    def other_name(n):
        
        return name + " " + n
    
    return other_name
    
    
# 같은 함수에 나온 객체 지만, 서로다른 내부 정보를 가지고 있다(free variable)
    
me = account("min")
you = account('jun')

# other_name 함수를 호출할때 서로 다른 값을 호출해서, 서로 다른 결과가 return 된다.

me("안녕하세요") # ' min 안녕하세요 '
you("hello world") ' jun hello world '


# 두 함수(me, you) 는 서로 다른 함수이다, 하지만 code object는 같다.(root function 이 같다는 이야기)

me == you # False
me.__code__ == you.__code__ # True


# 지역 변수를 확인해보면

me.__code__.co_varnames # n


# free variable 확인해보면 -> 서로다른 free variable 을 가진다.

me.__code__.co_freevars # name 



```

---

## Decorator


함수에 기존 함수의 기능을 추가하고 싶을 때 

---

## decorator 

```python
#overwrite되어 마지막에 정의된 func만 유효
def func(a, b):
    return a + b

def func(a, b):
    return a * b
```

---

## decorator

```python
#decorator
def outer(org_func):
    def inner(*args, **kwargs):
        print("Things")
        return org_func(*args, **kwargs)
    return inner

```

---

## decorator

```python
def func(a, b):
    return a + b

print(func.__name__)#func
func = outer(func)
print(func.__name__)#inner
```

---

## decorator 

```python
func = outer(func)

@outer
def func(a, b):
    return a + b
```

---

## decorator  


```python
#function call counter
def call_counter(org_func):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('function call : {}'.format(cnt))
        return org_func(*args, **kwargs)
    return inner
```

---

## decorator 


```python
@call_counter
def func(a, b):
    return a + b

for i in range(1, 10):
    a = i + 1
    b = i + 2
    result = func(a, b)
    print('{} + {} = {}'.format(a, b, result))
```

---

## decorator 


```python
#timer
import time
def timer(org_func):
    @wraps(org_func)
    def inner(*args, **kwargs):
        start = time.time()
        result = org_func(*args, **kwargs)
        elapsed = time.time() - start
        print("elapsed time : {}".format(round(elapsed, 1)))
        return result
    return inner
```
---

## decorator 


```python
@timer
def func(a, b):
    #pause
    time.sleep(5)
    return a + b

func(1, 2)
```
---

## decorator 


```python
from functools import wraps
```


```python
def outer(org_func):
    @wraps(org_func)
    def inner(*args, **kwargs):
        print("Things")
        return org_func(*args, **kwargs)
    return inner
```



 		