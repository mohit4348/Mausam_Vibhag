from tkinter import *
from PIL import Image,ImageTk
import requests

# ***************************************Main window***************************************

root = Tk()

root.title("MAUSAM VIBHAG")
root.geometry("600x400")
root.minsize(600,400)
root.maxsize(600,400)
root.iconbitmap(r"C:\Users\Mohit Sharma\OneDrive\Desktop\New folder\Mausam_Vibhag\icon.ico")

# ************************************Function to print in mainbox*************************


def format_response(weather):
    try:
        Name = weather["name"]
        Country = weather["sys"]["country"]
        Condition = weather["weather"][0]["description"]
        Temperature = weather["main"]["temp"]
        Humidity = weather["main"]["humidity"]
        Wind_Speed = weather["wind"]["speed"]
        final_str = "Name:%s\nCountry:%s\nCondition:%s\nTemperature(f):%s\nHumidity:%s\nWind Speed(Km/hr):%s"%(Name,Country, Condition,Temperature,Humidity,Wind_Speed)
    except:
        final_str="Data is NOT AVAILABLE for the desired City!"
    return final_str



# *****************************************Function to get the weather details***************


def getweather(city):
    weather_key = "1d7e77c7fbda480dcf0517d3c7c2a788"
    url = "https://api.openweathermap.org/data/2.5/weather"
    parametrs = {"APPID":weather_key,"q":city,"units":"imperial"}
    respnse = requests.get(url,parametrs)

    weather = respnse.json()

    print(weather["name"])
    print(weather["sys"]["country"])
    print(weather["weather"][0]["description"])
    print(weather["main"]["temp"])
    print(weather["main"]["humidity"])
    print(weather["wind"]["speed"])
    

    label2["text"] = format_response(weather)

# **************************************For running background images************************


global my_images, count
count = -1

my_images = [
        ImageTk.PhotoImage(Image.open("1.jpg").resize((600,400))),
        ImageTk.PhotoImage(Image.open("2.jpeg").resize((600,400))),
        ImageTk.PhotoImage(Image.open("3.jpg").resize((600,400))),
        ImageTk.PhotoImage(Image.open("4.jpg").resize((600,400))),
        ImageTk.PhotoImage(Image.open("5.jpg").resize((600,400))),
        ImageTk.PhotoImage(Image.open("6.jpg").resize((600,400))),

]


my_canvas = Canvas(root,width=600,height=400,highlightthickness=0)
my_canvas.pack(fill="both",expand=True)

my_canvas.create_image(0,0, image= my_images[0],anchor = "nw")


def next():
    global count
    if count == 5:
        my_canvas.create_image(0,0, image= my_images[0],anchor = "nw")
        count = 0
    else:
        my_canvas.create_image(0,0, image= my_images[count+1],anchor = "nw")
        count += 1

        root.after(5000,next)

next()


# ************************************Label 1******************************************

label1 = Label(root,text="Please Type The Name Of Desired City!",fg="white",bg="black" ,font="comicsans 13 bold",bd=2)
label1.place(x=120,y=50)


entryframe = Frame(root,bg="black" ,bd=5)
entryframe.place(x=120,y=80,height=50,width=380)

entryfield = Entry(entryframe,bg="white",font="comicsans 20 bold")
entryfield.place(x=0,y=0,height=40,width=260)

buton = Button(entryframe,bg="skyblue",activeforeground="white",text="Get!",font="comicsansa 15 bold",command=lambda:getweather(entryfield.get()))
buton.place(x=269,y=1,width=100,height=40)


infoframe = Frame(root,bg="black" ,bd=5)
infoframe.place(x=120,y=135,height=190,width=380)

# **************************************Label 2*******************************************


label2 = Label(infoframe,font="Georgia 15",justify="left",anchor="w")
label2.place(relwidth=1,relheight=1)



root.mainloop()