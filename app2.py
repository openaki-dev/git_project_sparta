import random

select = ["가위", "바위", "보"]
computer = random.choice(select)

while True:
    user = input("가위,바위,보 중에 한가지를 입력하세요.")
    if user in select:
        break
    else:
        print("잘못 입력하셨습니다.")


if user == "가위" and computer == "보" or \
   user == "바위" and computer == "가위" or \
   user == "보" and computer == "바위":
    print("이겼습니다.")

else:
    print("졌습니다.")
