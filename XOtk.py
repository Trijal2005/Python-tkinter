from tkinter import *

def adder(a,b,c):
    return a+b+c

root=Tk()
root.title("XO")
root.iconbitmap("Xo.ico")
l=Label(root,text="WELCOME TO Tic Tac Toe",pady=5,padx=23).grid(row=0,column=0,columnspan=3,sticky=W+E)

# 1st row
b1=Entry(root,width=3,border=2)
b1.grid(row=1,column=0,pady=2)

b2=Entry(root,width=3,border=2)
b2.grid(row=1,column=1,pady=2)

b3=Entry(root,width=3,border=2)
b3.grid(row=1,column=2,pady=2)



#2nd row
b4=Entry(root,width=3,border=2,)
b4.grid(row=2,column=0,pady=2)

b5=Entry(root,width=3,border=2)
b5.grid(row=2,column=1,pady=2)

b6=Entry(root,width=3,border=2)
b6.grid(row=2,column=2,pady=2)


#3rd row
b7=Entry(root,width=3,border=2,)
b7.grid(row=3,column=0,pady=2)

b8=Entry(root,width=3,border=2)
b8.grid(row=3,column=1,pady=2)

b9=Entry(root,width=3,border=2)
b9.grid(row=3,column=2,pady=2)

X=[0,0,0,0,0,0,0,0,0]
O=[0,0,0,0,0,0,0,0,0]

def read():
    if(b1.get()=="X"):
        X[0]=1
        b1L=Label(root,text="X",border=2,width=3)
        b1L.grid(row=1,column=0,pady=2)
    if(b1.get()=="O"):
        O[0]=1
        b1L=Label(root,text="O",border=2,width=3)
        b1L.grid(row=1,column=0,pady=2)
    if(b2.get()=="X"):
        X[1]=1
        b2L=Label(root,text="X",border=2,width=3)
        b2L.grid(row=1,column=1,pady=2)
    if(b2.get()=="O"):
        O[1]=1
        b2L=Label(root,text="O",border=2,width=3)
        b2L.grid(row=1,column=1,pady=2)
    if(b3.get()=="X"):
        X[2]=1
        b3L=Label(root,text="X",border=2,width=3)
        b3L.grid(row=1,column=2,pady=2)
    if(b3.get()=="O"):
        O[2]=1
        b3L=Label(root,text="O",border=2,width=3)
        b3L.grid(row=1,column=2,pady=2)
    if(b4.get()=="X"):
        X[3]=1
        b4L=Label(root,text="X",border=2,width=3)
        b4L.grid(row=2,column=0,pady=2)
    if(b4.get()=="O"):
        O[3]=1
        b4L=Label(root,text="O",border=2,width=3)
        b4L.grid(row=2,column=0,pady=2)
    if(b5.get()=="X"):
        X[4]=1
        b5L=Label(root,text="X",border=2,width=3)
        b5L.grid(row=2,column=1,pady=2)
    if(b5.get()=="O"):
        O[4]=1
        b5L=Label(root,text="O",border=2,width=3)
        b5L.grid(row=2,column=1,pady=2)
    if(b6.get()=="X"):
        X[5]=1
        b6L=Label(root,text="X",border=2,width=3)
        b6L.grid(row=2,column=2,pady=2)
    if(b6.get()=="O"):
        O[5]=1
        b6L=Label(root,text="O",border=2,width=3)
        b6L.grid(row=2,column=2,pady=2)
    if(b7.get()=="X"):
        X[6]=1
        b7L=Label(root,text="X",border=2,width=3)
        b7L.grid(row=3,column=0,pady=2)
    if(b7.get()=="O"):
        O[6]=1
        b7L=Label(root,text="O",border=2,width=3)
        b7L.grid(row=3,column=0,pady=2)
    if(b8.get()=="X"):
        X[7]=1
        b8L=Label(root,text="X",border=2,width=3)
        b8L.grid(row=3,column=1,pady=2)
    if(b8.get()=="O"):
        O[7]=1
        b8L=Label(root,text="O",border=2,width=3)
        b8L.grid(row=3,column=1,pady=2)
    if(b9.get()=="X"):
        X[8]=1
        b9L=Label(root,text="X",border=2,width=3)
        b9L.grid(row=3,column=2,pady=2)
    if(b9.get()=="O"):
        O[8]=1
        b9L=Label(root,text="O",border=2,width=3)
        b9L.grid(row=3,column=2,pady=2)
    return X,O
    
def checkwinner(X,O):
    win=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for i in win:
        if(adder(X[i[0]],X[i[1]],X[i[2]])==3):
            return 1
        elif(adder(O[i[0]],O[i[1]],O[i[2]])==3):
            return 0

def button_done(var):
    global msg
    global done

    done=Button(root,text="✔",padx=4,command=lambda:button_done(var+1))
    done.grid(row=4,column=0,pady=3)

    x,y=read()

    msg.grid_forget()

    if var==9:
            msg=Label(root,text="Draw !")
            msg.grid(row=5,column=0,columnspan=3,sticky=W+E)

            done=Button(root,text="✔",padx=4,state=DISABLED)
            done.grid(row=4,column=0,pady=3)
    
    if(var%2==0):
        msg=Label(root,text="X chance:",relief=SUNKEN,anchor=W)
        msg.grid(row=5,column=0,columnspan=3,sticky=W+E)
    else:
        msg=Label(root,text="O chance:",relief=SUNKEN,anchor=W)
        msg.grid(row=5,column=0,columnspan=3,sticky=W+E)
    
    if(checkwinner(x,y)==1):
        msg=Label(root,text="X Won !")
        msg.grid(row=5,column=0,columnspan=3,sticky=W+E)

        done=Button(root,text="✔",padx=4,state=DISABLED)
        done.grid(row=4,column=0,pady=3)

    elif(checkwinner(x,y)==0):
        msg=Label(root,text="O Won !")
        msg.grid(row=5,column=0,columnspan=3,sticky=W+E)

        done=Button(root,text="✔",padx=4,state=DISABLED)
        done.grid(row=4,column=0,pady=3)
    

done=Button(root,text="✔",padx=4,command=lambda:button_done(1))
done.grid(row=4,column=0,pady=4)

bexit=Button(root,text="Exit",command=root.quit)
bexit.grid(row=4,column=2)

msg=Label(root,text="X chance:",relief=SUNKEN,anchor=W)
msg.grid(row=5,column=0,columnspan=3,sticky=W+E)

root.mainloop()