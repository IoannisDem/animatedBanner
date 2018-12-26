import time
import os
import alphabet#library which i create
DISPLAY = 50#size of display used by program
list_word = []
list_word = alphabet.alph()#each element of the list consist of a row of all the letters 
max = 0
for i in list_word:
	if len(i) > max:
		max = len(i)
far = DISPLAY#defines how far the banner is 
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
