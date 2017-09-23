import openpyxl
import math
from functools import reduce


raw_data = {}
wb = openpyxl.load_workbook('class_1.xlsx')
ws = wb.active
g = ws.rows


for name, score in g:
    raw_data[name.value] = score.value

scores = list(raw_data.values())

#평균
avrg = reduce(lambda a,b :a + b, scores)/len(scores)

#분산
variance = round(reduce(lambda a,b : a+b , map(lambda s: (s-avrg)**2, scores))/len(scores),1)

# 표준편차 
std_dev = round(math.sqrt(variance), 1)

print("평균 :{}, 분산 : {}, 표준편차 : {}".format(avrg, variance, std_dev),'\n')

if avrg < 50 and std_dev > 20:
    print("성적이 너무 저조하고 학생들의 실력차이가 너무 크다.")
elif avrg > 50 and std_dev > 20:
    print("성적은 평균 이상이지만 학생들 실력 차이가 크다. 주의 요망!")
elif avrg < 50 and std_dev <20:
    print("학생들간 실력차이는 나지 않으나 성적이 너무 저조하다. 주의 요망!")
elif avrg > 50 and std_dev<20:
    print("성적도 평균 이상이고 학새읃ㄹ의 실력차도 크지 않다.")
    

