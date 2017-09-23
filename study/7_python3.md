# 7_Python3

**Reference: <https://github.com/ythwork>**

 [floating point number 자료(Reference: https://github.com/ythwork)](/image/numbers.pdf)

---



## numbers, 2의 보수, 부동 소수점(floating point number), 2, 10, 16 진수 변환



---
## number
  - decimal(10진수)
    - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
  - binary(2진수)
    - 0, 1
  - hexdecimal(16진수)
    - 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, e, d, f
---
## from decimal to binary
```python
>>> bin(25)
'0b11001'
```
---
## numbers
```python
>>> a = 0b11001
>>> a
25
>>> b = 0x19
>>> b
25
```
---

## memory address - why hex?
```python
>>> address = 0b11111111111111111111111111111111
>>> hex(address)
'0xffffffff'
```
---
## negative number
```python
#int.to_bytes(length, byteorder, signed = False) -> bytes
#양수 25
>>> >>> (25).to_bytes(1, byteorder = 'little', signed = True)
b'\x19'
#양수 25 in memory --> 0001 1001
```
---
## negative number
```python
#양수 25가 0001 1001 ==> 0x19
#음수 25는 1001 1001 ==> 0x99??
>>> (-25).to_bytes(1, byteorder = 'little', signed = True)
b'\xe7'
#0xe7 ==> 1110 0111
```
---
## negative number
  - two's complement
    - one's complement
    - +1
---
## negative number
  - one's complement without sign
    - 110 0111 -> 001 1000
  - +1
    - 001 1001
  - 001 1001 : 25
  - with sign : -25
---
## what is byteorder
  - little endian
```python
>>> little = 0x01020304
>>> little.to_bytes(4, byteorder = 'little', signed = True)
b'\x04\x03\x02\x01'
```
---
## what is byteorder
  - big endian
```python
>>> big = 0x01020304
>>> big.to_bytes(4, byteorder = 'big', signed = True)
b'\x01\x02\x03\x04'
```
---
## floating point number
```python
>>> a = 0.01
>>> result = 0.0
>>> for i in range(100):
	result += a

	
>>> result
1.0000000000000007
```
---
## floating point number
```python
# 0.015625 = 2^(-6)
>>> a = 0.015625
>>> result = 0.0
>>> for i in range(100):
	result += a

	
>>> result
1.5625
```
---
## floating point in python
```python
>>> import sys
>>> sys.float_info
sys.float_info(
#maximum representable finite float
max=1.7976931348623157e+308, 
max_exp=1024, 
max_10_exp=308, 
#minimum positive normalizer float
min=2.2250738585072014e-308, 
min_exp=-1021, 
min_10_exp=-307, 
#digits : 15자리 십진수
dig=15, 
# mantissa digits(52 + 1)
mant_dig=53, 
epsilon=2.220446049250313e-16, 
#radix or base : the number of unique digits
radix=2,
rounds=1)
```
---
## floating point number
  - float - 32 bit
    - sign : 1 bit
    - exponent : 8 bit
      - bias : 2^(8-1)-1 = 127
    - mantissa : 23 bit
  - double - 64 bit
    - sign : 1 bit
    - exponent : 11 bit
      - bias : 2^(11-1)-1 = 1023
    - mantissa : 52 bit
---
## floating point number
  - 2^10 is approximately 10^3
  - 0b1111 == 15 > 9 ---------------------------- 4
  - 0b111 1111 == 127 > 9 -----------------------7
  - 0b11 1111 1111 == 1023 > 999--------------10
  - 0b11 1111 1111 1111 == 16383 > 9999 ----14
---
## float : precision
  - mantissa digits : 24 bit 
  - 0b1111  1111  1111  1111  1111  1111
    == 16,777,215 > 9,999,999
    - 정밀도 : 7자리 십진수 
---
## double : precision
  - mantissa digits : 53 bit
  - 0b1 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111 1111
  == 9,007,199,254,740,991 > 999,999,999,999,999
    - 정밀도 : 15자리 십진수
---

## float 
  - 1.00000000000000000000000 * 2^24
    == 16,777,216
  - 1.00000000000000000000001 * 2^24
    == 16,777,218
  - 16,777,217은???
    - 16,777,216과 같이 표현된다.
---
## float
  - 1.00000000000000000000000 * 2^20
    == 1,048,576
  - 1.00000000000000000000001 * 2^20
    == 1 * 2^20 + 1 * 2^(20-23)
    == 1,048,576.125
  - 두 수의 차이
  - 1,048,576.125 - 1,048,576 == 0.125 == 2^(-3)
 ---
 
## float
 - between two representable floats
   - 2^(e-23)
   - 23 : mantissa bit
---
