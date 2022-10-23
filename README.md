
# Speech Recognition Calculator with Python
### What is Speech Recognition ?
Speech recognition is the ability of a machine to listen to spoken words and identify them. You can then use speech recognition in Python to convert the spoken words into text, make a request, or give a response. You can even program some devices to respond to these spoken words.

In addition:
 - Speech recognition uses computer science and linguistics to identify spoken words and convert them into text. It enables computers to understand human speech.
 - It is an important feature in several applications used such as home automation, artificial intelligence, etc.

![IMAGE1](https://user-images.githubusercontent.com/74800962/196057225-600d7b1e-516b-4733-865b-1a84f64a061a.jpg)


So the main idea and goal of our project is to recognize your voice as input to perform basic operations and display the result in a GUI computer.

### Speech Recognition Requires:
  1. Install the speech recognition package.
  2. Import the package into your Python project.
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

Wich makes retrieving the input really easy. Instead of having to create scripts from scratch to access microphones and process audio files, SpeechRecognition lets you get started in just a few minutes.

And of course, we used it in our project!


```python
import speech_recognition as sr
```
## Python GUI Programming With Tkinter

Python has a lot of GUI frameworks, but Tkinter is the only framework that's integrated with the Python standard library. Tkinter has several strengths. It's cross-platform, so the same code works on Windows, macOS and Linux. Visual elements are rendered using native operating system elements, so applications built with Tkinter look like they belong on the platform they're running on.

### How Do We Create Our Calculator Windows?
#### 1. The first and most important step is to download the Tkinter package

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
#### 3. Customize the window size, title and background 
```python
# Windows title
me.title("CALCULATOR")

# Tkinter window with dimensions 354x460
me.geometry('354x460')

# Windows background 
me.config(background='Dark gray')
```
# Object Oriented Principle
1. Set an icon for the window
we create a class that contains the creation() method to create the icon 
```python
class Image:
    def __init__(self, path):
        self.path = path

    def creaticon(self):
        # Tkinter PhotoImage method to display the icon 
        p1 = PhotoImage(file=self.path)
        # Icon set for the window
        me.iconphoto(False, p1)

```
2. Creating an object of the Image class and then calling the creation() function
```python
# path of the icon will be send throgh image class constructor 
icon = Image("1280px-Qassim_University_logo.svg.png")
icon.creaticon()
```
**Note:** The path of the image is changed according to the location of the image on your device



There is a lot of data that you can discover through this link!
[Tkinter](https://www.geeksforgeeks.org/python-gui-tkinter/)

# Import value From Another Python's File
There are two files in this project:
1. **Speech_recognition file (SR_DB)**
Which contains the evaluation expression and the database connection.

2. **GUI file (GUI)**
<br>

So we want to use the value of the **SR_DB** file, which is the result of the expression, in the **GUI** file. 
Since Python is a powerful language, we can perform this process with the statement **import**.
```python
from SR_DB import val
```

# Problem & Solution
* Expression evaluation
Since the device cannot evaluate the arithmetic expression directly like a human, several steps are required.
1. [Convert the infix expression to a postfix expression](https://favtutor.com/blogs/infix-to-postfix-conversion)
2. [Evaluating the postfix expression using the precedent of operations](https://www.geeksforgeeks.org/stack-set-4-evaluation-postfix-expression/)
<br>
At first we thought that we need to create code from these steps to get the result as in other programming languages, but as we say, Python is a powerful language that can shorten hundreds of lines with one line using the **eval() method**

```python
val=eval(text)
```

* Misunderstandings with some words
During the speech recognition process, some words are not spelled the way we expect, for example:

1. You want to say ' 1 + 1', but it is translated as 'one plus one'
2. You want to say ' 2 * 5', but it is translated as '2 X 5' 

We remind you that the **eval() method** only allows numbers and symbols as strings, so any other symbols or words are not allowed and will produce an error.
 ## replace() method
 Use the **replace() method** to ensure that the **eval() method** takes correct values

 ```python
if "multiply" in text:
    text = text.replace('multiply' , '*')
if 'divided by' in text:
    text = text.replace('divided by' , '/')
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
After calculating the result you need to store it in the database inorder to retrieve later. 
To create a connection between the MySQL database and Python, the connect() method of mysql.connector module is used. We pass the database details like HostName, username, and password in the method call, and then the method returns the connection object.

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
aadd = ("INSERT INTO Result "
       "(Expression,CalResult) "
       "VALUES (%(t)s , %(v)s)")

data = {'v': str(val),'t': str(text)}
}

cursor.execute(add, data)
conn.commit()
```
**NOTE:** By using phpMyAdmin an error may ocurr if you use the fllowing insertion statment 

```python
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
```

**Instead use a dictionary to store the value that will be inserted then us it in insert into.**

```python
val = 20
add = ("INSERT INTO Result "
       "(Expression,CalResult) "
       "VALUES (%(t)s , %(v)s)")

data = {'v': str(val),'t': str(text)}
```


## Preview 
Watch the video:
[![Watch the video](https://img.youtube.com/vi/zSu5jz465mk/maxresdefault.jpg)](https://youtu.be/zSu5jz465mk)
