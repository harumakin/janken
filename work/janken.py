import random


# handsというリストに、じゃんけんの手を覚えておいてもらう
hands=['グー', 'チョキ', 'パー']

# どの数字が、どの手を表しているのかを表示する
print('0:グー 1:チョキ 2:パー')

# プレイヤーからの入力をinput_strに覚えておいてもらう
input_str=input('ここに番号を入力してね！>>> ')
# 入力されたものは文字列になっているので、数値に変換したものを、hand_numに覚えておいてもらう
hand_num=int(input_str)

# ランダムにコンピューターの手の数字を決めて、computer_hand_numに覚えておいてもらう
computer_hand_num=random.randrange(3)

# ランダムにコンピュータの手の数字を決めて、computer_hand_numに覚えておいてもらう
computer_hand=hands[computer_hand_num]

# 入力された数字から、どの手なのかを出して、player_handに覚えておいてもらう
player_hand=hands[hand_num]

# player_handに覚えておいてもらった手を表示する
print(player_hand)
# computer_handはんどに覚えておいてもらったてを表示する
print('コンピュータは' +computer_hand+'を出しました')


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
