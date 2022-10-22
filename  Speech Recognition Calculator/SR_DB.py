import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    print ('Done!')

text = r.recognize_google(audio)


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
if 'divided by' in text:
    text = text.replace('divided by' , '/')
print (text)

val=eval(text)


# import mysql.connector
# from mysql.connector import cursor
# import mysql.connector
#
# cursor = conn.cursor()
# add = ("INSERT INTO test "
#        "(result) "
#        "VALUES (%(v)s)")
#
# data = {
#     'v': str(val)
# }
#
# cursor.execute(add, data)
# conn.commit()


