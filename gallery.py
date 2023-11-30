from tkinter import *#Main import
from PIL import ImageTk,Image
root=Tk()
root.title("Gallery")
root.iconbitmap("icon_g.ico")
img1=ImageTk.PhotoImage(Image.open("img_1.jpg"))
img2=ImageTk.PhotoImage(Image.open("img_2.jpg"))
img3=ImageTk.PhotoImage(Image.open("img_3.jpg"))
img4=ImageTk.PhotoImage(Image.open("img_4.jpg"))
img5=ImageTk.PhotoImage(Image.open("img_5.jpg"))

ilist=[img1,img2,img3,img4,img5]

lab=Label(image=img1)
lab.grid(row=0,column=0,columnspan=3)

status=Label(root,text=f"{1} of {len(ilist)}",relief=SUNKEN,anchor=E)
status.grid(row=2,column=0,columnspan=3,sticky=W+E)

def forward(num):
    global lab
    global bfor
    global bback
    global status
    global c
    c=num
    c+=1
    lab.grid_forget() 
    
    lab=Label(image=ilist[num])
    lab.grid(row=0,column=0,columnspan=3)
    
    bfor=Button(root,text=">>>",command=lambda: forward(num+1))
    bback=Button(root,text="<<<",command=lambda:back(num-1))
    status=Label(root,text=f"{c} of {len(ilist)}",relief=SUNKEN,anchor=E)

    if(num==(len(ilist)-1)):
        bfor=Button(root,text=">>>",state=DISABLED)
        bfor.grid(row=1,column=2)
    
    bfor.grid(row=1,column=2)
    bback.grid(row=1,column=0)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)  

def back(num):
    global lab
    global bfor
    global bback
    global status
    global c
    c=num+1
    lab.grid_forget()

    lab=Label(image=ilist[num])
    lab.grid(row=0,column=0,columnspan=3)

    bback=Button(root,text="<<<",command=lambda:back(num-1))
    bfor=Button(root,text=">>>",command=lambda: forward(num+1))
    status=Label(root,text=f"{c} of {len(ilist)}",relief=SUNKEN,anchor=E) 
    if num==0:
        bback=Button(root,text="<<<",state=DISABLED)
        bback.grid(row=1,column=0)
    
    bfor.grid(row=1,column=2)
    bback.grid(row=1,column=0)
    status.grid(row=2,column=0,columnspan=3,sticky=W+E)  


    
bexit=Button(root,text="Exit",command=root.quit)
bfor=Button(root,text=">>>",command=lambda: forward(1))
bback=Button(root,text="<<<",command=back,state=DISABLED)

bfor.grid(row=1,column=2,pady=7)
bexit.grid(row=1,column=1)
bback.grid(row=1,column=0)

root.mainloop()


