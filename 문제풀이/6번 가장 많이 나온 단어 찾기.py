# 문장이 주어질 때,가장 많이 나온 단어 하나만 반환하라.


def most_common_word(text):
    counts = {}
    words = text.split()

    # 1. 단어 세기 (아까 했던 거)
    for w in words:
        if w not in counts:
            counts[w] = 1
        
        else:
            counts[w] += 1
    return max(counts, key=counts.get)

text = "apple banana apple orange banana apple"
print(most_common_word(text))
