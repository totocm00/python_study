original = input("문자열을 입력하시요:")
word = original.lower()         # 입력 받은 문자열을 소문자로 변경한다.
vowels = 0
consonants = 0

#if not original.isalpha():  # 문자열이 알파벳이라면
for char in original:
    if 0xAC00 <= ord(char) <= 0xD7A3:
        original = input("알파벳이 아닙니다, 다시 입력해주세요: ")
        break

if len(original) > 0 and original.isalpha():        # 문자열의 길이가 0 초과이고, 알파벳이라면
    for char in word:                               # 각 문자에 대한 반복을 실행
        if char in "aeiou":
            vowels = vowels + 1                     # vowels변수에 1을 증가한다
        else:                                       # 모음이 아니라면...
            consonants = consonants + 1             # consonants변수에 1을 증가한다
print("모음의 개수", vowels)
print("자음의 개수", consonants)
print("소문자로 바꾸기:", original.lower())
print("대문자로 바꾸기:", original.upper())