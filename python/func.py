# func.py

# 함수를 선언(정의), return을 사용한 경우
# def bmi(weight, height):
#     BMI = weight / height / height

#     return BMI


# # 함수를 호출(실행)
# print(bmi(67, 1.78))

# # return 없이 함수를 선언
# def bmi(weight, height):
#     BMI = weight / height / height

#     print(BMI)

# bmi(67, 1.78)



# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 함수 내부에 있는 변수를 함수 밖에서 참조하는 방법
# global 변수명
# 함수 내부에 참조할 변수를 global 키워드를 사용하여 선언 하면
# 외부에서 함수 내부에 있는 변수를 참조할 수 있음
# A함수 내부에 있는 값을 B함수에서 사용할 때 많이 씀
# global bmi                              # global 키워드를 사용하여 변수 선언

# def BMI(height, weight):
#     global bmi                          # 함수 내부에서 global 사용(이거 안쓰면 안됨)
#     # global bmi = 0                    # global 키워드에서 변수에 값을 넣을 수는 없음 (오류)
    
#     height = height / 100
#     bmi = weight / (height * height)

#     return bmi

# print(BMI(178, 80))
# print(bmi)                              # bmi라는 변수를 global로 지정했기 때문에 함수 내부에 있는 
#                                         # 값을 참조 가능


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# 재귀함수
# 함수 내부에서 자기자신을 호출하는 함수
# def function() :
#     print('Hello')
#     input()
#     function()        # 자기 자신을 호출

# function()


# 피보나치 수
# https://pythontutor.com/render.html#mode=display
def fibonacci(a, b) :
    c = a + b
    if(a < 100):
        print(a, end='  ')
        return fibonacci(b, c)      # return None이 계속 반복되어서 호출된 함수들이 종료 된다.
    else:
        return                      # return 하는 값 또는 변수가 없기 때문에 None이 return 됨

fibonacci(1, 1)
print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# def star(n):
#     sum = n + n
#     if(n <= 16):
#         print('*' * n, end=' ')
#         return star(sum)
#     else:
#         return

# star(1)
# print()


# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ #


# def at(a, b):
#     c = b
#     d = a * b
#     if(a <= 4):
#         print('@'*a,end='')
#         print(' ', end='')
#         print('^'*b,end='')
#         print(' ', end='')
#         return at(c,d)
#     else:
#         return

# at(1,2)
# print()


# def p(a, b):
#     a += 10
#     b += 5

#     return a, b

# x  = p(10,20)
# print(x)