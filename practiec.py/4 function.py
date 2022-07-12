# 애완동물을 소개해 주세요~
from unicodedata import name

animal = "강아지"
name = "미니"
age = 8
hobby = "간식"
is_adult = age >= 8




print("우리집 "+ animal +"의 이름은 "+ name +"예요")
print(name +"는 "+ str(age) +"살이며, "+ hobby +"을 아주 좋아해요")
print(animal +"는 어른일까요?" + str(is_adult))

# , = str 없이 쓸수있다 ex) 나는 ,배,가 고프다