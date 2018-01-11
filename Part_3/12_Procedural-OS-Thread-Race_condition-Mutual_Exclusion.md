# 12_Python3

---

## procedural programming, OS, process scheduling, scheduler, Thread, Race condition, mutual exclusion

---

## procedure
 - routine, subroutine, function

---
## hardware support
  - stack pointer in CPU
    - ESP(Extended Stack Pointer) in intel architecture

---
## modularity
 - argument, return value
 - scoping
   - indentation in python

---
## why procedural?
  - 코드 이해, 유지 보수
  - '이 프로그램은 무엇을 하는가?'
  
---

## pre-emptive OS
  - multitasking OS
  - suspend currently running process
  - determine which process should execute next
---

## process scheduling
  - priority algorithm
    : the higher priority, the earlier running
  - round-robin algorithm
    - if same priority
      - time slice
---
## scheduler
  - when?
    - every time slice
    - a process created or a process ended
    - a running process blocked


---

**[program, process, Thread 자료](/image/OS.pdf)**


---

## Thread, Race condition, mutual exclusion

- Race condition : 공유 자원을 가지고, CPU 가 서로 사용하기 위해 CPU 권한을 뺴앗는것, 수행해야 하는 연산을 하기전에, CPU 권한이 넘어가 버려서, 해야할 수행을 하지 못하게 되는 현상이 발생함... 그것에 대한 대안으로 mutual exclusion 발상을 하게 됨.

- mutual exclusion : Race condition의 대안으로 cpu가 수행해야 하는일을 다하기전까지 권한을 넘길수 없게, 일종의 방화벽같은것을 걸어두는것임. 이렇게되면, race condition은 발생하지 않지만, CPU가 연산을 안전하게 끝내고 공유 자원에 접근해야하는데, '공유자원' 의 접근을 막음.. 막는 시간만큼 병목 현상 발생. 결국에는 완벽하게 대응이 불가능.

> thread 이론으로 들었을때는 이것만큼 완벽한것이 없다고 생각했는데, 사실 어느 일정 수준의 thread 를 넘어가면, 사실 core가 한개 있는것만 못하는 속도가 나옴..



```python
# multi thread
import threading
def thread_main(li, n):
    for i in range(offset * n + 1, offset *(n + 1) + 1):
        li[i] *= 2
n = 1000
offset = n // 4
li = [i for i in range(n+1)]
threads = []
for i in range(4):
    th = threading.Thread(target = thread_main,
                          args = (li, i))
    threads.append(th)

for th in threads:
    th.start()
for th in threads:
    th.join()
print(li)

# race condition
import threading
g_count = 0
def thread_main():
    global g_count
    for i in range(100000):
        g_count += 1
threads = []

for i in range(50):
    th = threading.Thread(target = thread_main)
    threads.append(th)

for th in threads:
    th.start()

for th in threads:
    th.join()

print('g_count : {:,}'.format(g_count)) # 연산 결과가 다르게 나옴.

# mutual exclusion 
import threading
g_count = 0
def thread_main():
    global g_count
    lock.acquire()
    for i in range(100000):
        g_count += 1
    lock.release()
lock = threading.Lock()
threads = []
for i in range(50):
    th = threading.Thread(target = thread_main)
    threads.append(th)
for th in threads:
    th.start()
for th in threads:
    th.join()
print('g_count : {:,}'.format(g_count)) # race condition 때와 시간을 비교해보면 차이가 있음..
```

