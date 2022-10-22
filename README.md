
# Speech Recognition Calculator Using Python
### What is Speech Recognition ?
Speech recognition is a machine's ability to listen to spoken words and identify them. You can then use speech recognition in Python to convert the spoken words into text, make a query or give a reply. You can even program some devices to respond to these spoken words.

In addition:
 - Speech Recognition incorporates computer science and linguistics to identify spoken words and converts them into text. It allows computers to understand human language.

-  It is an important feature in several applications used such as home automation, artificial intelligence, etc.

![IMAGE1](https://user-images.githubusercontent.com/74800962/196057225-600d7b1e-516b-4733-865b-1a84f64a061a.jpg)


So, the main idea and  goeal of our project is to recognise your voice as input to perform basic operations then show the result in GUI'S Calculator.

### Recognizing Speech Requires:
  1. Install Speech Recognition package.
  2. Import the package in your Python project.
  3. Transmit an audio input.

# Speech Recognition packages in Python
In some compilers like *intillj* you can download yours packages directly.

![IMAGE1](https://l.top4top.io/p_2486gl9i51.png)

 Or you can download them from the original source.
 
* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [apiai](https://pypi.org/project/apiai/)
* [assemblyai](https://pypi.org/project/assemblyai/)
* [google-cloud-speech](https://pypi.org/project/google-cloud-speech/)
* [pocketsphinx](https://pypi.org/project/pocketsphinx/)
* [watson-developer-cloud](https://pypi.org/project/watson-developer-cloud/)
* [wit](https://pypi.org/project/wit/)

There is one package that stands out in terms of ease-of-use: **SpeechRecognition**.

Wich makes retrieving the input really easy. Instead of having to build scripts for accessing microphones and processing audio files from scratch, SpeechRecognition will have you up and running in just a few minutes.

And of course we used it in our project!


```python
import speech_recognition as sr
```
## Python GUI Programming With Tkinter

Python has a lot of GUI frameworks, but Tkinter is the only framework that’s built into the Python standard library. Tkinter has several strengths. It’s cross-platform, so the same code works on Windows, macOS, and Linux. Visual elements are rendered using native operating system elements, so applications built with Tkinter look like they belong on the platform where they’re run.

### How We Create Our Calculator Windows?
#### 1. The first and important step is download the Tkinter package

```python
from tkinter import*
```

#### 2. Create a new window and assign it to variable
```python
# Creating tkinter window
me=Tk()

# Execute Tkinter
me.mainloop()
```
#### 3. Customize the windows size, title and background 
```python
# Windows title
me.title("CALCULATOR")

# Tkinter window with dimensions 354x460
me.geometry('354x460')

# Windows background 
me.config(background='Dark gray')
```
#### Object Oriented Principle
#### 4. Set an icon for the window
we create a class that contains creation() method to create the icon 
``` 
class Image:
    def __init__(self, path):
        self.path = path

    def creaticon(self):
        # Tkinter PhotoImage method to display the icon 
        p1 = PhotoImage(file=self.path)
        # Icon set for the window
        me.iconphoto(False, p1)

```
Creating object of class Image then calling creation() function
```
# path of the icon will be send throgh image class constructor 
icon = Image("1280px-Qassim_University_logo.svg.png")
icon.creaticon()
```
**Note:** path of the image will be changed to the path of image in your folder



There is alot of datail you can discover them using this link
[Tkinter](https://www.geeksforgeeks.org/python-gui-tkinter/)

# Import value From Another Python's File
In this project there are two files:
1. **Speech_recognition file (SR_DB)**
Wich contain the evaluation exepretion and data base connection 

2. **GUI file (GUI)**
<br>

So, we want to use the value of file **SR_DB** wich is the result of exepretion and used it in file **GUI**, because Python is powerful language we can do this process using **import** statement
```python
from SR_DB import val
```

# Problems & Solutions 
* Exepretion evaluation
Because the device cannot evaluate the arithmetic exepretion directly like human, it's requires many steps
1. [Convert the infix exepretion to  postfix exepretion](https://favtutor.com/blogs/infix-to-postfix-conversion)
2. [Evaluate the postfix exepretion usin the precedent of operations](https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/)
<br>
At first we thought that we must create code from those step to have the result like other Programming language!, but as we say Python is powerful language It can shorten hundreds of lines with one line by using **eval() method**

```python
val=eval(text)
```

* Misunderstanding some words
During speech recognition process some words don't write as we expect
for example:
1. You want to say ' 1 + 1', but it's translate as 'one plus one'
2. You want to say ' 2 * 5',  but it's translate as '2 X 5' 

We will remember you that the **eval() method** onle except numbers and symbols as string,so any other symbols or words are not allows and will produce error.
 ## replace() method
 Use **replace() method** To ensure that the **eval() method** takes correct values

 ```python
if "multiply" in text:
    text = text.replace('multiply' , '*')
if "plus" in text:
    text = text.replace('plus' , '+')
if 'X' in text:
    text = text.replace('X' , '*')
if 'x' in text:
    text = text.replace('x' , '*')
if 'minus' in text:
    text = text.replace('minus' , '-')
if 'one' in text:
    text = text.replace('one' , '1')
```


# Database Connection
After calculating result you need to store it in the database inorder to retraivet later.
To create a connection between the MySQL database and Python, the connect() method of mysql.connector module is used. We pass the database details like HostName, username, and the password in the method call, and then the method returns the connection object.

The following steps are required to connect SQL with Python:

  1- Download any local host [XAMPP](https://www.apachefriends.org/download.html) is recommended.
  
  2- Open phpMyAdmine (Make sure that you run Apache and MySQL ).
  
  <img src="https://user-images.githubusercontent.com/74800962/196057964-4ee7a88c-33af-465b-bcbb-34dbf13839ce.jpg" width="700" />

  3- Create the tables that you need via SQL tab (We create a result table to store result of calculation).
    <img width="938" alt="image" src="https://user-images.githubusercontent.com/74800962/197029250-86e19295-5ce9-4caa-86a1-c9ce73f93955.png">

  4- Connct your databse with python and write insert statment as the following code:

```python
from mysql.connector import cursor
import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root", password="", database="calculator")

cursor = conn.cursor()
add = ("INSERT INTO test "
       "(result) "
       "VALUES (%(v)s)")

data = {
    'v': str(val)
}

cursor.execute(add, data)
conn.commit()
```
**NOTE:** By using phpMyAdmin an error may ocurr if you use the fllowing insertion statment 

```sql
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
```

**Instead use a dictionary to store the value that will be inserted then us it in insert into.**

```sql
val = 20
add = ("INSERT INTO test "
       "(result) "
       "VALUES (%(v)s)")

data = {
    'v': str(val)
}
```


## Preview 
Watch the video:
[![Watch the video](https://img.youtube.com/vi/YgasSmBOFb4/maxresdefault.jpg)](https://youtu.be/YgasSmBOFb4)
