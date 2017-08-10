# Tic-Tac-Toe Game Liam J. Cattell 8/10/17 for High Score Academy Python Class
# Import the modules needed 
import turtle
import random


A=[1,2,3,4,5,6,7,8,9]

# function to initialize board which is stored as a list of lists
def init_board():
	tmp=[]
	B=[]
	for i in range(1,4):
		tmp.append(i)
	B.append(tmp)

	tmp=[]
	for i in range(4,7):
		tmp.append(i)
	B.append(tmp)

	tmp=[]
	for i in range(7,10):
		tmp.append(i)
	B.append(tmp)

	return B

# don't print the horizontal seperator on the last row
def print_board(B):
	# print blank line before and after board
	print("\n")
	for i in range(0,3):
		print(B[i][0],"|",B[i][1],"|", B[i][2])
		if i!=2:
			print("---------")
	print("\n")

# check the board for 3 of the same character in a row and then return the character(symbol)
def is_winner(B):
	# check the rows for the same character 3 times in a row
	for row in B:
		if row[0]==row[1] and row[1]==row[2]:
			return row[0]
	
	# check the columns for the same character 3 times in a row
	for i in range(0,3):
		if B[0][i]==B[1][i] and B[1][i]==B[2][i]:
			return B[0][i]
	
	# check the two diagonals for the same character 3 times in a row
	if B[0][0]==B[1][1] and B[1][1]==B[2][2]:
		return B[0][0]
	if B[0][2]==B[0][1] and B[0][1]==B[2][0]:
		return B[0][2]

# adds a symbol to the board for the player at one of the available positions
# removes that position from the list A and also checks if you picked a valid position.
def add_player_symbol(A,B,symbol):
	done=False
	while not done:
		prompt="Please choose a position in the board from "+str(A)+" >> "
		position=int(input(prompt))
		if position in A:
			done=True
			idx=A.index(position)
			del A[idx]
			# update the board B here we usw integer division (//) and remainder (%)
			# to convert to coordinates in the list of lists B
			# we subtract 1 because the numbers in the board are 1-9 but we need them to be 0-8
			row=(position-1)//3
			col=(position-1)%3
			B[row][col]=symbol

# adds a symbol to the board for the computer using a random choice from the list A
def add_computer_symbol(A,B,symbol):
	# get a random index into the list A
	# we need to subtract 1 because the method randint(a,b) returns a number a <= x <= b unlike range(a,b) which
	# returns a number list with a <= x < b. If your list has length 5 then the index should only go from 0 to 4.			
	idx=random.randint(0, len(A)-1)
	# get the number at that index
	position = A[idx]
	del A[idx]	
	row=(position-1)//3
	col=(position-1)%3
	B[row][col]=symbol


# Let's us the functions we have defined to check that everything is working

B=init_board()

print_board(B)

add_player_symbol(A,B,'X')
s=is_winner(B)
if s=="X":
	print ("Player wins!")
if s=="O":
	print ("Computer wins!")

print_board(B)

add_computer_symbol(A,B,'O')
s=is_winner(B)
if s=="X":
	print ("Player wins!")
if s=="O":
	print ("Computer wins!")

print_board(B)

add_player_symbol(A,B,'X')
s=is_winner(B)
if s=="X":
	print ("Player wins!")
if s=="O":
	print ("Computer wins!")

print_board(B)

add_computer_symbol(A,B,'O')
s=is_winner(B)
if s=="X":
	print ("Player wins!")
if s=="O":
	print ("Computer wins!")

print_board(B)

add_player_symbol(A,B,'X')
s=is_winner(B)
if s=="X":
	print ("Player wins!")
if s=="O":
	print ("Computer wins!")

print_board(B)

add_computer_symbol(A,B,'O')
s=is_winner(B)
if s=="X":
	print ("Player wins!")
if s=="O":
	print ("Computer wins!")

print_board(B)

