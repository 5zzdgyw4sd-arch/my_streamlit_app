import random
import sys

answer = random.randint(100,1000)
try:
	while True:
		number = int(input("数字を代入してください."))
		if number == answer:
			print("正解です!")
			break
		
		elif number > answer:
			print("大きすぎます")
		
		else: 
			print("小さすぎます")

except ValueError:
	print("数字を代入しろ間抜け")
	sys.exit()
