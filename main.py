import datetime
import os
import cv2
from ultralytics import YOLO
import matplotlib
from tkinter import *
from PIL import Image, ImageTk

# GLOBAL VARIABLES
FONT_FACE = "Helvetica Condensed"
ENTRYBOX_BG = ""
BLUE_BG = "#3A7FF6"
WHITE_BG = '#FFFFFF'
SKYBLUE = 'skyblue'
video_path = ["Data/vid1.mp4",
                  "Data/vid2.mp4",
                  "Data/vid3.mp4",
                  "Data/vid4.mp4",
                  "Data/vid5.mp4",
                  "Data/vid6.mp4",
                  "Data/vid7.mp4",
                  "Data/vid8.mp4",
                  "Data/vid9.mp4",
                  "Data/vid10.mp4",
                  "Data/vid11.mp4",
                  "Data/vid12.mp4"]

# LOADING MODEL
model = YOLO('yolov8n.pt')

root = Tk()
root.state('zoomed')
root.title("Traffic Light Optimiztion - Dashboard")



def loadVideo1():
    global video_path
    updateFrame(video_path[0],video_path[1],video_path[1],video_path[0],)


def loadVideo2():
    updateFrame(video_path[2],video_path[3],video_path[4],video_path[2],)


def loadVideo3():
    updateFrame(video_path[5],video_path[6],video_path[7],video_path[3],)


def loadVideo4():
    updateFrame(video_path[5],video_path[7],video_path[8],video_path[9],)

def loadVideo5():
    updateFrame(video_path[9],video_path[10],video_path[11],video_path[8],)



