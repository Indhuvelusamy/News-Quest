import time
from bs4 import BeautifulSoup
import bs4 as bs
import requests
from easygui import passwordbox
from tkinter import *
import tkinter as tk 
import tkinter.scrolledtext as st
import sqlite3


# Login authorization
def loginauth(username, password):
    conn = sqlite3.connect('news.db')
    cursor = conn.execute("SELECT ID,PASSWORD from user")
    for x in cursor:
        #print("ID =", x[0])
        #print("NAME = ", x[1])
        if username.strip()==x[0].strip() and password.strip()==x[1].strip():
            print("Login successful")
            return 1
    return 0
    conn.close()

# Login
def login():
    flag=0
    username = input("Username: ")
    if len(username) ==0:
        print("Username can't be blank")
        flag=1
    else:
        password = passwordbox("Password")
        if len(password) == 0:
            print("Password can't be blank")
            flag=1    
    if flag==0 and loginauth(username,password):
        rl=input("Which news paper u want to scrap \n\n1.THE HINDU TAMIL\n\n2.THE INDIAN EXPRESS\n\n3.GOOGLE NEWS\n\n4.JAGRAN\n\nEnter your choice:")
        if rl == "1":
            lang=input("Choose in which area the news-paper is to be scraped \n1.INDIA\n2.SPORTS\n3.TECHNOLOGY\nEnter ur choice:");
            if lang == "3":
                page=requests.get("https://www.hindutamil.in/news/technology")
                soup=BeautifulSoup(page.text,'lxml')
                news_box=soup.find('div',attrs={'class':'col-md-9 col-lg-9'})
                all_news=news_box.find_all('a')
                c=0
                win = tk.Tk() 
                win.title("Top News")
                tk.Label(win, text = "********************தொழில்நுட்பம்********************", font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 0) 

                win.geometry('2000x4000')
                text_area = st.ScrolledText(win,width = 132,height = 30,font = ("Times New Roman",15)) 

                text_area.grid(column = 0, pady = 10, padx = 10) 

                for news in all_news:
                    c=c+1
                    text_area.insert(tk.INSERT,news.text+"\n")
                    if c==40:
                        break
                text_area.configure(state ='disabled') 
                win.mainloop()
            if lang == "1":
                page=requests.get("https://www.hindutamil.in/news/india")
                soup=BeautifulSoup(page.text,'lxml')
                news_box=soup.find('div',attrs={'class':'container tab-pane active'})
                all_news=news_box.find_all('a')
                c=0
                win = tk.Tk() 
                win.title("Top News")
                tk.Label(win, text = "********************இந்தியா********************", font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 0) 

                win.geometry('2000x4000')
                text_area = st.ScrolledText(win,width = 132,height = 30,font = ("Times New Roman",15)) 

                text_area.grid(column = 0, pady = 10, padx = 10) 

                for news in all_news:
                    c=c+1
                    text_area.insert(tk.INSERT,news.text+"\n")
                    if c==40:
                        break
                text_area.configure(state ='disabled') 
                win.mainloop()          
            if lang == "2":
                page=requests.get("https://www.hindutamil.in/news/sports")
                soup=BeautifulSoup(page.text,'lxml')
                news_box=soup.find('div',attrs={'class':'col-md-9 col-lg-9'})
                all_news=news_box.find_all('a')
                c=0
                win = tk.Tk() 
                win.title("Top News")
                tk.Label(win, text = "********************விளையாட்டு********************", font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 0) 

                win.geometry('2000x4000')
                text_area = st.ScrolledText(win,width = 132,height = 30,font = ("Times New Roman",15)) 

                text_area.grid(column = 0, pady = 10, padx = 10) 

                for news in all_news:
                    c=c+1
                    text_area.insert(tk.INSERT,news.text+"\n")
                    if c==40:
                        break
                text_area.configure(state ='disabled') 
                win.mainloop()
        elif rl == "2":
            lang=input("Choose in which area the news-paper is to be scraped \n1.SOUTH\n2.NORTH\nEnter ur choice:");
            if lang == "1":
                state=input("\n1.Chennai\n2.Bangalore\n3.Hyderabad\n")
                if state=="1":
                    page=requests.get("https://indianexpress.com/section/cities/chennai/")
                    soup=BeautifulSoup(page.text,'lxml')
                    news_box=soup.find('div',attrs={'class':'cities-stories'})
                    news_box1=soup.find('div',attrs={'class':'story'})
                    all_news=news_box.find_all('a')
                    all_news1=news_box1.find_all('img')
                    c=0
                    win = tk.Tk() 
                    win.title("Top News")
                    tk.Label(win, text = "********************CHENNAI********************", font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 0) 

                    win.geometry('2000x4000')
                    text_area = st.ScrolledText(win,width = 132,height = 30,font = ("Times New Roman",15)) 

                    text_area.grid(column = 0, pady = 10, padx = 10) 
                    for news in all_news:
                        c=c+1
                        text_area.insert(tk.INSERT,news.text+"\n")
                        if c==40:
                            break
                    text_area.configure(state ='disabled') 
                    win.mainloop()
                if state=="2":
                    page=requests.get("https://indianexpress.com/section/cities/Bangalore/")
                    soup=BeautifulSoup(page.text,'lxml')
                    news_box=soup.find('div',attrs={'class':'cities-stories'})
                    all_news=news_box.find_all('a')
                    c=0
                    win = tk.Tk()
                    win.title("Top News")
                    tk.Label(win, text = "********************BANGALORE********************", font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 0) 
                    win.geometry('2000x4000')
                    text_area = st.ScrolledText(win,width = 132,height = 30,font = ("Times New Roman",15)) 

                    text_area.grid(column = 0, pady = 10, padx = 10) 

                    for news in all_news:
                        c=c+1
                        text_area.insert(tk.INSERT,news.text+"\n")
                        if c==40:
                            break
                    text_area.configure(state ='disabled') 
                    win.mainloop()
                if state=="3":
                    page=requests.get("https://indianexpress.com/section/cities/hyderabad/")
                    soup=BeautifulSoup(page.text,'lxml')
                    news_box=soup.find('div',attrs={'class':'cities-stories'})
                    all_news=news_box.find_all('a')
                    c=0
                    win = tk.Tk() 
                    win.title("Top News")
                    tk.Label(win, text = "********************HYDERABAD********************", font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 0) 

                    win.geometry('2000x4000')
                    text_area = st.ScrolledText(win,width = 132,height = 30,font = ("Times New Roman",15)) 

                    text_area.grid(column = 0, pady = 10, padx = 10) 

                    for news in all_news:
                        c=c+1
                        text_area.insert(tk.INSERT,news.text+"\n")
                        if c==40:
                            break
                    text_area.configure(state ='disabled') 
                    win.mainloop()
            if lang == "2":
                state=input("\n1.Mumbai\n2.Pune\n3.Kolkata\n4.Delhi\n")
                if state=="1":
                    page=requests.get("https://indianexpress.com/section/cities/mumbai/")
                    soup=BeautifulSoup(page.text,'lxml')
                    news_box=soup.find('div',attrs={'class':'cities-stories'})
                    all_news=news_box.find_all('a')
                    c=0
                    win = tk.Tk() 
                    win.title("Top News")
                    tk.Label(win, text = "********************MUMBAI********************", font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 0) 

                    win.geometry('2000x4000')
                    text_area = st.ScrolledText(win,width = 132,height = 30,font = ("Times New Roman",15)) 

                    text_area.grid(column = 0, pady = 10, padx = 10) 

                    for news in all_news:
                        c=c+1
                        text_area.insert(tk.INSERT,news.text+"\n")
                        if c==40:
                            break
                    text_area.configure(state ='disabled') 
                    win.mainloop()
                if state=="2":
                    page=requests.get("https://indianexpress.com/section/cities/pune/")
                    soup=BeautifulSoup(page.text,'lxml')
                    news_box=soup.find('div',attrs={'class':'cities-stories'})
                    all_news=news_box.find_all('a')
                    c=0
                    win = tk.Tk() 
                    win.title("Top News")
                    tk.Label(win, text = "********************PUNE********************", font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 0) 

                    win.geometry('2000x4000')
                    text_area = st.ScrolledText(win,width = 132,height = 30,font = ("Times New Roman",15)) 

                    text_area.grid(column = 0, pady = 10, padx = 10) 

                    for news in all_news:
                        c=c+1
                        text_area.insert(tk.INSERT,news.text+"\n")
                        if c==40:
                            break
                    text_area.configure(state ='disabled') 
                    win.mainloop()
                if state=="3":
                    page=requests.get("https://indianexpress.com/section/cities/kolkata/")
                    soup=BeautifulSoup(page.text,'lxml')
                    news_box=soup.find('div',attrs={'class':'cities-stories'})
                    all_news=news_box.find_all('a')
                    c=0
                    win = tk.Tk() 
                    win.title("Top News")
                    tk.Label(win, text = "********************KOLKATA********************", font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 0) 

                    win.geometry('2000x4000')
                    text_area = st.ScrolledText(win,width = 132,height = 30,font = ("Times New Roman",15)) 

                    text_area.grid(column = 0, pady = 10, padx = 10) 

                    for news in all_news:
                        c=c+1
                        text_area.insert(tk.INSERT,news.text+"\n")
                        if c==40:
                            break
                    text_area.configure(state ='disabled') 
                    win.mainloop()
                if state=="4":
                    page=requests.get("https://indianexpress.com/section/cities/delhi/")
                    soup=BeautifulSoup(page.text,'lxml')
                    news_box=soup.find('div',attrs={'class':'cities-stories'})
                    all_news=news_box.find_all('a')
                    c=0
                    win = tk.Tk() 
                    win.title("Top News")
                    tk.Label(win, text = "********************DELHI********************", font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 0) 

                    win.geometry('2000x4000')
                    text_area = st.ScrolledText(win,width = 132,height = 30,font = ("Times New Roman",15)) 

                    text_area.grid(column = 0, pady = 10, padx = 10) 

                    for news in all_news:
                        c=c+1
                        text_area.insert(tk.INSERT,news.text+"\n")
                        if c==40:
                            break
                    text_area.configure(state ='disabled') 
                    win.mainloop()
        elif rl == "3":
            lang=input("Choose in which area the news-paper is to be scraped \n1.Entertainment\n2.Worldwide news\nEnter ur choice:");
            if lang == "1":
                page=requests.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNREpxYW5RU0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen")
                soup=BeautifulSoup(page.text,'lxml')
                news_box=soup.find('div',attrs={'class':'fe4pJf'})
                all_news=news_box.find_all('a')
                c=0
                win = tk.Tk() 
                win.title("Top News")
                tk.Label(win, text = "********************ENTERTAINEMENT********************", font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 0) 

                win.geometry('2000x4000')
                text_area = st.ScrolledText(win,width = 132,height = 30,font = ("Times New Roman",15)) 

                text_area.grid(column = 0, pady = 10, padx = 10) 

                for news in all_news:
                    c=c+1
                    text_area.insert(tk.INSERT,news.text+"\n")
                    if c==40:
                        break
                text_area.configure(state ='disabled') 
                win.mainloop()
            if lang == "2":
                page=requests.get("https://news.google.com/topics/CAAqJggKIiBDQkFTRWdvSUwyMHZNRGx1YlY4U0FtVnVHZ0pKVGlnQVAB?hl=en-IN&gl=IN&ceid=IN%3Aen")
                soup=BeautifulSoup(page.text,'lxml')
                news_box=soup.find('div',attrs={'class':'ajwQHc BL5WZb'})
                all_news=news_box.find_all('a')
                c=0
                win = tk.Tk() 
                win.title("Top News")
                tk.Label(win, text = "********************WORLDWIDE NEWS********************", font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 0) 

                win.geometry('2000x4000')
                text_area = st.ScrolledText(win,width = 132,height = 30,font = ("Times New Roman",15)) 

                text_area.grid(column = 0, pady = 10, padx = 10) 

                for news in all_news:
                    c=c+1
                    text_area.insert(tk.INSERT,news.text+"\n")
                    if c==40:
                        break
                text_area.configure(state ='disabled') 
                win.mainloop()
        elif rl=="4":
            page=requests.get("https://www.jagran.com/")
            soup=BeautifulSoup(page.text,'lxml')
            news_box=soup.find('ol',attrs={'class':'p1Box'})
            all_news=news_box.find_all('a')
            c=0
            win = tk.Tk() 
            win.title("Top News")
            tk.Label(win, text = "********************HINDI NEWS********************", font = ("Times New Roman", 15),background = 'green',foreground = "white").grid(column = 0, row = 0) 

            win.geometry('2000x4000')
            text_area = st.ScrolledText(win,width = 132,height = 30,font = ("Times New Roman",15)) 

            text_area.grid(column = 0, pady = 10, padx = 10) 

            for news in all_news:
                c=c+1
                text_area.insert(tk.INSERT,news.text+"\n\n\n")
                if c==50:
                    break
            text_area.configure(state ='disabled') 
            win.mainloop()
    else:
        print("Given Username or password is  not registered")

