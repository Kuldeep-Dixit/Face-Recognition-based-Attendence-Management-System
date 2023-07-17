from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from ContactUs import Helpsupport

class ChatBot:
    def __init__(self,root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.entry_fun)


        main_frame=Frame(self.root,bd=4,bg='powder blue',width=610)
        main_frame.pack()


        img_chat = Image.open('Images/download.png')
        img_chat=img_chat.resize((200,70),Image.Resampling.LANCZOS)
        self.photoimg= ImageTk.PhotoImage(img_chat)

        Title_label = Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text='CHAT ME',font=('arial',30,'bold'),bg='white',fg='green')
        Title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text=Text(main_frame,width=65,height=20,border=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()


        btn_frame = Frame(self.root,bd=4,bg='white',width=610)
        btn_frame.pack()

        label_1 = Label(btn_frame,text='Type Anything',font=('arial',20,'bold'),bg='white',fg='green')
        label_1.grid(row=0,column=0,padx=0,sticky=W)

        self.entry=StringVar()
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=30,font=('times new roman',17,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text='Send',command=self.send,font=('arial',16,'bold'),width=8,bg='green')
        self.send.grid(row=0,column=2,padx=5,sticky=W)


        self.clear=Button(btn_frame,text='Clear Chat',command=self.clear,font=('arial',16,'bold'),width=8,bg='green')
        self.clear.grid(row=1,column=1,sticky=W)
    
        self.exit=Button(btn_frame,text='Exit',command=self.iExit,font=('arial',16,'bold'),width=8,bg='green')
        self.exit.grid(row=1,column=2,padx=5,sticky=W)
        
        self.contact=Button(btn_frame,command=self.helpUs,text='Contact Us',font=('arial',16,'bold'),width=8,bg='green')
        self.contact.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label_11 = Label(btn_frame,text=self.msg,font=('arial',20,'bold'),bg='white',fg='red')
        self.label_11.grid(row=0,column=0,padx=0,sticky=W)


        # =====================Fuction Declaration===============
    def entry_fun(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')



    def send(self):
        send = '\t\t\t'+'You:'+self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg='Please enter some Input'
            self.label_11.config(text=self.msg,fg='red',font=('arial',14,'bold'))

        else:
            self.msg=''
            self.label_11.config(text=self.msg,fg='red')

        if (self.entry.get()=='hello'):
            self.text.insert(END,'\n\n'+'Bot: Hello!')

        elif (self.entry.get()=='hii'):
            self.text.insert(END,'\n\n'+'Bot: Hi')

        elif (self.entry.get()=='who are you'):
            self.text.insert(END,'\n\n'+'Bot: I am J.A.R.V.I.S.. How can I help you?')

        elif (self.entry.get()=='what is your name'):
            self.text.insert(END,'\n\n'+'Bot: My Name is J.A.R.I.S.')

        elif (self.entry.get()=='who made you'):
            self.text.insert(END,'\n\n'+'Bot: Mr. Kuldeep Dixit(@KDCoder) made me using Python.')

        elif (self.entry.get()=='how are you'):
            self.text.insert(END,'\n\n'+'Bot: I am Fine sir. What about you.')

        else:
            self.text.insert(END,'\n\n'+"Bot: Sorry I didn't get it.")

        




    def helpUs(self):
        self.new_window = Toplevel(self.root)
        self.app = Helpsupport(self.new_window)

    def iExit(self):
                self.root.destroy()


if __name__ == '__main__':
    root = Tk()
    obj=ChatBot(root)
    root.mainloop()