def updateFrame(f1,f2,f3,f4):

    cap1 = cv2.VideoCapture(f1)
    cap2 = cv2.VideoCapture(f2)
    cap3 = cv2.VideoCapture(f3)
    cap4 = cv2.VideoCapture(f4)

    while True:

        rat1, frame1 = cap1.read()
        rat2, frame2 = cap2.read()
        rat3, frame3 = cap3.read()
        rat4, frame4 = cap4.read()
        
        '''<--Render Frame 1-->'''
        if not rat1:
            break
        else:
            x,y = frame1.shape[:2]   
            ratio = x/y
            yy = int(ratio*y*0.8)
            xx = int(ratio*x*0.8)

            img1 = cv2.resize(frame1,(yy,xx))
            img1 = cv2.cvtColor(img1,cv2.COLOR_BGR2RGB)
            result1 = model(img1)
            for result in result1:
                # initialize the list of bounding boxes, confidences, and class IDs
                bboxes = []
                confidences = []
                class_ids = []
        
                for data in result.boxes.data.tolist():
                    x1, y1, x2, y2, confidence, class_id = data
                    x = int(x1)
                    y = int(y1)
                    w = int(x2) - int(x1)
                    h = int(y2) - int(y1)
                    class_id = int(class_id)
            
                    # filter out weak predictions by ensuring the confidence is
                    # greater than the minimum confidence
                    if confidence > 0.4 and class_id in [2,3,5,7]:
                        bboxes.append([x, y, w, h])
                        confidences.append(confidence)
                        class_ids.append(class_id)
                        cv2.rectangle(img1, (x, y), (x + w, y + h), (100, 255, 100), 2)

            img11 = Image.fromarray(img1)
            img11 = ImageTk.PhotoImage(img11)
            videoFrame1['image'] = img11
            countFrame1['text'] = "Vehicle Count\n" + str(len(bboxes))
            timeFrame1['text'] = "Estimated Time\n" + str(len(bboxes)*2.5) + "Seconds"

        '''<--Render Frame 2-->'''
        if not rat2:
            break
        else:
            x,y = frame2.shape[:2]   
            ratio = x/y
            yy = int(ratio*y*0.8)
            xx = int(ratio*x*0.8)

            img2 = cv2.resize(frame2,(yy,xx))
            img2 = cv2.cvtColor(img2,cv2.COLOR_BGR2RGB)
            result2 = model(img2)

            for result in result2:
                # initialize the list of bounding boxes, confidences, and class IDs
                bboxes = []
                confidences = []
                class_ids = []
        
                for data in result.boxes.data.tolist():
                    x1, y1, x2, y2, confidence, class_id = data
                    x = int(x1)
                    y = int(y1)
                    w = int(x2) - int(x1)
                    h = int(y2) - int(y1)
                    class_id = int(class_id)
            
                    # filter out weak predictions by ensuring the confidence is
                    # greater than the minimum confidence
                    if confidence > 0.4 and class_id in [2,3,5,7]:
                        bboxes.append([x, y, w, h])
                        confidences.append(confidence)
                        class_ids.append(class_id)
                        cv2.rectangle(img2, (x, y), (x + w, y + h), (200, 255, 0), 2)

            img22 = Image.fromarray(img2)
            img22 = ImageTk.PhotoImage(img22)
            videoFrame2['image'] = img22
            countFrame2['text'] = "Vehicle Count\n" + str(len(bboxes))
            timeFrame2['text'] = "Estimated Time\n" + str(len(bboxes)*2.5) + "Seconds"

        '''<--Render Frame 3-->'''
        if not rat3:
            break
        else:
            x,y = frame3.shape[:2]   
            ratio = x/y
            yy = int(ratio*y*0.8)
            xx = int(ratio*x*0.8)

            img3 = cv2.resize(frame3,(yy,xx))
            img3 = cv2.cvtColor(img3,cv2.COLOR_BGR2RGB)
            result3 = model(img3)
            
            for result in result3:
                # initialize the list of bounding boxes, confidences, and class IDs
                bboxes = []
                confidences = []
                class_ids = []
        
                for data in result.boxes.data.tolist():
                    x1, y1, x2, y2, confidence, class_id = data
                    x = int(x1)
                    y = int(y1)
                    w = int(x2) - int(x1)
                    h = int(y2) - int(y1)
                    class_id = int(class_id)
            
                    # filter out weak predictions by ensuring the confidence is
                    # greater than the minimum confidence
                    if confidence > 0.4 and class_id in [2,3,5,7]:
                        bboxes.append([x, y, w, h])
                        confidences.append(confidence)
                        class_ids.append(class_id)
                        cv2.rectangle(img3, (x, y), (x + w, y + h), (255, 0, 200), 2)

            img33 = Image.fromarray(img3)
            img33 = ImageTk.PhotoImage(img33)
            videoFrame3['image'] = img33
            countFrame3['text'] = "Vehicle Count\n" + str(len(bboxes))
            timeFrame3['text'] = "Estimated Time\n" + str(len(bboxes)*2.5) + "Seconds"

        '''<--Render Frame 4-->'''
        if not rat4:
            break
        else:
            x,y = frame4.shape[:2]   
            ratio = x/y
            yy = int(ratio*y*0.8)
            xx = int(ratio*x*0.8)

            img4 = cv2.resize(frame4,(yy,xx))
            img4 = cv2.cvtColor(img4,cv2.COLOR_BGR2RGB)

            result4 = model(img4)
            
            for result in result4:
                # initialize the list of bounding boxes, confidences, and class IDs
                bboxes = []
                confidences = []
                class_ids = []
        
                for data in result.boxes.data.tolist():
                    x1, y1, x2, y2, confidence, class_id = data
                    x = int(x1)
                    y = int(y1)
                    w = int(x2) - int(x1)
                    h = int(y2) - int(y1)
                    class_id = int(class_id)
            
                    # filter out weak predictions by ensuring the confidence is
                    # greater than the minimum confidence
                    if confidence > 0.4 and class_id in [2,3,5,7]:
                        bboxes.append([x, y, w, h])
                        confidences.append(confidence)
                        class_ids.append(class_id)
                        cv2.rectangle(img4, (x, y), (x + w, y + h), (255, 255, 0), 2)
                        
            img44 = Image.fromarray(img4)
            img44 = ImageTk.PhotoImage(img44)
            videoFrame4['image'] = img44
            countFrame4['text'] = "Vehicle Count\n" + str(len(bboxes))
            timeFrame4['text'] = "Estimated Time\n" + str(len(bboxes)*2.5) + "Seconds"


        root.update()

# Heading frame for adding button to add signals
headFrame = Frame(root,
                  bg = SKYBLUE,
                  height=50,
                  width=1800)
headFrame.pack()

# Button 1
loginButton1 = Button(headFrame,
                       text="Signal 1",
                       relief='flat',
                       border=0,
                       bg=BLUE_BG,
                       fg=WHITE_BG,
                       borderwidth=0,
                       command=loadVideo1,
                       font=(FONT_FACE,12))

loginButton1.place(x=30,
                y=10,
                width=100,
                height=30)


