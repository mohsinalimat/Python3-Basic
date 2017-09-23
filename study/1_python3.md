# 1_Python3 

---
## Variable, Data Type(List, tuple)

---

## Variable 선언 

```python


a = 10 
b = "20"
c = ["a"] 


```
python 은 동적인 언어라서, 자료형의 타입을 미리 선언하지 않고 자료형을 선언 할수 있다. 

---

## Data Type

 - Data Type 종류 
 	- Int, Double, float(숫자형)
 	- String(문자형)
 	- [ ] List (리스트)
 	- Tuple () 
 	- Dictionary {a:b} (딕셔너리)
 	- Set (집합)

 	
---

## Int, Double, float(숫자형)

 - 숫자형 정의 

 ```python
 
 파이썬에서는 정수형 1,2,3, 실수형 1.1, 2.5.. 등을 따로 선언하지 않고, 변수에 숫자 그대로 표현해서 정의해주면 그 type 로 자동으로 변환 된다. 
 
 그 외의 2진수, 8진수, 16진수 등등은 다음에 알아보기로 하자.

 ... 등등으로 정의 할수 있다.
 
 
 ```
 
 - 숫자 연산을 위한 연산자들

 	- 거듭제곱(**) 연산자 
 	- 대상을 나누고 난 나머지를 표현하는(%) 연산자 
 	- 정수형 나눗셈을 하는(//) 연산자

 	


---

## String(문자열)

- 문자열 선언하기 

파이썬에서는 문자열을 어떻게 선언하고 사용할까?

```python
# 문자 선언하기

string = 'a'
string1 = "b"
string2 = ''' c '''
string3 = """ d """

# 여러 줄의 스트링 선언도 가능하다.
string4 = """abcd
efg
fijk"""

```

 - 문자열 연산하기 

 ```python
 
 string = "abc"
 string1 = "def"
 
 print(string + string1) # "abcdef"
 print(string*3) # "abcabcabc"
 ```
 
 - 문자열 indexing 

```python

string = "hello world"
print(string[2]) # "l"
print(string[0]) # "h"


문자열 인덱싱은 python의 언어의 특징중 하나인데, 익숙해지면 사용하기 굉장히 편리하다.
```

- 문자열 type formating 




---

## List, Tuple 차이점

- List []

> 리스트는 값을 추가, 수정이 가능합니다, Tuple는 값을 수정, 삭제 할수 없습니다. 

```python

# List 선언 
list = []

# list 에 값추가.

# list에 요소를 추가할수 있습니다.

list.append("a")
print(list) # ["a"]

#특정 위치에 요소를  넣을수도 있고,
list.insert(0,"abc") 

# 삭제도 가능합니다
list.remove("abc")
print(list) # []

정렬, 특정값 빼오기 등 여러가지 함수의 기능을 사용할수도 있습니다.



```

 - Tuple () 

```python

# tuple 선언 
tuple = (1, 2, 3, 4)

# tuple 삭제 시도
del tuple[0] #에러 

# tuple 끼리 더하거나, 반복 하는 연산이 가능합니다

tuple = (1,2,3)
tuple1 = (4,5,6)

print(tuple + tuple1, tuple*3) # (1,2,3,4,5,6), (1,2,3,1,2,3,1,2,3)


```

---

## Dictionary

- dictinoary 선언


```python

dic = {}

# dictionary 은 key 와 value 로 구성되어 있다.

dic = {"korea":100, "math": 50}

# 요소 삭제가 가능하다.

del dic["korea"]
print(dic) # {"math":50}

dictionary 를 응용해서, key 값과 value 값을 이용해서 data control 할수 있습니다.


```

---

# Set

 - Set 특징
 	 - 중복이 없다
 	 - 순서가 없다
 	 - 수학의 집한 연산을 쉽게 하기 위해서 만들어진 자료형이다.(잘 사용되지 않음)

 	 
```python

# Set 선언
ppap = {'pen', 'apple', 'pineapple', 'pen'}

# Set 응용

A ∪ B	== A | B A ∩ B	== A & B A - B	== A - B A Δ B == A ^ B 기호들을 사용해서, 수학의 집합 연산을 이용할수 있다.


```





