# ----- 코드 정의 ------
class member:
    name = ''
    username = ''
    password = ''

    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password
        print('어렵다 과제')

    def display(self):
        print(f"회원이름 : {self.name} 아이디: {self.username}")


class Post:
    title = ''
    content = ''
    auther = {{member.name}}

    def __init__(self, title, content, auther):
        self.title = title
        self.content = content
        self.auther = auther
        print('여기까진 이해 가능')


# 회원인스턴스
    m1 = member('강아지', '미루', '0000')
    m2 = member('고양이', '루피', '0000')
    m3 = member('토끼', '토롱이', '0000')
    # m1 = self
    # m1.name = 강아지
    # m1.username = '미루'
    # m1.password = '0000'


# ----- 코드 실행 ------
members = []
members.append(m1)
members.append(m2)
members.append(m3)

for member in members:
    print(member.name)


posts = []

# TODO : 코드 구현이 필요합니다.
