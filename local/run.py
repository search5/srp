import random
import lib
import sys

avail_srp = ["가위", "바위", "보"]

def main():
    user_input = input("가위, 바위, 보 중 하나를 입력하세요.\n")
    if user_input not in avail_srp:
        print("잘못된 정보를 입력하셨어요")
    
    if lib.ruling(random.choice(avail_srp), user_input):
        print("내가 이겼어요")
    else:
        print("내가 졌어요")

if __name__ == "__main__":
    main()