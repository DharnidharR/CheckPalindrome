start=0
num=input()

end=len(num)
def check_palindrome(num,start,end):
    if (start>end):
        return 1
    if (num[start]!=num[end]):
        return 0
    return check_palindrome(num,start+1,end-1)
print(check_palindrome(num,start,end-1))
