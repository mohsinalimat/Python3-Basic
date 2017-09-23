# 6_Python3.md 

---

## Call By Value, Call By Reference 

 - 참조 순서 
 

	1. [stack frame 자료](/image/stackframe.pdf)

	2. [memory 자료](/image/memory.pdf)

	3. [Call By Value, Call By Reference PDF](/image/call_by_what.pdf)


 - Call by value, Call by Reference 

> Call by value 와 Call by reference 의 가장큰 차이점은, 변수를 사용할때, 이미 변수는 객체로서, 어떤 값을 참조 하고있다. 이때, 객체인 '변수' 가 참조하는 값과, 그 객체인 '변수'가 참조하고 있는 '값' 들 '그 자체' 에서 차이가 있는데, 백문이 불여 일견, 코드로 한번 보자, 



```python

# call by value 

list = [1,2,3,4]

def change_value(li):
	 li = [10,20,30,40]
	 
	 return li

change_value(list) # [10,20,30,40]

 -> 함수 내부에서는 메모리에 새로운 stack frame 에 새롭게 li 를 할당 했음. 그래서 list 의 값을 받아서 사용했지만, 실제로 stack frame 가 끝나고 나서는 list의 값 자체가 변하지는 않앗다.
 
print(list) # [1,2,3,4] 

# call by reference

list = [1,2,3,4]
def call_by_reference(li, idx, value):
	li[idx] = value
	
	return li
	
print(call_by_reference(list, 0, "call by reference")) # ['call by reference', 2, 3, 4]


print(list) # ['call by reference', 2, 3, 4]

 -> 함수 호출이 시작되고 stack frame 쌓일때, 다른 stack frame 에서 다른 stack frame 에 있는 list에 접근해서 list 값 자체를 reference(참조) 해서 값 자체를 변경 했다.
	 
 

```


> 여기서 주의! 해야할점은 call by value 와 call by reference 할때, 그 대상이 **mutable**, **immutable** 이라서 **mutable** 일때는 call by reference 이고, **immutable** 일때는 call by value 가 아니다. 엄밀하게 짚고 넘어가자.
 

 