# Button 2 
loginButton2 = Button(headFrame,
                       text="Signal 2",
                       relief='flat',
                       border=0,
                       bg=BLUE_BG,
                       fg=WHITE_BG,
                       borderwidth=0,
                       command=loadVideo2,
                       font=(FONT_FACE,12))

loginButton2.place(x=160,
                y=10,
                width=100,
                height=30)


# Button 3 
loginButton2 = Button(headFrame,
                       text="Signal 3",
                       relief='flat',
                       border=0,
                       bg=BLUE_BG,
                       fg=WHITE_BG,
                       borderwidth=0,
                       command=loadVideo3,
                       font=(FONT_FACE,12))

loginButton2.place(x=290,
                y=10,
                width=100,
                height=30)


# Button 4
loginButton2 = Button(headFrame,
                       text="Signal 4",
                       relief='flat',
                       border=0,
                       bg=BLUE_BG,
                       fg=WHITE_BG,
                       borderwidth=0,
                       command=loadVideo4,
                       font=(FONT_FACE,12))

loginButton2.place(x=420,
                y=10,
                width=100,
                height=30)


# Button 5
loginButton2 = Button(headFrame,
                       text="Signal 5",
                       relief='flat',
                       border=0,
                       bg=BLUE_BG,
                       fg=WHITE_BG,
                       borderwidth=0,
                       command=loadVideo5,
                       font=(FONT_FACE,12))

loginButton2.place(x=550,
                y=10,
                width=100,
                height=30)


# Top Frame for two video frames
topFrame = Frame(root,
                  bg = WHITE_BG,
                  height=350,
                  width=1800)
topFrame.pack()

# Mid Frame for two video frames
midFrame = Frame(root,
                  bg = SKYBLUE,
                  height=50,
                  width=1800)
midFrame.pack()

# Bottom Frame for two video frames
bottomFrame = Frame(root,
                  bg = WHITE_BG,
                  height=350,
                  width=1800)
bottomFrame.pack()


'''<-- Video Frame 1 -->'''

# Video Frame 1
videoFrame1 = Label(topFrame,
                    bg=WHITE_BG)
videoFrame1.place(x=10,y=10)

# Labels Frame 1
countFrame1 = Label(topFrame,
                    bg=WHITE_BG,
                    font=(FONT_FACE,'12'),
                    text="Vehicle Count")
countFrame1.place(x=600,y=20)

timeFrame1 = Label(topFrame,
                    bg=WHITE_BG,
                    font=(FONT_FACE,'12'),
                    text="Estimated Time")
timeFrame1.place(x=600,y=65)


'''<-- Video Frame 2 -->'''

# Video Frame 2
videoFrame2 = Label(topFrame,
                    bg=WHITE_BG)
videoFrame2.place(x=930,y=10)

# Labels Frame 2
countFrame2 = Label(topFrame,
                    bg=WHITE_BG,
                    font=(FONT_FACE,'12'),
                    text="Vehicle Count")
countFrame2.place(x=810,y=20)

timeFrame2 = Label(topFrame,
                    bg=WHITE_BG,
                    font=(FONT_FACE,'12'),
                    text="Estimated Time")
timeFrame2.place(x=810,y=65)

'''<-- Video Frame 3 -->'''

# Video Frame 3
videoFrame3 = Label(bottomFrame,
                    bg=WHITE_BG)
videoFrame3.place(x=10,y=10)

# Labels Frame 3
countFrame3 = Label(bottomFrame,
                    bg=WHITE_BG,
                    font=(FONT_FACE,'12'),
                    text="Vehicle Count")
countFrame3.place(x=600,y=250)

timeFrame3 = Label(bottomFrame,
                    bg=WHITE_BG,
                    font=(FONT_FACE,'12'),
                    text="Estimated Time")
timeFrame3.place(x=600,y=295)

'''<-- Video Frame 4 -->'''

# Video Frame 4
videoFrame4 = Label(bottomFrame,
                    bg=WHITE_BG)
videoFrame4.place(x=930,y=10)

# Labels Frame 4
countFrame4 = Label(bottomFrame,
                    bg=WHITE_BG,
                    font=(FONT_FACE,'12'),
                    text="Vehicle Count")
countFrame4.place(x=810,y=250)

timeFrame4 = Label(bottomFrame,
                    bg=WHITE_BG,
                    font=(FONT_FACE,'12'),
                    text="Estimated Time")
timeFrame4.place(x=810,y=295)



root.mainloop()