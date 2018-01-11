# 3_Python3

---

## Lambda, Map, Filter, Reduce, Layz Evaluation

---

## Lambda

  - 익명함수
  - 자주사용하지 않을때 편리하다(한번 사용되고 소멸됨)
  - return 이 없다
  - lambda를 변수로 받아서 사용이 가능하다.
  - Lazy evaluation(게으른 연산이 가능하다)
  - body는 오직 expression<식>만 올 수 있다.
  
> 식 : a+b
> 
> 문 : a+b = c 
     
     	 
  
```python
def adder(a,b):
	return a+b
	
# lambda로 변환
f = lambda(a:b, a+b) 
  -> 변수로 a,b를 받고 결과로 a+b를 한다는 의미이다. 
  -> 위의 함수를 간단하게 축약해서 사용할수 있음.
f(5,10) # 10
```

---

## Map 

- Map 
 
 map 은 함수라고 생각하자, map 이라는 함수와, x(정의역) 을 설정해서, y값을 반환 받을수 있는 역활을 할수 있는게 'map' 이다.
 
 
```python
li = [1,2,3,4]
def func(x):
    return x*2
map_func = map(func,li) // map_func 에 결과들이 객체로 만들어져서, 바로 결과 값이 출력되지않고, 들어있는 값들을 for 구문을 통해서 꺼내준다

for i in map_func:
    print(i)
    # 2,4,6,8 출력.
    
# lambda로 변환 가능    
map_lambda = map(lambda x:x*2, li)  
for i in map_lambda :
    print(i)  
    #2,4,6,8 출력
```

---

## Filter 

- Filter

조건이 참인것을 골라내어 준다. 

객체로 만들어 졌을때는 iterator 이다.

```python
li = [1,2,3,4]
iterator_filter = filter(lambda x: x>2, li)
for i in iterator_filter:
    print(i)    
    # 3,4 
filter 로 정의 되었을때, 데이터들 자체가 객체 않에 들어가 있음. OOP 적으로 생각해서 값을 꺼내주어야 한다.
```

---


## Reduce 

- Reduce

reduce(function, sequence[, initial]) -> value

함수는 두 개의 인자를 받음 sequence 자료형에서 두 개씩 가져온 후 연산해 한 개의 값으로 치환


```python 
from functools import reduce
li = [i for i in range(1,11)]
f_reduce = reduce(lambda x,y: x+y, li)
print(f_reduce) # 55
reduce 함수가, iterator 객체가 되어서, lambda의 역활은 두개의 인자만 더해주는것인데, 
lambda 함수가 x+y 의 인자를 더하고, 1+2 -> 3+3 -> 6+4 .. 쭈루룩 더해나갔다. 그리고 결과를 반환함.
```

--- 

## layz evaluation

 - layz evaluation(게으른 연산)

게으른 연산으로 정의하면, code 전체가 맨처음에 메모리에 할당 되는것이 아니라, 사용될때 한번 load 되고, 사용후 메모리에서 해제 된다. 어떻게 사용하느냐에 따라서 전체적인 성능을 높일수 있다.