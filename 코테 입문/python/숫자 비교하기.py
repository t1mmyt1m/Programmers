def solution(num1, num2):
    if 0 <= num1 <= 10000 and 0 <= num2 <= 10000:
        if num1 == num2:
            answer = 1
        elif num1 != num2:
            answer = -1
    return answer