import tkinter
import chess

board=chess.Board()

root = tkinter.Tk()
root.geometry('1000x1000')
root.title("Chess")

BB = tkinter.PhotoImage(file="BB.png")
BK = tkinter.PhotoImage(file="BK.png")
BP = tkinter.PhotoImage(file="BP.png")
BR = tkinter.PhotoImage(file="BR.png")
BQ = tkinter.PhotoImage(file="BQ.png")
BN = tkinter.PhotoImage(file="BN.png")

WB = tkinter.PhotoImage(file="WB.png")
WK = tkinter.PhotoImage(file="WK.png")
WP = tkinter.PhotoImage(file="WP.png")
WR = tkinter.PhotoImage(file="WR.png")
WQ = tkinter.PhotoImage(file="WQ.png")
WN = tkinter.PhotoImage(file="WN.png")
temp=''
chars=['a','b','c','d','e','f','g','h']
src=''

allButtons={}
	
def onClick(widget,mlist):
	#widget.configure(bg='blue')
	bt=str(widget)
	k=bt[8:]
	if(k==''):
		p=q=0
		key='b00'
	elif(k=='64'):
		key='b77'
		p=q=7
	else:
		k=int(k)
		p=k//8
		q=k%8
		if q==0:
			p=p-1
			q=7
		else:
			q=q-1
		#print(p,q)
		key='b'+str(p)+str(q)
	tn=(8-p)
	global src
	src=chars[q]+str(tn)
	print(src)
	if(allButtons[key]['img']!='null'):
		global temp
		temp=allButtons[key]['img']
		allButtons[key]['img']='null'
		mlist[p][q].configure(image='',height=6,width=12)

def handler(event):
	#print(temp)
	bt=str(event.widget)
	k=bt[8:]
	if(k==''):
		p=q=0
		key='b00'
	elif(k=='64'):
		key='b77'
		p=q=7
	else:
		k=int(k)
		p=k//8
		q=k%8
		if q==0:
			p=p-1
			q=7
		else:
			q=q-1
		#print(p,q)
		key='b'+str(p)+str(q)
	tnn=(8-p)
	global des
	global src
	des=chars[q]+str(tnn)
	print(src)
	print(des)
	move=chess.Move.from_uci(src+des)
	if(board.is_legal(move)):
		print("Inside Legal")
		if(temp=='BR'):
			event.widget.configure(image=BR,height=90,width=90)
			allButtons[key]['img']='BR'
		elif(temp=='BN'):
			event.widget.configure(image=BN,height=90,width=90)
			allButtons[key]['img']='BN'
		elif(temp=='BB'):
			event.widget.configure(image=BB,height=90,width=90)
			allButtons[key]['img']='BB'
		elif(temp=='BK'):
			event.widget.configure(image=BK,height=90,width=90)
			allButtons[key]['img']='BK'
		elif(temp=='BQ'):
			event.widget.configure(image=BQ,height=90,width=90)
			allButtons[key]['img']='BQ'
		elif(temp=='BP'):
			event.widget.configure(image=BP,height=90,width=90)
			allButtons[key]['img']='BP'
		elif(temp=='WR'):
			event.widget.configure(image=WR,height=90,width=90)
			allButtons[key]['img']='WR'
		elif(temp=='WN'):
			event.widget.configure(image=WN,height=90,width=90)
			allButtons[key]['img']='WN'
		elif(temp=='WB'):
			event.widget.configure(image=WB,height=90,width=90)
			allButtons[key]['img']='WB'
		elif(temp=='WK'):
			event.widget.configure(image=WK,height=90,width=90)
			allButtons[key]['img']='WK'
		elif(temp=='WQ'):
			event.widget.configure(image=WQ,height=90,width=90)
			allButtons[key]['img']='WQ'
		elif(temp=='WP'):
			event.widget.configure(image=WP,height=90,width=90)
			allButtons[key]['img']='WP'
	src=''
	des=''

def drawchess():
	#buttons names
	mlist=[]
	for i in range (8):
		row=[]
		for j in range (8):
			element='b'+str(i)+str(j)
			row.append(element)
		mlist.append(row)

	#button attributes
	global allButtons
	for i in range(8):
		for j in range(8):
			d={mlist[i][j]:{'img':'null','imgtype':'null'}}
			allButtons.update(d)


	for i in range (8):
		for j in range (8):
			keyval=mlist[i][j]
			shift=''
			if i%2 == 0 and j%2 == 0 or i%2 == 1 and j%2 == 1 :
				col='grey'
			else:
				col='white'
			mlist[i][j]=tkinter.Button(root,state='normal',height=6,width=12,bg=col,activebackground=col)
			mlist[i][j].config(command=lambda widget=mlist[i][j]: onClick(widget,mlist))
			mlist[i][j].bind('<Double-Button-1>', handler)
			mlist[i][j].grid(row=i,column=j)
			if i==0:
				if (j==0 or j==7):
					mlist[i][j].configure(image=BR,height=90,width=90)
					allButtons[keyval]['img']='BR'
					allButtons[keyval]['imgtype']='B'
				elif j==1 or j==6:
					mlist[i][j].configure(image=BN,height=90,width=90)
					allButtons[keyval]['img']='BN'
					allButtons[keyval]['imgtype']='B'
				elif j==2 or j==5:
					mlist[i][j].configure(image=BB,height=90,width=90)
					allButtons[keyval]['img']='BB'
					allButtons[keyval]['imgtype']='B'
				elif j==3 :
					mlist[i][j].configure(image=BQ,height=90,width=90)
					allButtons[keyval]['img']='BQ'
					allButtons[keyval]['imgtype']='B'
				else :
					mlist[i][j].configure(image=BK,height=90,width=90)
					allButtons[keyval]['img']='BK'
					allButtons[keyval]['imgtype']='B'
			if i==7:
				if (j==0 or j==7):
					mlist[i][j].configure(image=WR,height=90,width=90)
					allButtons[keyval]['img']='WR'
					allButtons[keyval]['imgtype']='W'
				elif j==1 or j==6:
					mlist[i][j].configure(image=WN,height=90,width=90)
					allButtons[keyval]['img']='WN'
					allButtons[keyval]['imgtype']='W'
				elif j==2 or j==5:
					mlist[i][j].configure(image=WB,height=90,width=90)
					allButtons[keyval]['img']='WB'
					allButtons[keyval]['imgtype']='W'
				elif j==3 :
					mlist[i][j].configure(image=WQ,height=90,width=90)
					allButtons[keyval]['img']='WQ'
					allButtons[keyval]['imgtype']='W'
				else :
					mlist[i][j].configure(image=WK,height=90,width=90)
					allButtons[keyval]['img']='WK'
					allButtons[keyval]['imgtype']='W'
			if i==1:
				mlist[i][j].configure(image=BP,height=90,width=90)
				allButtons[keyval]['img']='BP'
				allButtons[keyval]['imgtype']='B'
			if i==6:
				mlist[i][j].configure(image=WP,height=90,width=90)
				allButtons[keyval]['img']='WP'
				allButtons[keyval]['imgtype']='W'

		#print(allButtons)
drawchess()
root.mainloop()
