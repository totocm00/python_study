original = input("문자열을 입력하시오:")
word = original.lower()
vowels =0
consonants = 0

# is.isalpha()
# 한글, 일본어 다 가능함 그래서 특수문자 검출할 때 사용

if len(original) > 0 and original.isalpha():
	for char in word:
		if char in 'aeiou':
			vowels = vowels +1
			
		else:
			consonants = consonants + 1
			
	print("모음의 개수:", vowels)
	print("자음의 개수:", consonants)
	print("소문자로 바꾸기:", original.lower())
	print("대문자로 바꾸기:", original.upper())