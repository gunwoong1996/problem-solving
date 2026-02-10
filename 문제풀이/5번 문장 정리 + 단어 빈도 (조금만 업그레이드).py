# # 문자열 문장이 주어질 때,

# 1. 모두 소문자로 바꾸고

# 2. 쉼표(,)와 마침표(.)를 제거한 뒤

# 3. 단어 빈도를 딕셔너리로 반환




def count_words_clean(text):
    counts = {}
    
    # 1. 소문자
    # 2. 쉼표, 마침표 제거
    text = text.lower() #문장 전체를 소문자로 통일한다.
    text = text.replace(",", "").replace(".", "") #쉼표 , 와 마침표 . 를 없애버린다.
    words = text.split() # 공백 기준으로 문장을 쪼개서 단어 리스트를 만든다.


    for w in words:

        if w not in counts:
            counts[w] = 1
        else:
            counts[w] += 1
        pass

    return counts

text = "Apple, banana apple. Orange banana, apple."
print(count_words_clean(text))