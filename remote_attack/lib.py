SCISSORES = "가위"
ROCK = "바위"
PAPER = "보"

def ruling(shield_hand, attach_hand):
    # 누가 이겼는지 알아야 한다.
    # 방어패가 이기면 True, 방어패가 지면 False
    if shield_hand == SCISSORES and attach_hand == ROCK:
        return False
    elif shield_hand == SCISSORES and attach_hand == PAPER:
        return True
    elif shield_hand == ROCK and attach_hand == SCISSORES:
        return True
    elif shield_hand == ROCK and attach_hand == PAPER:
        return False
    elif shield_hand == PAPER and attach_hand == SCISSORES:
        return False
    elif shield_hand == PAPER and attach_hand == ROCK:
        return True

if __name__ == "__main__":
    #srp = ["가위", "바위", "보"]
    print(ruling("가위", "바위"))