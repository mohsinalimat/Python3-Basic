# 11_Python3

**Reference: <https://github.com/ythwork>**

**[CPU 동작원리 youtube 설명](https://www.youtube.com/watch?v=cNN_tTXABUA&t=569s)**

---

## CPU, Memoey, Cache, Stack Frame, locality, virtual address space, 

---


## CPU

  - clock
  - cpi(clocks per instruction)
    : 한 인스트럭션이 실행되는데 걸리는 클럭
  - register
    - instruction register
      : 현재 실행 중인 인스트럭션
    - program counter
      : 다음에 실행할 인스트럭션이 저장된 
      메모리의 주소값
---

## CPU

  - fetch
  
    - 실행할 인스트럭션을
    - 메모리에서 인스트럭션 레지스터로 이동
    
  - decode
  
    - CU에서 인스트럭션을 해석
  - execution 
  
    - 해석된 인스트럭션을 실행
    
    


**[CPU clock image](/image/cpu.pdf)**


---

## Memory

**[Memory image](/image/memory.pdf)**

**[Stackframe.pdf image](/image/stackframe.pdf)**


---


## cache
  - cache hit
    - 필요한 데이터가 캐시에 있을 때 
  - cache miss
    - 필요한 데이터가 캐시에 없을 때
      - 데이터를 가져올 때 
        : 64 bytes ~ 128 bytes
---

## locality
  - temporal locality
    - 한번 접근한 메모리에 자주 접근
  - spatial locality
    - 접근하는 메모리가 이전에 접근한 메모리의
      근처일 확률이 높다
---

## example code
```python
>>> li = [1, 2, 3, 4, 5]
>>> res = 0
>>> for e in li:
    #temporal locality + spatial locality
	res += e
```
  
---
## virtual address space
  - code
    - 프로그램의 인스트럭션들이 저장되어 있는 공간
  - data
    - 전역 변수(static 지역 변수 포함)가 저장되는 공간
    - 프로그램 실행시 생성 후 프로그램 종료시 소멸 
  - stack
    - 지역 변수가 저장되는 공간
    - 함수 호출 시 스택 프레임 생성
  - heap
    - 할당과 해제를 프로그래머가 결정

    

**[Virtual Memory.PDF](virtual_memory.pdf)**

---
## example code
```C
//DATA
int global_x = 10;

int main(void){

	//STACK
	int stack_x = 20;
    
        //HEAP
        //원하는 시점에 할당 
	int * ptr = (int*)malloc(sizeof(int));
	*ptr = 30;
        //원하는 시점에 해제
	free(ptr);

	return 0;
}
```

