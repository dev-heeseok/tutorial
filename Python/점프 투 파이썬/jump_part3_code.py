"""
Q1. 다음 코드의 결괏값은 무엇일까?

a = "Life is too short, you need python"

```
if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
```
"""
# shirt 출력 


"""
Q2. while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
"""
a = 0
result = 0
while(a < 1000):
    a += 1
    if a % 3 == 0:
        result += a

print("3의 배수의 합 :", result)

"""
Q3. while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.

```
*
**
***
****
*****
```
"""
