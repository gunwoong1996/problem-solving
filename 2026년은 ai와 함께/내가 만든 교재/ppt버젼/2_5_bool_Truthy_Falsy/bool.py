

user = {"id": "kim","age":20}

print(user["age"])

#=======================

user = {"level": 6}
if user["level"] >= 5:
    print("접근 가능")

#=======================

profile = {"name": "lee"}
age = profile.get("age", 0)
print(profile["name"])
print(age)

#=======================
data = {}
data["score"] = 100
print(data)

#====================

scores = {"kim": 90, "lee": 85}
for name in scores:
    print(name)


#=========================

#문자열 개수 세기
text = "banana"
count = {}

for ch in text:
    count[ch] = count.get(ch, 0) + 1

print(count)

