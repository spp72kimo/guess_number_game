# 猜數字遊戲

import random

print('猜數字遊戲')							# 遊戲標題

ans = []
for i in range(4):
	ans.append(random.randint(0, 9))

print('正確答案是：', ans)

Situation = True							#預設while迴圈為True
while Situation:
	guess_num = []
	count_A = 0
	count_B = 0

	num = input('猜四位正確數字：')
	guess_num = num.split()					#將input內容存成list(預設以空格區分)
	for i in range(len(guess_num)):
		guess_num[i] = int(guess_num[i])	#將str 轉換成int

	
	for i in range(len(guess_num)):			#判斷答案是否正確
		if guess_num[i] == ans[i]:
			count_A += 1
			if count_A == 4:
				print('恭喜答對！')
				Situation = False	 		#跳出while迴圈
		else:
			for j in range(len(ans)):
				if guess_num[i] == ans[j]:
					count_B += 1

	print(count_A, 'A', count_B, 'B')