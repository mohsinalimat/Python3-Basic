# 15_Python3

---

## linearSearch, binarySearch, Big O

---
 
## linearSearch

> linearSearch 는 O(n) 인 성능을 가지고있다, 풀어서 이야기 하면, 내가 찾고자 하는 데이터 개수에서, 내가 찾으려고 하는 데이터가 떨어져 있는 만큼 순회해서 값을 찾아낸다. 


```python
예를 들어서 데이터가 [1,2,3,4,5,6] 인데, 찾고 싶은 데이터가 5라면, 1>2>3>4>'5' 찾는다고 이해하자.

def linear_search(data, target):
    for idx in range(len(data)):
        if data[idx] == target:
            return idx
    return None

if __name__ == "__main__":
    data = [i for i in range(10)]
    target = 4
    idx = linear_search(data, target)
    if idx == None:
        print("{}이 존재하지 않습니다".format(target))
    else:
        print("찾는 데이터의 인덱스는 {}이고 데이터는 {} 입니다".format(idx, data[idx]))
```

---

## binarySearch

[bianrySearch big O, 알고리즘 PDF](/image/binary_search.pdf)

> binarySearch 의 성능은 linearSearch 보다 좋다, binartSearch 의 O(log n) 이다. 이유는, 찾고하자 하는데이터를 반씩 나누어서 결과값을 찾는다. [1,2,3,4,5,6] 찾는 데이터가 2 라면 [1,2,3,4,5,6] 의 데이터중 중간의 값을 찾아서, 중간보다 크거나, 작은 값은 날려서 원하는 값을 찾아 나간다. [1,2,3,4,5,6] -> [1,2,3] -> [1,2] -> '2' 를 찾아서 반환한다



```python
def binary_search(data, target):
    data.sort()
    start = 0
    end = len(data) - 1
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

if __name__ == "__main__":
    data = [i**2 for i in range(1, 11)]
    target = 1000
    idx = binary_search(data, target)
    if idx == None:
        print("{}이 존재하지 않습니다".format(target))
    else:
        print("찾는 데이터의 인덱스는 {}이고 데이터는 {} 입니다".format(idx, data[idx]))
```
