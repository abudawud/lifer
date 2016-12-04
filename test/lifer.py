''' 
/*
* --------------------------
* LiFeR	- Line Feed Remover
* -----------

COPYRIGHT
* Copyright (C) 2016  Ahmad Waris Al H
*
* This program is free software: you can redistribute it and/or modify
* it under the terms of the GNU General Public License as published by
* the Free Software Foundation, either version 3 of the License, or
* (at your option) any later version.
*
* This program is distributed in the hope that it will be useful,
* but WITHOUT ANY WARRANTY; without even the implied warranty of
* MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
* GNU General Public License for more details.
*
* You should have received a copy of the GNU General Public License
* along with this program.  If not, see <http://www.gnu.org/licenses/>.
*
*
* AUTHOR
* Amad Waris Al H (warisafidz@gmail.com) - Abu Dawud
*/
'''

from __future__ import print_function

def nprint(msg):
	print(msg, end = '')


text = open("input.txt", "r")

title = 0	#title string
tbool = True		#title state
tcontrol = True

next = ''	#store next read char
last = '\0'	#store printing char
consen = False		#check if continous sentences
skip = False

for next in text.read():
	if tbool == True:
		if last == ' ':
			title += 1
		if title >= 5:
			tbool = False
			
	if next == '\n':
		pastch = False
		if last == '.':
			nprint(".\n\n")
			#skip = True
			tbool = True
			title = 0
		elif tbool == True:
			nprint("%c\n" %last)
			title = 0
			#skip = True		#skip to next char
		elif last == '-':
			nprint('-')
			consen = True	#continous sentence
		elif ord(last) <= 122:
			nprint(last)
		elif ord(last) >= 122:
			consen = True	#continous sentence
	else:
		if last == '\n' and tbool == False and consen == False:
			nprint(' ')		#space only on uncontinous sentence
		elif ord(last) <= 122 and last != '\n':
			nprint(last)

	last = next

print("\n\nAll Done")
print("author@abudawud")
