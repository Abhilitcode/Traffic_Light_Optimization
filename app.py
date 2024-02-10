from tkinter import *
from PIL import Image, ImageTk


# Login Function
def login():
    if userID.get() == "123" and password.get() == "123":
        print("Login Request: Pass")
        root.destroy()
        print("Loading Dashboard...")
        import main
    else:
        print("Login Request: Error") 


# GLOBAL VARIABLES
DESCRIPTION = '''This innovative application utilizes real-time data and
advanced algorithms to optimize traffic light timings, 
reducing congestion, minimizing wait times, and improving
traffic flow. Say goodbye to frustrating gridlock and
hello to quicker, more efficient journeys with this
Traffic Light Optimization App.'''

FONT_FACE = "Helvetica Condensed"
ENTRYBOX_BG = ""
BLUE_BG = "#3A7FF6"
WHITE_BG = '#FFFFFF'

root = Tk()
root.geometry('800x550')
root.title("Login Screen")

# Main Frame 
main_frame = Frame(root)
main_frame.pack()

# Left Frame - For the Description
leftFrame = Frame(main_frame,bg=BLUE_BG,padx=10,pady=190)
leftFrame.grid(row=0,column=0)

desHeadingLabel = Label(leftFrame,
                        text="Project - Traffic Light Optimiztion",
                        fg=WHITE_BG,
                        bg=BLUE_BG,
                        font=(FONT_FACE,'16','bold'),
                        pady=10,
                        justify="left",anchor="w")
desHeadingLabel.grid(row=0,column=0,sticky=W)

desTextLabel = Label(leftFrame,
                     text=DESCRIPTION,
                     bg=BLUE_BG,
                     fg=WHITE_BG,
                     font=(FONT_FACE,'11'),
                     justify="left",anchor="w")
desTextLabel.grid(row=1,column=0,sticky=W)

desAuthorLabel = Label(leftFrame,
                       text="Project by - Abhishek",
                       bg=BLUE_BG,
                       fg=WHITE_BG,
                       font=(FONT_FACE,'11'),
                       pady=3,
                       justify="left",anchor="w")
desAuthorLabel.grid(row=2,column=0,sticky=W)

# Right Frame - For the Login Details 
rightFrame = Frame(main_frame,bg=WHITE_BG,padx=60,pady=255)
rightFrame.grid(row=0,column=1)

logLabel = Label(rightFrame,text="About the application",fg=WHITE_BG,bg=WHITE_BG,font=('','20'),padx=10,pady=10)
logLabel.pack()

userAuthLabel = Label(rightFrame,
    anchor="nw",
    text="User Authentication.",
    bg=WHITE_BG,
    fg="#4D4F7A",
    font=(FONT_FACE, 16,'bold'))

userAuthLabel.place(x=10,y=-100)

'''Entry1 - Prof Name'''

userIDLabel = Label(rightFrame,
    anchor="nw",
    text="User ID",
    bg=WHITE_BG,
    fg="#4D4F7A",
    font=(FONT_FACE, 11,'bold'))

userIDLabel.place(x=10,y=-30)

userID = StringVar()
entry_1 = Entry(
    rightFrame,
    bd=0,
    bg="#F7F7F8",
    font=(FONT_FACE,'12'),
    fg="#4D4F7A",
    highlightthickness=0,textvariable=userID,borderwidth=0)

entry_1.place(x=10,y=-5,
              width=270,height=35)


'''Entry2 - Password'''

passwordLabel = Label(rightFrame,
    anchor="nw",
    text="Password",
    bg=WHITE_BG,
    fg="#4D4F7A",
    font=(FONT_FACE, 11,'bold'))

passwordLabel.place(x=10,y=40)

password = StringVar()
passEntry = Entry(
        rightFrame,
        bd=0,
        bg="#F7F7F8",
        font=(FONT_FACE,'12'),
        fg="#4D4F7A",
        highlightthickness=0,textvariable=password,
        borderwidth=0)

passEntry.place(x=10,y=70,
              width=270,height=35)

# Login 
loginButton = Button(rightFrame,
                       text="Login",
                       relief='flat',
                       border=0,
                       bg=BLUE_BG,
                       fg="#FFFFFF",
                       borderwidth=0,
                       command=login,
                       font=(FONT_FACE,12))

loginButton.place(x=90,
                    y=150,
                    width=100,
                    height=30)

root.mainloop()
