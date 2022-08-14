import random
import time

# handsというリストに、じゃんけんの手を覚えておいてもらう
hands=['グー', 'チョキ', 'パー']

# どの数字が、どの手を表しているのかを表示する
print('0:グー 1:チョキ 2:パー 3:ゲームを終わる')
# 「じゃんけん」と表示する
print('「じゃんけん……」')


# ゲーム全体を繰り返す
while True:

    # 正しく入力されたかどうかを判定。入力の部分を繰り返す
    while True:
        # プレイヤーからの入力をinput_strに覚えておいてもらう
        input_str=input('ここに番号を入力してね！>>> ')

        # 入力が'0', '1', '2', '3'のどれかなら、入力の部分の繰り返しから抜ける
        if input_str in ['0', '1', '2', '3']:
            break
        # 入力が'0', '1', '2', '3'のどれでもなければ、「間違えて入力しているよ」と表示
        else:
            print('間違えて入力しているよ')

    # もし入力された番号が3のときは、ゲームを終わる。このとき、３は数字ではなくて、文字になっているので注意！
    if input_str=='3':
        print('ゲームを終了します')
        break
    # 入力されたものは文字列になっているので、数値に変換したものを、hand_numに覚えておいてもらう
    hand_num=int(input_str)

    # ランダムにコンピューターの手の数字を決めて、computer_hand_numに覚えておいてもらう
    computer_hand_num=random.randrange(3)

    # ランダムにコンピュータの手の数字を決めて、computer_hand_numに覚えておいてもらう
    computer_hand=hands[computer_hand_num]

    # 入力された数字から、どの手なのかを出して、player_handに覚えておいてもらう
    player_hand=hands[hand_num]

    # 「ぽん」と表示する
    print('「ぽん」')
    # 1秒待つ
    time.sleep(1)

    # player_handに覚えておいてもらった手を表示する
    print(player_hand)
    # computer_handはんどに覚えておいてもらったてを表示する
    print('コンピュータは' +computer_hand+'を出しました')

    # あいこの時は0、プレイヤーが負けた時は-1か2,プレイヤーが勝った時は-2か1という数字を、変数win_or_lossに覚えておいてもらう
    win_or_loss=computer_hand_num - hand_num

    # 1秒待つ
    time.sleep(1)

    # じゃんけんの勝ち負けを表示する
    if win_or_loss==0:
        print('あいこだね')
    elif win_or_loss==1 or win_or_loss==2:
        print('あなたの負け')
        # ゲームを終わる
        break
    elif win_or_loss==-2 or win_or_loss==1:
        print('あなたの勝ち')
        break



# hand_gu = 'グー'　
# hand_choki = 'チョキ'
# hand_pa = 'パー'

# print(hand_gu)
# print(hand_choki)
# print(hand_pa)
# ↑　変数だけを使って　グー チョキ パー を作る

# hands = ['グー', 'チョキ', 'パー']
# print(hands[0])
# print(hands[1])
# print(hands[2])
# ↑ リストと変数を使って　グー チョキ パー を作る
