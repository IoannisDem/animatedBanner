def alph():'''Add more characters of your desire, each character is in a 7x7 square(except space) and with 2 additional spaces'''
	let_dic = {"A":["*******  ",
					"*     *  ",
					"*     *  ",
					"*******  ",
					"*     *  ",
					"*     *  ",
					"*     *  "],
		"B":["*****    ",
			 "*   *    ",
			 "*   *    ",
			 "*******  ",
			 "*     *  ",
			 "*     *  ",
			 "*******  "],
		"C":["*******  ",
			 "*        ",
			 "*        ",
			 "*        ",
			 "*        ",
			 "*        ",
			 "*******  ",],
		"D":["*****    ",
			 "*    *   ",
			 "*     *  ",
			 "*      * ",
			 "*     *  ",
			 "*    *   ",
			 "*****    "],
		"E":["*******  ",
			 "*        ",
			 "*        ",
			 "****     ",
			 "*        ",
			 "*        ",
			 "*******  ",],
		"F":["*******  ",
			 "*        ",
			 "*        ",
			 "****     ",
			 "*        ",
			 "*        ",
			 "*        "],
		"G":["*******  ",
		     "*        ",
			 "*        ",
			 "*   ***  ",
			 "*     *  ",
			 "*     *  ",
			 "*******  "],
		"H":["*     *  ",
			 "*     *  ",
			 "*     *  ",
			 "*******  ",
			 "*     *  ",
			 "*     *  ",
			 "*     *  "],
		"I":["*******  ",
			 "   *     ",
			 "   *     ",
			 "   *     ",
			 "   *     ",
			 "   *     ",
			 "*******  "],
		"J":["*******  ",
			 "   *     ",
			 "   *     ",
			 "*  *     ",
			 "*  *     ",
			 "*  *     ",
			 "****     "],
		"K":["*     *  ",
			 "*    *   ",
			 "*   *    ",
			 "*  *     ",
			 "*   *    ",
			 "*    *   ",
			 "*     *  "],
		"L":["*        ",
			 "*        ",
			 "*        ",
			 "*        ",
			 "*        ",
			 "*        ",
			 "*******  "],
		"M":["*     *  ",
			 "**   **  ",
			 "* * * *  ",
			 "*  *  *  ",
			 "*     *  ",
			 "*     *  ",
			 "*     *  "],
		"N":["*     *  ",
			 "**    *  ",
			 "* *   *  ",
			 "*  *  *  ",
			 "*   * *  ",
			 "*    **  ",
			 "*     *  "],
		"O":["*******  ",
			 "*     *  ",
			 "*     *  ",
			 "*     *  ",
			 "*     *  ",
			 "*     *  ",
			 "*******  "],
		"P":["*******  ",
			 "*     *  ",
			 "*     *  ",
			 "*******  ",
			 "*        ",
			 "*        ",
			 "*        "],
		"Q":["******   ",
			 "*    *   ",
			 "*    *   ",
			 "*  * *   ",
			 "*   **   ",
			 "******   ",
			 "      *  "],
		"R":["*******  ",
			 "*     *  ",
			 "*     *  ",
			 "*******  ",
			 "*    *   ",
			 "*     *  ",
			 "*     *  "],
		"S":["*******  ",
			 "*        ",
			 "*        ",
			 "*******  ",
			 "      *  ",
			 "      *  ",
			 "*******  "],
		"T":["*******  ",
			 "   *     ",
			 "   *     ",
			 "   *     ",
			 "   *     ",
			 "   *     ",
			 "   *     "],
		"U":["*     *  ",
			 "*     *  ",
			 "*     *  ",
			 "*     *  ",
			 "*     *  ",
			 "*     *  ",
			 "*******  "],
		"V":["*     *  ",
			 "*     *  ",
			 " *   *   ",
			 " *   *   ",
			 "  * *    ",
			 "  * *    ",
			 "   *     "],
		"W":["*     *  ",
			 "*     *  ",
			 "*     *  ",
			 "*     *  ",
			 "*  *  *  ",
			 "* * * *  ",
			 "**   **  "],
		"X":["*     *  ",
			 " *   *   ",
			 "  * *    ",
			 "   *     ",
			 "  * *    ",
			 " *   *   ",
			 "*     *  "],
		"Y":["*     *  ",
			 " *   *   ",
			 "  * *    ",
			 "   *     ",
			 "   *     ",
			 "   *     ",
			 "   *     "],
		"Z":["*******  ",
			 "     *   ",
			 "    *    ",
			 "   *     ",
			 "  *      ",
			 " *       ",
			 "*******  "],
		" ":["    ",
			 "    ",
			 "    ",
			 "    ",
			 "    ",
			 "    ",
			 "    "]
		}
	word = (input("Enter word: ")).upper()
	list_word=[""]*100
	for row in range(7):
		for letter in word:
			list_word[row] += (let_dic[letter][row])
		 
	return list_word
			
