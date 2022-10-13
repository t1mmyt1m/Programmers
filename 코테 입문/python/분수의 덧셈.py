def solution(denum1, num1, denum2, num2):
    denum = (denum1*num2) + (denum2*num1)
    num = (num1*num2)
    
    def get_gcd(a, b):
        if a%b == 0:
            return b
        else:
            return get_gcd(b, a%b)
    
    gcd = get_gcd(denum, num)
    answer = [denum/gcd, num/gcd]
    return answer