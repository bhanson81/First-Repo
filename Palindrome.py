

def isPalindrome(s):
	return s == s[::-1]


# Driver code
s = "catac"
ans = isPalindrome(s)

if ans:
	print("Yes")
else:
	print("No")
