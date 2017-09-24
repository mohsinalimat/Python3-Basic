# 13_Python3

---

## interpreter, compile


---

## compiler
  - lexer
    - characters -> lexer -> tokens
  - parser
    - tokens -> parser -> parse tree(implicit)

---
## python compiler 
  - source code -> parse tree
  - parse tree ->AST(Abstract syntax tree)
  - build a symbol table
  - AST -> bytecode

---
## token 

```python
#token
>>> import token
>>> token.tok_name
```
---
## example code

```python
#test.py
def func(a, b):
    return a + b

a = 10
b = 20

c = func(a, b)
print(c)
```
---
## tokenize 

```python
#tokenize
>>> from tokenize import tokenize
>>> from io import BytesIO
>>> s = open('test.py').read()
>>> g = tokenize(BytesIO(s.encode('utf-8')).readline)
>>> for token in g:
	print(token)
```
---
## ast 

```python
#ast
>>> import ast
#node 생성
>>> node = ast.parse(s, 'test.py', 'exec')
# yield all descendant nodes
>>> g = ast.walk(node)
#a formatted dump - show the names and the values for fields
>>> ast.dump(node)
```
---
## symtable

```python
#symtable
>>> import symtable
>>> sym = symtable.symtable(s, 'test.py', 'exec')
>>> sym.get_name()
'top'#global table
>>> sym.get_symbols()
[<symbol 'func'>, <symbol 'a'>, <symbol 'b'>, <symbol 'c'>, <symbol 'print'>]

>>> func_sym = sym.get_children()[0]
>>> func_sym.get_symbols()
[<symbol 'a'>, <symbol 'b'>]
```
---
## bytecode

```python
#bytecode
>>> import dis
>>> g = dis.get_instructions(s)
>>> for inst in g:
	print(inst.opname.ljust(20), end = ' ')
	print(inst.argval)
```
---
## PVM
  - stack machine
  - a big loop 

---
## PVM

```python
#dis
>>> dis.dis(s)
```

---
## dis exam

```python
>>> code = compile(s, 'test.py', 'exec')

#in dis.dis(s)
4         8 LOAD_CONST    2 (10)
#4 : line number
#8 : offset from co_code
#2 : co_consts[2]
         10 STORE_NAME    1 (a)

>>> code.co_consts
>>> code.co_names
```


**[interpreter, compile PDF ](/study/interpreter.pdf)**

---

> interpreter, compile 의 차이는, compile 는 user이 프로그램을 사용중일때는, 이미 모든 소스코드들이 compile 된 이후의 상태에서 사용하는것이고, interpreter은 user 이, 프로그램을 사용하면서, 명령어 한줄 한줄 compile 하는 상태라고 할수 있다, 각각의 장단점을 생각하면서 그 차이를 알고 있으면 될 것같다.

> compile 의 장점은, 프로그램을 사용하기전 모든 컴파일이 완료된 상태라서, 알수없는 오류가 발생될 확률이 상대적으로(?) 적다. 그리고 빠르다.

> interpreter 은 사용자가 사용하면서, 한줄한줄 명령어를 입력할때마다 compile 하기 때문에 생각치 못한 오류가 발생할 확률이 compile 언어보다 높다. 하지만, 프로그램을 사용시 Source Code 가 모두 compile 가 된상태가 아니기 때문에, 가볍다. 
> 
> 나머지 더 필요한 내용은 보충 하자.






