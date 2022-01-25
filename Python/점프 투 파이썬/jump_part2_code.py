# 2장 연습문제

# Q1. 홍길동 씨의 과목별 점수는 다음과 같다. 홍길동 씨의 평균 점수를 구해 보자.

a = {'국어': 80, '영어': 75, '수학': 55}
result = 0
for it in a.values():
    result += it

print('평균 : {}'.format(result / len(a.values())))

# Q2. 자연수 13이 홀수인지 짝수인지 판별할 수 있는 방법에 대해 말해 보자.
if 13 % 2 == 0:
    print('짝수')
else:
    print('홀수')

# Q3. 홍길동 씨의 주민등록번호는 881120-1068234이다. 홍길동 씨의 주민등록번호를 연월일(YYYYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해 보자.
pin = '8801120-1068234'
print(pin)
idx = pin.index('-')
yyyymmdd = pin[:idx]
print(yyyymmdd)
etc = pin[idx+1:]
print(etc)

# Q4. 주민등록번호 뒷자리의 맨 첫번째 숫자는 성별을 나타낸다. 주민번호에서 성별을 나타내는 숫자를 출력해 보자.
pin = '881120-1068234'
idx  pin.index('-')
type_id = pin[idx+1:][0]
if type_id == '1':
    print("남자")
else:
    print("여자")

# Q5. 다음과 같은 문자열 a:b:c:d:가 있다. 문자열의 replace 함수를 사용하여 a#b#c#d로 바꿔서 출력해 보자
a = 'a:b:c:d'
result = a.replace(':', '#')
print(result)

# Q6. [1, 3, 5, 4, 2] 리스트를 [5, 4, 3, 2, 1] 로 만들어 보자
a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()
print(a)

# Q7. ['life', 'is', 'too', 'short'] 리스트를 Life is too short 문자열로 만들어 출력해 보자.
a = ['life', 'is', 'too', 'short']
result = " ".join(a)
print(result)
"""
str_sentence = ''
for i in str_list:
    str_sentence += i
    str_sentence += ' '
"""

# Q8. (1, 2, 3) 튜플에 값 4를 추가하여 (1, 2, 3, 4)를 만들어 출력해 보자
a = (1, 2, 3)
result = a + (4, )
print(result)

# Q9. 다음과 같은 딕셔너리 a가 있다. 
# 다음 중 오류가 발생하는 경우를 고르고, 그 이유를 설명해 보자
"""
a[[1]] = 'python' # dict 의 key 는 list 를 입력할 수 없다. 
"""

# Q10. 딕셔너리 a에서 'B'에 해당되는 값을 추출해 보자.
a = {'a':90, 'b':80, 'c':70}
print(a.pop('b'))

# Q11. a 리스트에서 중복 숫자를 제거해 보자.
a = [1, 1, 2, 2, 3, 4, 4, 5]
b = set(a)
print(b)

# Q12. 파이썬은 다음처럼 동일한 값에 여러 개의 변수를 선언할 수 있다. 
# 다음과 같이 a, b 변수를 선언한 후 a의 두번째 요솟값을 변경하면
# b값은 어떻게 될까? 그리고 이런 결과가 오는 이유에 대해 설명해 보자

"""
a = b = [1, 2, 3]
a[1] = 4
print(b) # [1, 4, 3] 
list 의 변수는 주소값이기 때문에 a[1] 을 변경했을 때에 주소에 있는 값을 변경 
따라서 b도 값이 변경된다.
id(a) == id(b) # true
"""