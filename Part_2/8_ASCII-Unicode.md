# 8_Python


**Reference: <https://github.com/ythwork>**

---


## ASCII, unicode

---

> ASCII 코드 -> Unicode 가 됨 **Unicode 속에 ASCII 코드 포함되어 있다** 

> Big-endian: 큰 단위 부터 저장이 되는 형식 fa8765.... 맨처음에 motorora 사에서 사용했다고함.
 
> Little-endian: 작은 단위 부터 저장이 되는 형식 0123... intel 사는 Little-endian 방식을 사용하고 있다고함.. 

두개의 저장 방식중 무엇이 좋다 나쁘다는 없지만, 서로다른 저장방식을 가지고 있는 컴퓨터 끼리 통신시 문제가 생김.


---
## from characters to code
 - from 'a' to 97(ASCII)
---

## encoding model
 - ASCII : 7 bit (2의 7승 : 128 가지 문자)
   - 로마자 및 특수 기호(한글 포함 안됨)
 - unicode
   - 2 byte (2의 16승 : 65,536가지 문자)
   - 한글 및 많은 언어 포함
   - 모든 인코딩 방법을 대체하려고 함

---

## unicode exam
 - 'A' - U+0041 (ASCII 호환)
 - '가' - U+AC00
---

## unicode exam
```python
>>> '\u0041'
'A'
>>> '\uAC00'
'가'
```
---

## 한글의 범위
  - U+AC00 ~ U+D7AF
```python
>>> '\uAC00'
'가'
>>> '\uB098'
'나'
>>> '\uB2E4'
'다'
```
---

## 초성
ㄱ/0 ㄲ/1 ㄴ/2 ㄷ/3 ㄸ/4 ㄹ/5 ㅁ/6 ㅂ/7 ㅃ/8 ㅅ/9 ㅆ/10
ㅇ/11 ㅈ/12 ㅉ/13 ㅊ/14 ㅋ/15 ㅌ/16 ㅍ/17 ㅎ/18

---

## 중성
ㅏ/0 ㅐ/1 ㅑ/2 ㅐ/3 ㅓ/4 ㅔ/5 ㅕ/6 ㅖ/7 ㅗ/8 ㅘ/9 ㅙ/10
ㅚ/11 ㅛ/12 ㅜ/13 ㅝ/14 ㅞ/15 ㅟ/16 ㅠ/17 ㅡ/18 ㅢ/19 ㅣ/20

---

## 종성
없음/0 ㄱ/1 ㄲ/2 ㄳ/3 ㄴ/4 ㄵ/5 ㄶ/6 ㄷ/7 ㄹ/8 ㄺ/9 ㄻ/10
ㄼ/11 ㄽ/12 ㄾ/13 ㄿ/14 ㅀ/15 ㅁ/16 ㅂ/17 ㅄ/18 ㅅ/19 ㅆ/20
ㅇ/21 ㅈ/22 ㅊ/23 ㅋ/24 ㅌ/25 ㅍ/26 ㅎ/27

---

## 공식에 의해 한글 유니코드 계산하기
  - 0xAC00 + (초성순서 * 21) + 중성순서) *28 + 종성순서
```python
def make_hangul_unicode(cho, jung, jong):
	unicode = 0xAC00 + ((cho * 21) + jung) * 28 + jong
    	return chr(unicode)
        
# 양
# ㅇ : 11 (초성), ㅑ : 2 (중성), ㅇ : 21(종성)
print(make_hangul_unicode(11, 2, 21))
```python
---
## 유니코드의 부호화 방식
 - UTF-8 
   - 8bit 기반
   - 가변 길이 유니코드 인코딩 시스템 
---
## 유니코드의 부호화 방식
 - UTF-16 
   - BMP(Basic multilingual plane)
       : 다국어 기본 평면
       : 16 bit
   - SMP(Supplementary Multilingual plane) 이상 
       : 다국어 보충 평면~
       : 32 bit
---
## 유니코드의 부호화 방식
 - UTF-32
   - 32 bit
---

## 유니코드의 부호화 방식
 - CP949
   - code page 949
   - 통합형 한글 코드( Unified Hangul Code)
   - 현대의 모든 한글 수용
---

## UTF-8 이란?
 - 1 byte ~ 4 byte 
 - U+0000 ~ U+007F(ASCII)
   - 1 byte로 나타낸다
 - 한글 
   - 3byte로 나타낸다
---

## in python
 - 부호화 방식이 UTF-8
```python
>>> coded = "abcde".encode()
>>> coded
b'abcde'
```
---

## in python
 - 부호화 방식이 UTF-8
```python
>>> coded_string = "abcde".encode()
>>> for ch in coded_string:
		print(ch)
97
98
99
100
101
```
---
## in python
 - 부호화 방식이 UTF-8
```python
>>> coded_string = "파이썬".encode()
>>> coded_string
b'\xed\x8c\x8c\xec\x9d\xb4\xec\x8d\xac' # 한 글자당 3byte
```
---

## '가'의 encoding 과정
 - UTF-8 구조 
   - 0800 - FFFF 
     ==> 1110XXXX 10XXXXXX 10XXXXXX
   - '가'의 유니코드 
     ==> U+AC00
     ==> 1010 1100 0000 0000
     ==> 1010 110000 000000
   - 11101010 10110000 10000000
   - 0xEAB080
   - 즉, 3 바이트로 인코딩
---

---

## '가'의 encoding 과정
  - 0xEAB080
 ```python
 >>> '가'.encode('UTF-8')
 b'\xea\xb0\x80'
 # EA B0 80
 ```
---


## in python
 - 부호화 방식이 UTF-8
```python
>>> string = coded_string.decode()
>>> string
"파이썬"
``