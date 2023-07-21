import tkinter
import os
import socket
import threading
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import tkinter as tk
import time
import random

def on_enter(e):
    myButton['background'] = 'blue'
def on_leave(e):
    myButton['background'] = 'SystemButtonFace'

def on_enter1(e):
    myButton1['background'] = 'blue'
def on_leave1(e):
    myButton1['background'] = 'SystemButtonFace'

def on_enter2(e):
    myButton2['background'] = 'blue'
def on_leave2(e):
    myButton2['background'] = 'SystemButtonFace'

def on_enter3(e):
    myButton3['background'] = 'blue'
def on_leave3(e):
    myButton3['background'] = 'SystemButtonFace'




def helloCallBack():
   try:
    def transfer(filepaths):
        if filepaths == "" or filepaths is None:
            print("No file path found.")
            return

        lblMessage['text'] = ""
        for filepath in filepaths:
            path, filename = os.path.split(filepath)
            print("1. File Name: " + str(filename))
            while True:
                conn, addr = s.accept()
                print("2. Server: Connection from: ", addr)

                message = conn.recv(2048).decode()  
                print("3. Client: ", str(message))

                conn.send(filename.encode())  
                print("4. Server: File Name Sent")

                data = conn.recv(2048).decode()  
                print("5. Client: ", str(data))

                f = open(filepath, 'rb')
                data = f.read(2048)
                while data:
                    conn.send(data)
                    data = f.read(2048)
                f.close()
                t=random.randrange(2,7)
                while t >=0:
                    print(t, end='...')
                    time.sleep(1)
                    t -= 1

                print('\n6. File Received.\n')
                conn.close()
                lblMessage['text'] += "File Sent: " + filename + "\n"
                print("Select File...")
                break
    k = []

    def select_files():
        files = filedialog.askopenfilenames(initialdir="./", title="Select File",
                                            filetypes=(("all files", "*.*"), ("jpeg files", "*.jpg")))
        k.append(files)
        
        transfer(files)
        print(files)
        


    if __name__ == '__main__':
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.connect(("8.8.8.8", 80))
        ip = str(sock.getsockname()[0])
        sock.close()

        host = "0.0.0.0"
        port = 8000
        s = socket.socket()
        s.bind((host, port))
        s.listen(5)
        print('\nServer listening....')
        print("Select File...")

        lblWelcome = Label(text="Share Files")
        lblIp = Label(text="Host IP")
        lblIpValue = Label(text=ip)
        lblSelect = Label(text="Select File")
        btnSelect = Button(text="Select", command=select_files, width=10)
        lblMessage = Label(text="")

        lblWelcome.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        lblIp.grid(row=2, column=1, padx=10, pady=10)
        lblIpValue.grid(row=2, column=2, padx=10, pady=10)
        lblSelect.grid(row=3, column=1, padx=10, pady=10)
        btnSelect.grid(row=3, column=2, padx=10, pady=10)
        lblMessage.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
        root.mainloop()

   except Exception as e:
    print("Error: " + str(e));

def helloCallBack1():
   try:
    def connect():
        recieved_files = []
        host_ip = str(entHostIP.get())
        t1 = threading.Thread(target=transfer(host_ip))
        t1.daemon = True
        t1.start()


    def transfer(host_ip):
        while True:
            s = socket.socket()
            host = host_ip
            port = 8000
            s.connect((host, port))

            s.send(b'Send File...')  
            print("1. Client: Send File...")

            filename = s.recv(2048).decode()  
            print("2. Server: File Name: " + str(filename))

            received_files = []
            received_files.append(filename)

            # path = "/storage/emulated/0/Download/Test2/" + str(filename)
            directory = './Test/'
            if not os.path.exists(directory):
                os.makedirs(directory)
            path = directory + str(filename)
            
            s.send(b'Receiving File...')


            with open(path, 'wb') as f:
                print('File "' + str(filename) + '" opened')
                packet = 0
                while True:
                    packet += 1
                    # print("Packet: " + str(packet))
                    data = s.recv(2048)
                    if not data:
                        break
                    f.write(data)
            f.close()
            print("File Closed")
            s.close()
            print("3. Server: File Sent.")
            print("4. Client: Connection closed.\n")
            lblMessage['text'] = 'File "' + str(filename) + '" saved.'
            

            
            print(received_files)
    def on_enter1(e):
        btnConnect['background'] = 'lightblue'

    def on_leave1(e):
        btnConnect['background'] = 'SystemButtonFace'

    if __name__ == '__main__':
        lblWelcome = Label(text="Share Files")
        lblHostIp = Label(text="Host IP")
        entHostIP = Entry()
        btnConnect = Button(text="Connect", command=connect, width=10)
        lblMessage = Label(text="")

        lblWelcome.grid(row=1, column=1, columnspan=2, padx=10, pady=10)
        lblHostIp.grid(row=2, column=1, padx=10, pady=10)
        entHostIP.grid(row=2, column=2, padx=10, pady=10)
        btnConnect.grid(row=3, column=1,  columnspan=2, padx=10, pady=10)
        lblMessage.grid(row=4, column=1, columnspan=2, padx=10, pady=10)
        btnConnect.bind("<Enter>", on_enter1)
        btnConnect.bind("<Leave>", on_leave1)
        root.mainloop()

   except Exception as e:
    print("Error: " + str(e))
 
   
   

def helloCallBack3():
   root.destroy()

def helloCallBack4():
    arr = os.listdir()
    lis = ''
    for i in range(0,len(arr)):
        j = i + 1
        lis += str(j) + '. '+ arr[i] + '\n'
    messagebox.showinfo('history',lis)
    

root = tk.Tk()
root.config(bg="lightblue")
menu = Menu(root)
root.config(menu=menu) 
filemenu = Menu(menu)
helpmenu = Menu(menu) 
menu.add_cascade(label='Help', menu=helpmenu) 
helpmenu.add_command(label='propython@gmail.com')
filemenu = Menu(menu)
helpmenu = Menu(menu) 
menu.add_cascade(label='How To Share', menu=helpmenu) 
helpmenu.add_command(label='Get the host IP address from the sender and enter into the client box and click connect')
myButton = tk.Button(root,text="SEND",padx=30,pady=10,command=helloCallBack)
myButton.grid(row=8,column=7)
myButton1 = tk.Button(root,text="RECEIVE",padx=30,pady=10,command=helloCallBack1)
myButton1.grid(row=10,column=9)
myButton2 = tk.Button(root,text="HISTORY",padx=30,pady=10,command=helloCallBack4)
myButton2.grid(row=12,column=11)
myButton3 = tk.Button(root,text="Exit",padx=30,pady=10,command=helloCallBack3)
myButton3.grid(row=14,column=7)

myButton.bind("<Enter>", on_enter)
myButton.bind("<Leave>", on_leave)

myButton1.bind("<Enter>", on_enter1)
myButton1.bind("<Leave>", on_leave1)

myButton2.bind("<Enter>", on_enter2)
myButton2.bind("<Leave>", on_leave2)

myButton3.bind("<Enter>", on_enter3)
myButton3.bind("<Leave>", on_leave3)

ourMessage ='SHARE FILES'
messageVar = Message(root, text = ourMessage) 
messageVar.config(bg='lightblue',padx=20,pady=10,font='Times') 
messageVar.grid( )

root.mainloop()
