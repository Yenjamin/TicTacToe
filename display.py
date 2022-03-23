from tkinter import *
import tkinter.messagebox as msg

numbers = [1,2,3,4,5,6,7,8,9]
sign = ""
count = 0
blocks = ["block"]*10
class display(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Tic Tac Toe")
        Label(self,text="player1 : X",font="times 15").grid(row=0,column=1)
        Label(self,text="player2 : O",font="times 15").grid(row=0,column=2)
        def winCondition(blocks,sign):
            return ((blocks[1] == blocks[2] == blocks [3] == sign)
                or (blocks[1] == blocks[4] == blocks [7] == sign)
                or (blocks[1] == blocks[5] == blocks [9] == sign)
                or (blocks[2] == blocks[5] == blocks [8] == sign)
                or (blocks[3] == blocks[6] == blocks [9] == sign)
                or (blocks[3] == blocks[5] == blocks [7] == sign)
                or (blocks[4] == blocks[5] == blocks [6] == sign) 
                or (blocks[7] == blocks[8] == blocks [9] == sign))
        def gameTrack(number):
            if number==1 and number in numbers:
                button1.config(text = check(number))
                win()
            if number==2 and number in numbers:
                button2.config(text = check(number))
                win()
            if number==3 and number in numbers:
                button3.config(text = check(number))
                win()
            if number==4 and number in numbers:
                button4.config(text = check(number))
                win()
            if number==5 and number in numbers:
                button5.config(text = check(number))
                win()
            if number==6 and number in numbers:
                button6.config(text = check(number))
                win()
            if number==7 and number in numbers:
                button7.config(text = check(number))
                win()
            if number==8 and number in numbers:
                button8.config(text = check(number))
                win()
            if number==9 and number in numbers:
                button9.config(text = check(number))
                win()
        def check(number):
            global count, sign
            numbers.remove(number)
            if count%2==0:
                sign ='X'
                blocks[number]=sign
            elif count%2!=0:
                sign = 'O'
                blocks[number]=sign
            count += 1
            return sign
        def win():
            if(winCondition(blocks,sign) and sign=="X"):
                msg.showinfo("Result","Player1 wins")
                self.destroy()
            elif(winCondition(blocks,sign) and sign=="O"):
                msg.showinfo("Result","Player2 wins")
                self.destroy()
            elif count == 9:
                msg.showinfo("Result","Draw")
                self.destroy()
        button1=Button(self,width=15,font=("Times 16 bold"),height=7,command=lambda:gameTrack(1))
        button1.grid(row=1,column=1)
        button2=Button(self,width=15,height=7,font=("Times 16 bold"),command=lambda:gameTrack(2))
        button2.grid(row=1,column=2)
        button3=Button(self,width=15,height=7,font=("Times 16 bold"),command=lambda:gameTrack(3))
        button3.grid(row=1,column=3)
        button4=Button(self,width=15,height=7,font=("Times 16 bold"),command=lambda:gameTrack(4))
        button4.grid(row=2,column=1)
        button5=Button(self,width=15,height=7,font=("Times 16 bold"),command=lambda:gameTrack(5))
        button5.grid(row=2,column=2)
        button6=Button(self,width=15,height=7,font=("Times 16 bold"),command=lambda:gameTrack(6))
        button6.grid(row=2,column=3)
        button7=Button(self,width=15,height=7,font=("Times 16 bold"),command=lambda:gameTrack(7))
        button7.grid(row=3,column=1)
        button8=Button(self,width=15,height=7,font=("Times 16 bold"),command=lambda: gameTrack(8))
        button8.grid(row=3,column=2)
        button9=Button(self,width=15,height=7,font=("Times 16 bold"),command=lambda: gameTrack(9))
        button9.grid(row=3,column=3)
        self.mainloop()