# Register
def register():
        username = input("New username: ")
        if  len(username) == 0:
            print("Username can't be blank")
        password = passwordbox("New Password")
        if  len(password) ==0:
            print("Password can't be blank")
        else:
            conn = sqlite3.connect('news.db')
            #conn.execute("DROP TABLE IF EXISTS user")
            #conn.execute("CREATE TABLE user(ID TEXT PRIMARY KEY NOT NULL,PASSWORD TEXT NOT NULL);")
            sql = "INSERT INTO user(ID,PASSWORD) \
                   values('%s','%s')"%\
                   (username,password)
            conn.execute(sql)
            time.sleep(1)
            print("Account has been created")
            conn.commit()
            conn.close()
            print("Creating account...")
            

#main program
print("\n\t\t\t\t\t\t*****WELCOME TO THE SYSTEM*****\n")
print("\n\n\t\t\t\t----------Here you can find headlines from specific areas----------\n\n Please register or login.")
print("\n  Options:\n  1.REGISTER\n  2.LOGIN\n  3.EXIT\n  Enter ur choice:")
while True:
    option = input(">>")
    if option == "1":
        register()
    elif option == "2":
        login()
    elif option == "3":
        break
    else:
        print(option + " is not an option")

# On exit
print("Shutting down...")
time.sleep(1)
