# ----- 코드 정의 ------
class member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password

    def display(self):
        print(f"회원이름 : {self.name} 아이디: {self.username}")


class post:
    def __init__(self, title, content, auther):
        self.title = title
        self.content = content
        self.auther = auther

     # 이 부분은 잘 모르겠다. class member 처럼 display를 써주어야하는 것 같은데 어떤 걸 써야하는지 아직 어렵다.


# 회원인스턴스 m1 당 네줄로 썼다가 구글링 해보고 더 알아보기 쉽게 수정하였다.
# m1=self 강아지=name 미루=username 0000=password
m1 = member('강아지', '미루', '0000')
m2 = member('고양이', '루피', '0000')
m3 = member('토끼', '토롱이', '0000')

members = []

members.append(m1)
members.append(m2)
members.append(m3)

for member in members:
    print(member.name)


posts = []

for member in members:
    print(member.name)

p1 = post('첫번째 글', '첫번째 내용', m1.name)
p2 = post('두번째 글', '두번째 내용', m1.name)
p3 = post('세번째 글', '세번째 내용', m1.name)
posts.append(p1)
posts.append(p2)
posts.append(p3)

p4 = post('네번째 글', '네번째 내용', m2.name)
p5 = post('다섯번째 글', '다섯번째 내용', m2.name)
p6 = post('여섯번째 글', '여섯번째 내용', m2.name)
posts.append(p4)
posts.append(p5)
posts.append(p6)

p7 = post('일곱번째 글', '일곱번째 내용', m3.name)
p8 = post('여덟번째 글', '여덟번째 내용', m3.name)
p9 = post('아홉번째 글', '아홉번째 내용', m3.name)
posts.append(p7)
posts.append(p8)
posts.append(p9)

print(posts)
