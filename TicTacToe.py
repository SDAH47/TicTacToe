from tkinter import *

tk = Tk()
tk.title( 'Tic Tac Toe GUI' )

tk.geometry( '500x350' )

header = Label( tk, text = 'GCI Tik Tac Toe', font = 'Helvetica 20 bold' )
header.grid( row = 0, column = 0 )

btn1 = Button( tk, text = '', bg = 'skyblue', fg = 'white', width = 3, height = 1, font = 'Helvetica 20' )
btn1.grid( column = 1, row = 1 )
btn2 = Button( tk, text = '', bg = 'skyblue', fg = 'white', width = 3, height = 1, font = 'Helvetica 20' )
btn2.grid( column = 2, row = 1 )
btn3 = Button( tk, text = '', bg = 'skyblue', fg = 'white', width = 3, height = 1, font = 'Helvetica 20' )
btn3.grid( column = 3, row = 1 )
btn4 = Button( tk, text = '', bg = 'skyblue', fg = 'white', width = 3, height = 1, font = 'Helvetica 20' )
btn4.grid( column = 1, row = 2 )
btn5 = Button( tk, text = '', bg = 'skyblue', fg = 'white', width = 3, height = 1, font = 'Helvetica 20' )
btn5.grid( column = 2, row = 2 )
btn6 = Button( tk, text = '', bg = 'skyblue', fg = 'white', width = 3, height = 1, font = 'Helvetica 20' )
btn6.grid( column = 3, row = 2 )
btn7 = Button( tk, text = '', bg = 'skyblue', fg = 'white', width = 3, height = 1, font = 'Helvetica 20' )
btn7.grid( column = 1, row = 3 )
btn8 = Button( tk, text = '', bg = 'skyblue', fg = 'white', width = 3, height = 1, font = 'Helvetica 20' )
btn8.grid( column = 2, row = 3 )
btn9 = Button( tk, text = '', bg = 'skyblue', fg = 'white', width = 3, height = 1, font = 'Helvetica 20' )
btn9.grid( column = 3, row = 3 )

tk.mainloop()