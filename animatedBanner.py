import time
import os
import alphabet
DISPLAY = 50
list_word = []
list_word = alphabet.alph()
max = 0
for i in list_word:
	if len(i) > max:
		max = len(i)
far = DISPLAY
print(max)
while True:
	if DISPLAY + far >= DISPLAY:
		varA = 0
	else:
		varA = abs(far)
	if far < -max:
		far = DISPLAY
	varB = DISPLAY - far
	os.system("cls")
	for row in range(7):
		print(far*" "+list_word[row][varA:varB])
	far -= 1
	time.sleep(0.05)