import numpy as np
import math

# 建立不重複答案庫
def build_database():
    # 第一個不重複
    database = np.array([123])
    num = 123
    # 到最後一個不重複
    while(num < 987):
        num = num + 1
        hun = math.floor(num / 100)
        ten = math.floor(num / 10) % 10
        digit = num % 10
        # 去掉 0
        if(hun == 0 or ten == 0 or digit == 0):
            continue
        # 扣除重複
        if(hun == ten or hun == digit or ten == digit):
            continue
        database = np.append(database, num)
    return database

ans = 0
# 計算 AB
def generate_AB(guess):
    ans_hun = math.floor(ans / 100)
    ans_ten = math.floor(ans / 10) % 10
    ans_digit = ans % 10
    guess_hun = math.floor(guess / 100)
    guess_ten = math.floor(guess / 10) % 10
    guess_digit = guess % 10
    A = 0
    B = 0
    if(ans_hun == guess_hun):
        A = A + 1
    elif(ans_hun == guess_ten or ans_hun == guess_digit):
        B = B + 1
    if(ans_ten == guess_ten):
        A = A + 1
    if(ans_ten == guess_hun or ans_ten == guess_digit):
        B = B + 1
    if(ans_digit == guess_digit):
        A = A + 1
    elif(ans_digit == guess_hun or ans_digit == guess_ten):
        B = B + 1
    return A, B

first_guess = 0
# 找與第一次完全不重複的數
def find_another():
    first_guess_hun = math.floor(first_guess / 100)
    first_guess_ten = math.floor(first_guess /10) % 10
    first_guess_digit = first_guess % 10
    # 去除重複的數再洗牌
    temp = list(range(1, 10))
    temp.remove(first_guess_hun)
    temp.remove(first_guess_ten)
    temp.remove(first_guess_digit)
    np.random.shuffle(temp)
    guess_hun = temp[0]
    guess_ten = temp[2]
    guess_digit = temp[4]
    guess = guess_hun * 100 + guess_ten * 10 + guess_digit
    return guess

# 根據 AB 過濾答案庫
def filter(database, turn):
    guess = 0
    # if(turn == 1):
    #     guess = 123
    # # 如果 123 非 3B 1A2B 2A1B
    # elif(turn == 2 and len(database) > 3):
    #     guess = 456

    # 第一輪先從答案庫隨機挑選
    if(turn == 1):
        i = np.random.randint(0, len(database)-1)
        guess = database[i]
        global first_guess
        first_guess = guess
    # 第二輪找完全不重複的，若快接近答案則直接從答案庫挑 (約 1, 2, 3, 18)
    elif(turn == 2 and len(database) > 20):
        guess = find_another()

    else:
        i = np.random.randint(0, len(database)-1)
        guess = database[i]
    # print(f"{turn} guess: {guess}")
    # 產生 AB
    A, B = generate_AB(guess)
    if(A == 3):
        return np.array([guess])
    else:
        # 過濾答案庫
        del_index = []
        for i in range(len(database)):
            i_hun = math.floor(database[i] / 100)
            i_ten = math.floor(database[i] /10) % 10
            i_digit = database[i] % 10
            guess_hun = math.floor(guess / 100)
            guess_ten = math.floor(guess / 10) % 10
            guess_digit = guess % 10
            a = 0
            b = 0
            # 位置數字都對
            if(i_hun == guess_hun):
                a = a + 1
            if(i_ten == guess_ten):
                a = a + 1
            if(i_digit == guess_digit):
                a = a + 1
            # 位置錯數字對
            if(i_hun == guess_ten or i_hun == guess_digit):
                b = b + 1
            if(i_ten == guess_hun or i_ten == guess_digit):
                b = b + 1
            if(i_digit == guess_hun or i_digit == guess_ten):
                b = b + 1
            # 不合的答案記錄起來
            if(a != A or b != B):
                del_index = del_index + [i]
        # 刪除所有不合的答案
        return np.delete(database, del_index)

# 測試平均花費局數
def main():
    count = 500
    turn_list = []
    lens = []
    for i in range(count):
        database = build_database()
        # 隨機挑選答案
        rand = np.random.randint(0, len(database)-1)
        global ans
        ans = database[rand]
        # print(f"ans: {ans}")
        turn = 1
        while(len(database) > 1):
            database = filter(database, turn)
            if(turn == 1):
                lens = lens + [len(database)]
            turn = turn + 1
        turn_list = turn_list + [turn]
    # print(turn_list)
    print(f"average turn: {np.average(turn_list)}")
    print(f"average lens: {np.average(lens)}")
    temp = np.array(lens)
    print(f"least 10 lens: {np.sort(temp)[:10]}")

if __name__ == "__main__":
    main()
