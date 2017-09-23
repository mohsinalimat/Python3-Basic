#2_python3 

---

## Func, File I/O, Error Handle

---

## Func 

 - Func sysntax

```python

# 문법 
def function(parameter):
	실행문1
	실행문2
	... 
	
def awe_sum(a,b):  
	result = a + b
    return result

a = 2
b = 3
print(awe_sum(a,b)) # 5
# def : 함수 선언 명령문, awe_sum : 함수 이름, (a,b) : 인자, 파라미터, return : 반환값


```

 - 함수 특징
 	 - function without input 
 	 - function without return
 	 - function with multiple return
 	 - parameter with initialize(defualt 값 설정가능)
 	 - arguments(여러 가지 인자를 받을수 있다.)
 	 - keyword arguments(여러가지 ketword 인자를 받을수 있다.)


```python

# function without input 

def func() :

	return print("hello world")

# function without return

def func(n):
	print("hello world")

# function with multiple return

def func(x, y):
	return x+y

# parameter with initialize

def func(x = 10, y = 20) :
	return x+y
	
print(func()) # 30

# arguments

def mul_variable(*args):
    mul_sum = 0
    
    for i in args:
        mul_sum += i
        
    return mul_sum

print(mul_variable(1,2,3,4,5,6,7,8,9,10) # 55  

#

def show_kwargs(**kwargs):
    print(str(kwargs))
    
print(show_kwargs(a=10,b=20,c=30,d=40)) # {'a': 10, 'b': 20, 'c': 30, 'd': 40}

 -> dictionary 형식으로 출력됨.
  
	

```

---

##File I/O

 - python IDLE 상에서 file 의 데이터를 control할수 있다.
 

```python

# 기본적으로 open 을 하고 나면, f.close()를 같이 사용하자, f.close()를 하지않으면 지속 적으로 리소스를 갉아 먹는다.

f = open(filename, mode)
f.close()


# Mode 

mode r - 읽기모드 w - 쓰기모드 a - 추가모드(파일의 마지막에 새로운 내용을 추가)

# Create New File and Write text

f = open("Newfile.txt", 'w')
f.close()
 -> 현재 위치의 Newfile.txt 생기고, w 모드로 들어갔다가, 나왔음.
 
 
 
 f = open("Newfile.txt", 'a')
for i in range(1,11):
    text = "line %d. \n" % i
    f.write(text)
f.close()
   -> 추가 모드로 들어가서, 각각 줄에 line (for 구문 횟수) 만큼 텍스트를 적어주고, 종료함
   
   
# Read all taxt

f = open("abcd.txt", 'r')
while True:
    text = f.readline()
    if not text: break
    print(text)
f.close()

 -> 현재 text에 있는 모든 내용들이 출력된다. 
 
   
  
```



---

## Error Handling 

알고있는 오류의 문구를 내가 handlling 할수 있다. 

```python

# sysntax

try:

except:

# 사용

try:
    some_input = int(input("type some number: "))
except ValueError:
    print("I said type some NUMBER!!!!")
    
 -> valueError 는 int 가 출력되어야 하는곳에, 스트링을 넣으면 발생하는 에러인데, 그 에러문구를 수정했음. error 을 발생시키면, I said ty~ 으로 에러메세지가 출력된다.
 
  -> 사용하려면 내가 발생시키는 에러가 정확히 무엇인지 알고 선택해서 사용해야 겠다.




```

