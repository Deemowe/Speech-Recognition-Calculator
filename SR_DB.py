import mysql as mysql
import speech_recognition as sr
conn = mysql.connector.connect(host="localhost", user="root", password="", database="calculator")‏


r = sr.Recognizer()
with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    print ('Done!')

text = r.recognize_google(audio)


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

print (text)

val=eval(text)

cursor = conn.cursor()
add = ("INSERT INTO Result "
       "(CalResult) "
       "VALUES (%(v)s)")

data = {
    'v': str(val)
}

cursor.execute(add, data)
conn.commit()


