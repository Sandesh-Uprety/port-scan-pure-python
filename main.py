from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.messagebox
from PIL import Image, ImageTk
from datetime import datetime
import socket
import sys


class App:
    def __init__(self, master):
        self.master = master
        self.master.geometry("1060x540")
        self.master.title("Port Scanner")  
        self.master.resizable(False, False)
        self.master.config(bg="skyblue")  

        self.frame1_left = Frame(self.master, bg='grey')
        self.frame1_left.place(x=10, y=10, width=380, height=500, )

        self.frame2_right = Frame(self.master)
        self.frame2_right.place(x=400, y=10, width=650, height=500)

        self.bg_o = Image.open("Picture1.png")
        self.bg_i = self.bg_o.resize((450,450))
        self.bg = ImageTk.PhotoImage(self.bg_i)
        self.bg_image = Label(self.frame2_right, image=self.bg)
        self.bg_image.place(x=10, y=10, relwidth=1, relheight=1)

        self.welcome = Label(self.frame1_left, text="\nPort Scanner\n", font=('arial 22 bold'),
                                fg='black', bg='grey')
        self.welcome.grid(row=0, column=0, padx=100)

        self.welcome = Label(self.frame1_left, text="\nBy Sandesh Uprety\n", font=('arial 16 bold'),
                             fg='black', bg = 'grey')
        self.welcome.grid(row=1, column=0, padx=100)

        self.b1 = Button(self.frame1_left, text='New Scan', compound=LEFT, width=30,
                             height=2, bg='steelblue', command=self.new_scan)
        self.b1.grid(row=2, column=0, padx=8, pady=50)
        self.b2 = Button(self.frame1_left, text='View History', compound=LEFT, width=30,
                         height=2, bg='steelblue', command=self.view_history)
        self.b2.grid(row=3, column=0, padx=8, pady=10)


    def new_scan(self):
        root.withdraw()
        top = Toplevel()
        top.geometry("1060x540")
        top.title("New Scan")
        top.resizable(False, False)
        top.config(bg="skyblue")

        self.frame1_left = Frame(top, bg='grey')
        self.frame1_left.place(x=10, y=10, width=500, height=500, )

        self.frame2_right = Frame(top)
        self.frame2_right.place(x=520, y=10, width=530, height=500)

        self.title = Label(self.frame1_left, text="New Scan", font=('arial 30 bold'), fg='black')
        self.title.place(x=150, y=20)

        #Enter IP
        self.ins1 = Label(self.frame1_left, text="Enter IP address:", font=('arial 12'), fg='black')
        self.ins1.place(x = 100, y = 180)

        #Enter port
        self.ins2 = Label(self.frame1_left, text="Enter port or range:", font=('arial 12'), fg='black')
        self.ins2.place(x = 100, y = 230)

        self.ip_add = Entry(self.frame1_left, width=20)
        self.ip_add.place(x = 300, y = 183)
        self.ip_add.insert(END, "192.168.254.254")

        self.port = Entry(self.frame1_left, width=20)
        self.port.place(x = 300, y = 233)

        self.scbtn = Button(self.frame1_left, text='Begin the scan', compound=LEFT, width=30,
                         height=2, bg='steelblue', command=self.socket)
        self.scbtn.place(x = 150,y = 300)

        self.rl = Label(self.frame2_right, text="Your result will show here", font=('arial 12'), fg='black')
        self.rl.pack()
        self.st = ScrolledText(self.frame2_right, width=50, height=10, wrap='word')
        self.st.pack(fill=BOTH, side=LEFT, expand=True)

    def view_history(self):
        root.withdraw()
        top = Toplevel()
        top.geometry("1060x540")
        top.title("New Scan")
        top.resizable(False, False)
        top.config(bg="skyblue")

        self.title = Label(top, text="View History", font=('arial 30 bold'), fg='black')
        self.title.pack()

        st = ScrolledText(top, width=50, height=10, wrap='word')
        st.pack(fill=BOTH, side=LEFT, expand=True)

        f = open("history.txt", "r")
        st.insert(END, f.read())

    def store(self, data):
        f = open("history.txt", "a")
        f.write(data)
        f.close()

    def socket(self):
        port = int(self.port.get())
        self.final_text = []
        self.texts = "*-"*17+f"*\nScanning port {port}", f"\nOn Time: {datetime.now()}" + f"\nScanning ip {self.ip_add.get()}\n" + "*-"*17+"*"
        strr = str(self.texts)
        self.final_text.append(strr)
        self.st.insert(END, self.texts)
        try:
            host = socket.gethostbyname(self.ip_add.get())
            print(host)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(1)
            result = s.connect_ex((f'{host}', port))
            if result == 0:
                self.final_text.append(f"\nSuccessful connection to port {port}")
                self.st.insert(END, f"\nSuccessful connection to port {port}")
                print(self.final_text)
            else:
                self.st.insert(END, f"\nPort {port} is closed.")
                self.final_text.append(f"\nPort {port} is closed")
            s.close()
            data = "".join(self.final_text)

        except KeyboardInterrupt:
            tkinter.messagebox.showwarning("Error","\nExiting.")
            sys.exit()

        except socket.gaierror:
            tkinter.messagebox.showwarning("Error","IP cannot be resolved.")
            sys.exit()

        except socket.error:
            tkinter.messagebox.showwarning("Error","Connection Problem.")
            sys.exit()

        self.store(data)
        return port

root = Tk()  # making an object of class Tk
b = App(root)  # making the object of class tkinter class App with root as variable to constructor
root.mainloop()