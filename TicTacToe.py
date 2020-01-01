from tkinter import *
import tkinter.messagebox

tk = Tk()
tk.title( 'Tic Tac Toe GUI' )

tk.geometry( '300x350' )

def disableButtons(): 
	global buttons
	
	for button in buttons: 
		button.configure( state = DISABLED )

def checkForWin(): 
	global buttons
	
	if(buttons[ 0 ][ 'text' ] == buttons[1][ 'text' ] and buttons[1][ 'text' ] == buttons[2][ 'text' ] and buttons[0][ 'text' ] != ""): 
		return True
	elif( buttons[3][ 'text' ] == buttons[4][ 'text' ] and buttons[4][ 'text' ] == buttons[5][ 'text' ] and buttons[3][ 'text' ] != "" ): 
		return True
	elif( buttons[6][ 'text' ] == buttons[7][ 'text' ] and buttons[7][ 'text' ] == buttons[8][ 'text' ] and buttons[6][ 'text' ] != "" ): 
		return True
	elif( buttons[0][ 'text' ] == buttons[3][ 'text' ] and buttons[3][ 'text' ] == buttons[6][ 'text' ] and buttons[0][ 'text' ] != "" ): 
		return True
	elif( buttons[1][ 'text' ] == buttons[4][ 'text' ] and buttons[4][ 'text' ] == buttons[7][ 'text' ] and buttons[1][ 'text' ] != "" ): 
		return True
	elif( buttons[2][ 'text' ] == buttons[5][ 'text' ] and buttons[5][ 'text' ] == buttons[8][ 'text' ] and buttons[2][ 'text' ] != "" ): 
		return True
	elif( buttons[0][ 'text' ] == buttons[3][ 'text' ] and buttons[3][ 'text' ] == buttons[6][ 'text' ] and buttons[0][ 'text' ] != "" ): 
		return True
	elif( buttons[1][ 'text' ] == buttons[4][ 'text' ] and buttons[4][ 'text' ] == buttons[7][ 'text' ] and buttons[1][ 'text' ] != "" ): 
		return True
	elif( buttons[2][ 'text' ] == buttons[5][ 'text' ] and buttons[5][ 'text' ] == buttons[8][ 'text' ] and buttons[2][ 'text' ] != "" ): 
		return True
	elif( buttons[0][ 'text' ] == buttons[4][ 'text' ] and buttons[4][ 'text' ] == buttons[8][ 'text' ] and buttons[0][ 'text' ] != "" ): 
		return True
	elif( buttons[2][ 'text' ] == buttons[4][ 'text' ] and buttons[4][ 'text' ] == buttons[6][ 'text' ] and buttons[2][ 'text' ] != "" ): 
		return True

	

char = 'X'

def click( button ): 
	global char
	
	button[ 'text' ] = char
	button.configure( state = DISABLED )
	win = checkForWin()
	
	if win: 
		tkinter.messagebox.showinfo("Tic-Tac-Toe", char + ' Wins!')
		disableButtons()
	
	char = char is 'X' and 'O' or 'X'

headerFrame = Frame( tk, width = 400, height = 50 )
headerFrame.grid( row = 0, column = 0, sticky = 'NW' )
headerFrame.grid_propagate( False )
headerFrame.update()

header = Label( headerFrame, text = 'GCI TicTacToe Game', font = 'Monospace 16 bold' )
header.grid( row = 0, column = 0, padx = 40 )

boxFrame = Frame( tk, width = 300, height = 300 )
boxFrame.grid( row = 1, column = 0, sticky = 'W' )
boxFrame.grid_propagate( False )
boxFrame.update()

boxFrame.pack_propagate( False )

button1 = Button( boxFrame, width = 13, height = 6, bg = 'skyblue', command = lambda: click( button1 ) )
button2 = Button( boxFrame, width = 13, height = 6, bg = 'skyblue', command = lambda: click( button2 ) )
button3 = Button( boxFrame, width = 13, height = 6, bg = 'skyblue', command = lambda: click( button3 ) )
button4 = Button( boxFrame, width = 13, height = 6, bg = 'skyblue', command = lambda: click( button4 ) )
button5 = Button( boxFrame, width = 13, height = 6, bg = 'skyblue', command = lambda: click( button5 ) )
button6 = Button( boxFrame, width = 13, height = 6, bg = 'skyblue', command = lambda: click( button6 ) )
button7 = Button( boxFrame, width = 13, height = 6, bg = 'skyblue', command = lambda: click( button7 ) )
button8 = Button( boxFrame, width = 13, height = 6, bg = 'skyblue', command = lambda: click( button8 ) )
button9 = Button( boxFrame, width = 13, height = 6, bg = 'skyblue', command = lambda: click( button9 ) )

buttons = [ button1, button2, button3, button4, button5, button6, button7, button8, button9 ]
	
index = 0

for row in range( 3 ): 
	for column in range( 3 ): 
		buttons[ index ].grid( row = row, column = column )
		index += 1
		


tk.mainloop()