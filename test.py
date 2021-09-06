#The Barcode Generator
#ALHPA STAGE
#Credits: Joseph Hutchens

#Imports
import re
import hashlib
from pathlib import Path
from barcode  import EAN13
from barcode.writer import ImageWriter
from random import randint
from datetime import date
import qrcode
from PIL import Image

#Variables
barcode=0
##########Order Number, Sha256 HASH, 12Digit Barcode
bar_info = [0,0,0]

#The Number Dictionary For English and Italian.
numbar= {
    'one':['one','uno'],
    'two':['two','dos','due'],
    'three':['three','tre','tres'],
    'four':['four','quattro','cuatro'],
    'five':['five','cinco','cinque'],
    'six':['six','seis','sei'],
    'seven':['seven','siete','sette'],
    'eight':['eight','otto','ocho'],
    'nine':['nine','nove','nueve'],
    'ten':['ten','Diez','dieci']}
numbar2= {'one':1,
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    'ten':10}

#Functions

def start():
    print("Welcome TO Barcode Generator                     ALPHA VERSION")

#GET Functions

#Finds The English/Italian Words    
def lang_numbers(word):
    if word in numbar:
        return numbar[word]
#Get Current Date
def current_date():
    today = date.today()
    return today
#Finds The Quantity Based on the Word Entered
def quantity(qty):
    if qty in numbar2:
     newqty = numbar2[qty]
     return newqty
    else:
        print("No Quantity")
#Takes A Subject Discription of The Item
def subject():
    print("Enter An Order Number.")
    disc = 'Order Number: 3959572740'
    return disc
#Using Sha256 Hash for Authenticity
#Uses The Subject
def create_hash(disc4):
    bar_hash = hashlib.sha256()
    disc5 = disc4.encode()
    bar_hash.update(disc5)
    return bar_hash.hexdigest()
#Creates a Random Number for Quantities Over 10
def create_digit(qty6):
    if qty6 > 9:
        qty6 = randint(1,8)
        return qty6
    else:
        return qty6
def create_digit12(qty6):
    digits12 = []
    digits12.append(0)
    digits12.append(randint(1,9))
    digits12.append(randint(3,6))
    digits12.append(randint(0,9))
    digits12.append(randint(1,4))
    digits12.append(randint(2,8))
    digits12.append(create_digit(qty6))
    digits12.append(randint(4,9))
    digits12.append(randint(0,1))
    digits12.append(randint(5,7))
    digits12.append(randint(0,9))
    digits12.append(randint(3,9))
    #Option Run a loop ex. loop 12times and Append randint(a,b)
    return digits12
#The Different Types Of Barcode Formats
#EAN-8
#EAN-13
#EAN-14
#UPC-A
#JAN
#ISBN-10
#ISBN-13
#ISSN
#Code 39
#Code 128
#PZN
def barcode_gen(num6):
    if num6!=0:
        path_to_file = 'barcode.png'
        path = Path(path_to_file)

        if path.is_file():
            print(f'The file {path_to_file} exists')
            print("Enter a file name: ")
            x = input()
            path_to_file = (f'barcode_{x}.png')
            with open(f'{path_to_file}', 'wb') as f:
                EAN13(num6, writer=ImageWriter()).write(f)
        else:
            print(f'The file {path_to_file} does not exist')
            print("Barcode will be created.")
            with open(f'{path_to_file}', 'wb') as f:
                EAN13(num6, writer=ImageWriter()).write(f)

def barcode_gen_qr(num7):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_H,
            box_size=10,
            border=4,
            )
        
        qr.add_data(num7)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        path_to_file = 'qrcode.png'
        path = Path(path_to_file)
        if path.is_file():
            print(f'The file {path_to_file} exists')
            print("Enter a file name: ")
            x = input()
            path_to_file = (f'qrcode_{x}.png')
            img.save(f'{path_to_file}')
        else:
            print(f'The file {path_to_file} does not exist')
            print("Barcode will be created.")
            img.save("qrcode.png")
def test(code23):
       barcode = code23
       return barcode
#Main Code
start()
print("Spell Out The Quantity Amount ")
print("Enter Q to Quit")
word = 'one'
while word != 'Q':
    #Print Out The Word
    print(lang_numbers(word))
    #Print Out The Quantity
    #print(quantity(word))
    #Print Current Date
    print(current_date())
    #Print Out New Quantity if Higher than 9
    #print(create_digit(quantity(word)))
    #Create Hash Based on Subject
    print(create_hash(subject()))
    #Create 12 Digit Number
    s = create_digit12(create_digit(quantity(word)))
    print(s)
    #Turns The 12 Digit Number to a String
    code = "".join(map(str,s))
    print(code)
    test(code)
    print("Do You want to save the 12 Digit Barcode? Y or N")
    ques109 = 'Y'
    if ques109 == 'Y':
       #Generate Barcode        
        barcode_gen(code)
        barcode_gen_qr(code)
    print("Enter Q to Quit")
    word = 'Q'
