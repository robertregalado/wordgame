from copyreg import pickle
from lib2to3.pgen2.token import NUMBER
import random
from tkinter.tix import TEXT
from unicodedata import category

from matplotlib.pyplot import flag
from scipy import rand
#pip install pywebio
from pywebio.input import *
from pywebio.output import *

total = 0
ppl = 0
turn = 0
plname = input("Hey! Please enter your name: ", type=TEXT)
#category = input("Bible Characters", type=TEXT)

def choose():
    '''
    words = ['notebook','computer','science','programming','mathemathics','straight',
             'repetition','reverse','juice','board','calibre','something','hazard','hesitation',
             'trouble','happiness','sprinkle']
    '''
    words = ['Joseph','Abraham','Adam','Eve','Daniel','Ezekiel','Amos','Moses','David','Solomon','Jesus Christ',
             'God','Samuel','Isaiah','Saul','Matthew','John','Abel','Cain','Nehemiah','Paul','Mark','Luke','Timothy']
    pick = random.choice(words)
    return pick

def jumble(word):
    random_word = random.sample(word,len(word)) #return list
    jumbled = ''.join(random_word) #get to string format
    return jumbled

#Function for showing your final score
def thank(pln, pl, total):
    if pl == total: #all correct answers
        put_text("\n",pln+ ', your score is :', pl, '/', total).style('color: #3e8a12; font-size: 18px')
        put_text('You seem to be genius! Well done!').style('color: #fcba03; font-size: 18px')
    if total > 3:
        if pl == (total - 1):
            put_text("\n",pln+ ', your score is :', pl, '/', total).style('color: #3e8a12; font-size: 18px')
            put_text('Ahh just short by 1! On your way to being a genius!').style('color: #fcba03; font-size:18px')
        else:
            put_text("\n",pln+ ', your score is :', pl, '/', total).style('color: #3e8a12; font-size: 18px')
            put_text('Thanks for playing!').style('color: #fcba03; font-size:18px')
    else:
        put_text("\n",pln+ ', your score is :', pl, '/', total).style('color: #3e8a12; font-size: 18px')
        put_text('Thanks for playing!').style('color: #fcba03; font-size:18px')

def play():
    global total, ppl, flag
    flag = 0
    encourage = ["Great! Next Up...", 'Well done! Coming up next...', 'Great effort! Next up...', 'Superb! Coming']
    
    for i in range(0,7):
        total += 1
        picked_word = choose()
        qn = jumble(picked_word)
        put_text("Your challenge is :", qn)
        ans = input("Your answer: ", type=TEXT)
        
        if ans == picked_word:
            ppl += 1
            e = random.choice(encourage)
            put_text("\n"+e+"\n").style('color: #02639c; font-size: 18px')
        
        else:
            put_text("Uh oh! Better luck next time...\nThe correct answer is: "+picked_word).style('color: #fc030c; font-size: 18px')
            c = input("Press 1 to continue and 0 to quit :",type=NUMBER)
            
            if c == 0:
                thank(plname,ppl, total)
                flag = 1
                break
    if flag == 0: #(User want to continue playing or (no wrong ans + 6 words over))
        cont = input("\nDo you want to continue playing?(YES/NO)", type = TEXT)
        if cont.lower() == 'yes':
            play()
            
play()
            
        
    
             