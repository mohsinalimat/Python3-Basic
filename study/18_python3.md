# 18_python

---

## bubbleSort, QuickSort, BigO, recursion ,Stack, Queue

---

## bubbleSort 

### Reference

[bubbleSort PDF 자료](/image/bubble_sort.pdf)

 - bubleSort
 
	1. 방울 처럼 팡팡팡팡 터지면서 구현된다고 해서 bubbleSort 이다. 원리는 정렬하려는 자료의 개수^2 배만큼 정렬을 시도한다. 

	2. [1,2,3,4,5] 리스트가 있을때, 1>2 -> 2>3 .... 한번 1>2 -> 2>3... 을 5번 비교해서. 원하는 정렬 형태로 만들어줌.

```python

def bubble_sort(data):
    data_len = len(data)

    for i in range(data_len - 1):#1
        for j in range(data_len - i - 1):#2
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

if __name__ == "__main__":
    li = [2, 3, 5, 2, 3, 8, 6, 7, 10, 8, 1, 4]
    bubble_sort(li)
    print(li)




```

---

## Quick Sort



### Reference

[QuickSort PDF 자료](/image/quick_sort.pdf)

 - QuickSort

	1. pivot 과 left, right 를 정해서, 데이터를 1/2 씩 줄여 나가면서 [5,4,3,2,1] 의 리스트를 정렬 해나감 Divide and conquer(분할정복 기법) 이라고도 부르는데, 데이터를 쪼개서 처리 한다고 붙여진 이름인것 같다.

	2. bigO 의 연산결과가 정확하게 마음에 와닿지는 않지만, bubbleSort 보다 적은 횟수의 시도를 통해서 원하는 정렬 값으로 만들어 준다는것은 알겠다.

	3. 하지만 최악의 경우(이미 정렬이 다되어있는경우) 에는 bubbleSort 와 같은 성능이라고 한다. 생각해보면, 정렬하려고 하는데이터를 반으로 나누어서 정렬해주어도, 어차피 정렬이 되어 있어서 한개의 값만 처리 되었다고 생각하니까, bubbleSort 와 같은 성능이라고 할수 있다. 

	
```python

def bubble_sort(data):
    data_len = len(data)

    for i in range(data_len - 1):#1
        for j in range(data_len - i - 1):#2
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

if __name__ == "__main__":
    li = [2, 3, 5, 2, 3, 8, 6, 7, 10, 8, 1, 4]
    bubble_sort(li)
    print(li)



```

---


## BigO 개념

### Reference

[QuickSort PDF 자료](/image/binary_search.pdf)

[나무 위키 점근 표기법](https://namu.wiki/w/%EC%A0%90%EA%B7%BC%20%ED%91%9C%EA%B8%B0%EB%B2%95)


**bigO 는 성능 평가!**

---

## recursion

 - recursion : 설계시, 꼭 탈출 조건을 주어야함. 그렇지 않으면, 무한 루프돌게됨!
 
 - 대표적인 Recursion 문제인 피보나치 수열

```python

def fibonacci(n):
    if n == 0 or n == 1:
        return 1

    return fibonacci(n-2) + fibonacci(n-1)

if __name__ == "__main__":
    n = 10
    for i in range(n):
        print(fibonacci(i), end = '  ')
        
** 계승

def factorial(n):
    #탈출 조건
    if n <= 1:
        return 1
    
    return n * factorial(n-1)

if __name__ == "__main__":
    n = 3
    res = factorial(n)
    print("The factorial of {} is {}".format(n, res))



```

 - hanoi tower

	1. 설계 전략, 어떻게 되든 링을 놓고, 그 링을 처음에는 2번째에 모두 옮기고, 그다음에는 모두 3번째에 옮긴다... 
	2. 사실 아직 이해 못했다......ㅠ.ㅠ

```python


def hanoi(num, _from, _by, _to):
    #탈출 조건
    if num == 1:
        print("{}에서 {}로 {} 번째 원반 이동".format(_from, _to, num))
        return

    hanoi(num-1, _from, _to, _by)
    print("{}에서 {}로 {} 번째 원반 이동".format(
        _from, _to, num))
    hanoi(num-1, _by, _from, _to)

if __name__ == "__main__":
    while 1:
        numOfTray = int(input("원반의 개수를 입력하세요!(종료 : 0) :"))
        if numOfTray == 0:
            break
        hanoi(numOfTray, 'A', 'B', 'C')

    

  

```


---

## Stack, Queue

### Reference

[후위 표기법 계산기 PDF 자료](/image/calculator.pdf)

[Stack, Queue 작동방식 PDF 자료](/image/stack_queue.pdf)





