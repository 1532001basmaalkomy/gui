from tkinter import *
from gtts import gTTS
import os

# إنشاء نافذة
myframe = Tk()
myframe.title("CUI.PYTHON")
myframe.geometry("500x500")
myframe.configure(bg="#5ce1e6")

label = Label(myframe, text="add your text here", font="tahoma 30 bold", bg="#5ce1e6")
label.pack(pady=30)

# دالة تشغيل النص وتحويله لصوت
def myfunction():
    text = myentry.get()
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")
    os.system("start output.mp3")

myentry = Entry(myframe, width=60)
myentry.pack(pady=10)

mybutton = Button(myframe, text="play", bg="#828686", fg="black", pady=30, padx=30, command=myfunction)
mybutton.pack(pady=10)

# دالة الخروج
def exitfun():
    exit()

mybutton1 = Button(myframe, text="exit", bg="red", fg="black", pady=30, padx=30, command=exitfun)
mybutton1.pack(pady=10)

# دالة حذف النص
def delete():
    myentry.delete(0, END)

mybutton2 = Button(myframe, text="set", bg="#85acad", fg="black", pady=30, padx=30, command=delete)
mybutton2.pack(pady=10)

myframe.mainloop()
