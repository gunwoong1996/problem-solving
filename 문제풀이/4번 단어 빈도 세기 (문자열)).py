#문자열 문장이 주어질 때,각 단어가 몇 번씩 나오는지를 딕셔너리로 만들어라.



def count_words(text):
    counts = {}
    words = text.split()

    for w in words:
        if w not in counts:
            counts[w] = 1

        else:
            counts[w] += 1
        # 여기에 작성
        pass

    return counts

text = "apple banana apple orange banana apple"
print(count_words(text))