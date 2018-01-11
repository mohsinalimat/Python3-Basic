# 5_Python3

---

## Literator, Generator

---

- Literator, Generator
	- Generator은 litertor의 특징이다. 
	- 순회가 가능한 객체
	- 게으른 연산은 한다
	- 필요할때만 불러서 연산이 가능하다

```python
li = [1,2,3,4].
li1 = iter(li)

next(li1) # 1
next(li1) # 2
next(li1) # 3
next(li1) # 4
next(li1) # litertor error 발생.
``` 