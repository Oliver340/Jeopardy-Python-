from tkinter import *
import time, random

global questionNumber
questionNumber = 1
points1 = 0
points2 = 0
multiplayer = False
dailydouble = random.randint(1,30)
dailydouble2 = random.randint(1,30)
while dailydouble == dailydouble2:
    dailydouble2 = random.randint(1,30)

print('Welcome to Jeopardy!')
print('''Type "S" to play singleplayer
Type "M" to play multiplayer''')
mode = str.lower(input())
while mode != 's' and mode != 'm':
    mode = str.lower(input())
if mode == 's':
    print('Playing singleplayer mode.')
if mode == 'm':
    multiplayer = True
    print('Playing multiplayer mode.')
root = Tk()
root.title('Jeopardy!')

def videogames200():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))
    
    x = True
    if dailydouble == 1 or dailydouble2 == 1:
        Label(text="", height=7, width=28).grid(row=1, column=0)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('This system brought Microsoft into the gaming world. It’s also considered the system with game that modernized the first person shooter game genre.')
        answer = str.lower(input())
        question = 'xbox'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
        
    print('This system brought Microsoft into the gaming world. It’s also considered the system with game that modernized the first person shooter game genre.')
    answer = str.lower(input())
    question = 'xbox'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            points1 = points1 + 200
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            points2 = points2 + 200
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 200
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 200
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=1, column=0)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def videogames400():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 2 or dailydouble2 == 2:
        Label(text="", height=7, width=28).grid(row=2, column=0)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('"Link" is the name of the main character from this classic NES game.')
        answer = str.lower(input())
        question = 'the legend of zelda'
        if answer == question or answer == 'legend of zelda':
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('"Link" is the name of the main character from this classic NES game.')
    answer = str.lower(input())
    question = 'the legend of zelda'
    if answer == question or answer == 'legend of zelda':
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 400
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 400
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 400
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 400
            print('Player Two Points: ' + str(points2))         #nice
    Label(text="", height=7, width=28).grid(row=2, column=0)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def videogames600():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 3 or dailydouble2 == 3:
        Label(text="", height=7, width=28).grid(row=3, column=0)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('Morrowind and Skyrim are iterations of this "venerable" set of games.')
        answer = str.lower(input())
        question = 'the elder scrolls'
        if answer == question or answer == 'elder scrolls':
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('Morrowind and Skyrim are iterations of this "venerable" set of games.')
    answer = str.lower(input())
    question = 'the elder scrolls'
    if answer == question or answer == 'elder scrolls':
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 600
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 600
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 600
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 600
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=3, column=0)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def videogames800():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 4 or dailydouble2 == 4:
        Label(text="", height=7, width=28).grid(row=4, column=0)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('"Put your hands together, if you want to clap. As we take you through this monkey rap!" are lyrics in a rap song by this famous ape.')
        answer = str.lower(input())
        question = 'donkey kong'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('"Put your hands together, if you want to clap. As we take you through this monkey rap!" are lyrics in a rap song by this famous ape.')
    answer = str.lower(input())
    question = 'donkey kong'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 800
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 800
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 800
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 800
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=4, column=0)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def videogames1000():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 5 or dailydouble2 == 5:
        Label(text="", height=7, width=28).grid(row=5, column=0)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('This game features a war between humans and an alien alliance known as the Covenant.')
        answer = str.lower(input())
        question = 'halo'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('This game features a war between humans and an alien alliance known as the Covenant.')
    answer = str.lower(input())
    question = 'halo'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 1000
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 1000
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 1000
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 1000
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=5, column=0)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def music200():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 6 or dailydouble2 == 6:
        Label(text="", height=7, width=28).grid(row=1, column=1)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('"Another one bites the dust" is a song from this popular music group')
        answer = str.lower(input())
        question = 'queen'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('"Another one bites the dust" is a song from this popular music group')
    answer = str.lower(input())
    question = 'queen'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 200
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 200
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 200
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 200
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=1, column=1)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def music400():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 7 or dailydouble2 == 7:
        Label(text="", height=7, width=28).grid(row=2, column=1)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('This group from Britain is considered the best-selling music group of all time')
        answer = str.lower(input())
        question = 'the beatles'
        if answer == question or answer == 'beatles':
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('This group from Britain is considered the best-selling music group of all time')
    answer = str.lower(input())
    question = 'the beatles'
    if answer == question or answer == 'beatles':
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 400
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 400
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 400
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 400
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=2, column=1)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def music600():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 8 or dailydouble2 == 8:
        Label(text="", height=7, width=28).grid(row=3, column=1)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('Beethoven, Bach, Tchaikovsky and Vivaldi are part of this genre.')
        answer = str.lower(input())
        question = 'classical'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('Beethoven, Bach, Tchaikovsky and Vivaldi are part of this genre.')
    answer = str.lower(input())
    question = 'classical'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 600
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 600
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 600
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 600
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=3, column=1)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def music800():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 9 or dailydouble2 == 9:
        Label(text="", height=7, width=28).grid(row=4, column=1)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('Lyrics from a David Bowie song include "Ground control to" this person.')
        answer = str.lower(input())
        question = 'major tom'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('Lyrics from a David Bowie song include "Ground control to" this person.')
    answer = str.lower(input())
    question = 'major tom'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 800
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 800
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 800
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 800
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=4, column=1)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def music1000():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 10 or dailydouble2 == 10:
        Label(text="", height=7, width=28).grid(row=5, column=1)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('This is the colour of a "colourful" dog in a song by Led Zeppelin')
        answer = str.lower(input())
        question = 'black'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('This is the colour of a "colourful" dog in a song by Led Zeppelin')
    answer = str.lower(input())
    question = 'black'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 1000
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 1000
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 1000
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 1000
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=5, column=1)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def science200():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 11 or dailydouble2 == 11:
        Label(text="", height=7, width=28).grid(row=1, column=2)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('This planet is the largest gas giant in our solar system.')
        answer = str.lower(input())
        question = 'jupiter'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('This planet is the largest gas giant in our solar system.')
    answer = str.lower(input())
    question = 'jupiter'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 200
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 200
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 200
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 200
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=1, column=2)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def science400():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 12 or dailydouble2 == 12:
        Label(text="", height=7, width=28).grid(row=2, column=2)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('This organelle is commonly known as the "powerhouse" of the cell')
        answer = str.lower(input())
        question = 'mitochondria'
        if answer == question or answer == 'mitochondrion':
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('This organelle is commonly known as the "powerhouse" of the cell')
    answer = str.lower(input())
    question = 'mitochondria'
    if answer == question or answer == 'mitochondrion':
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 400
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 400
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 400
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 400
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=2, column=2)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def science600():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 13 or dailydouble2 == 13:
        Label(text="", height=7, width=28).grid(row=3, column=2)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('The discovery of gravity was made in the 17th century by this physicist.')
        answer = str.lower(input())
        question = 'isaac newton'
        if answer == question or answer == 'sir isaac newton':
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('The discovery of gravity was made in the 17th century by this physicist.')
    answer = str.lower(input())
    question = 'isaac newton'
    if answer == question or answer == 'sir isaac newton':
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 600
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 600
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 600
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 600
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=3, column=2)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def science800():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 14 or dailydouble2 == 14:
        Label(text="", height=7, width=28).grid(row=4, column=2)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('6.02x10^23 is the amount of one of these units, used primarily in chemistry.')
        answer = str.lower(input())
        question = 'mol'
        if answer == question or answer == 'mols' or answer == 'mole' or answer == 'moles':
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('6.02x10^23 is the amount of one of these units, used primarily in chemistry.')
    answer = str.lower(input())
    question = 'mol'
    if answer == question or answer == 'mols' or answer == 'mole' or answer == 'moles':
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 800
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 800
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 800
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 800
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=4, column=2)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def science1000():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 15 or dailydouble2 == 15:
        Label(text="", height=7, width=28).grid(row=5, column=2)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('This (Ψ) is a greek symbol used in probability wave functions.')
        answer = str.lower(input())
        question = 'psi'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('This (Ψ) is a greek symbol used in probability wave functions.')
    answer = str.lower(input())
    question = 'psi'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 1000
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 1000
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 1000
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 1000
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=5, column=2)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def geography200():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 16 or dailydouble2 == 16:
        Label(text="", height=7, width=28).grid(row=1, column=3)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('This region, sometimes considered a continent, encompasses Australasia, Melanesia, Micronesia and Polynesia.')
        answer = str.lower(input())
        question = 'oceania'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('This region, sometimes considered a continent, encompasses Australasia, Melanesia, Micronesia and Polynesia.')
    answer = str.lower(input())
    question = 'oceania'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 200
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 200
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 200
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 200
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=1, column=3)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def geography400():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 17 or dailydouble2 == 17:
        Label(text="", height=7, width=28).grid(row=2, column=3)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('This river in northeastern Africa is the longest in the world by length')
        answer = str.lower(input())
        question = 'the nile'
        if answer == question or answer == 'nile':
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('This river in northeastern Africa is the longest in the world by length')
    answer = str.lower(input())
    question = 'the nile'
    if answer == question or answer == 'nile':
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 400
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 400
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 400
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 400
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=2, column=3)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def geography600():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 18 or dailydouble2 == 18:
        Label(text="", height=7, width=28).grid(row=3, column=3)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('This country, the fourth most populous on Earth, is made up of over 18,000 islands.')
        answer = str.lower(input())
        question = 'indonesia'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('This country, the fourth most populous on Earth, is made up of over 18,000 islands.')
    answer = str.lower(input())
    question = 'indonesia'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 600
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 600
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 600
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 600
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=3, column=3)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def geography800():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 19 or dailydouble2 == 19:
        Label(text="", height=7, width=28).grid(row=4, column=3)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('This country, bordered on three sides by France, is 2nd to Vatican City for being the smallest country in the world by area.')
        answer = str.lower(input())
        question = 'monaco'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('This country, bordered on three sides by France, is 2nd to Vatican City for being the smallest country in the world by area.')
    answer = str.lower(input())
    question = 'monaco'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 800
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 800
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 800
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 800
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=4, column=3)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def geography1000():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 20 or dailydouble2 == 20:
        Label(text="", height=7, width=28).grid(row=5, column=3)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('The national flag of this country in southern Asia is the only flag whose shape is not rectangular')
        answer = str.lower(input())
        question = 'nepal'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('The national flag of this country in southern Asia is the only flag whose shape is not rectangular')
    answer = str.lower(input())
    question = 'nepal'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 1000
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 1000
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 1000
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 1000
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=5, column=3)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def pokemon200():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 21 or dailydouble2 == 21:
        Label(text="", height=7, width=28).grid(row=1, column=4)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('In the Pokémon anime, this popular electric Pokémon given to the main character, Ash, by Professer Oak, was Ash\'s first obtained.')
        answer = str.lower(input())
        question = 'pikachu'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('In the Pokémon anime, this popular electric Pokémon given to the main character, Ash, by Professer Oak, was Ash\'s first obtained.')
    answer = str.lower(input())
    question = 'pikachu'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 200
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 200
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 200
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 200
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=1, column=4)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def pokemon400():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 22 or dailydouble2 == 22:
        Label(text="", height=7, width=28).grid(row=2, column=4)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('This pokémon with a bulb on its back has the first entry in the "Pokédex."')
        answer = str.lower(input())
        question = 'bulbasaur'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('This pokémon with a bulb on its back has the first entry in the "Pokédex."')
    answer = str.lower(input())
    question = 'bulbasaur'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 400
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 400
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 400
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 400
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=2, column=4)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def pokemon600():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 23 or dailydouble2 == 23:
        Label(text="", height=7, width=28).grid(row=3, column=4)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('The first Pokémon game created was named "Pokémon Red and" this colour.')
        answer = str.lower(input())
        question = 'blue'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('The first Pokémon game created was named "Pokémon Red and" this colour.')
    answer = str.lower(input())
    question = 'blue'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 600
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 600
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 600
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 600
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=3, column=4)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def pokemon800():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 24 or dailydouble2 == 24:
        Label(text="", height=7, width=28).grid(row=4, column=4)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('The name "Pokémon" is short for this.')
        answer = str.lower(input())
        question = 'pocket monsters'
        if answer == question or answer == 'pocket monster':
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('The name "Pokémon" is short for this.')
    answer = str.lower(input())
    question = 'pocket monsters'
    if answer == question or answer == 'pocket monster':
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 800
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 800
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 800
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 800
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=4, column=4)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def pokemon1000():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 25 or dailydouble2 == 25:
        Label(text="", height=7, width=28).grid(row=5, column=4)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('This pokémon had its skin colour changed to purple due to the backlash of its racist appearance')
        answer = str.lower(input())
        question = 'jynx'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('This pokémon had its skin colour changed to purple due to the backlash of its racist appearance')
    answer = str.lower(input())
    question = 'jynx'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 1000
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 1000
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 1000
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 1000
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=5, column=4)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def movies200():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 26 or dailydouble2 == 26:
        Label(text="", height=7, width=28).grid(row=1, column=5)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('In this movie, a timid clownfish sets out on a journey to bring home his son who has been captured.')
        answer = str.lower(input())
        question = 'finding nemo'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('In this movie, a timid clownfish sets out on a journey to bring home his son who has been captured.')
    answer = str.lower(input())
    question = 'finding nemo'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 200
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 200
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 200
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 200
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=1, column=5)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def movies400():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 27 or dailydouble2 == 27:
        Label(text="", height=7, width=28).grid(row=2, column=5)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('A blue monster and his green friend accidentally let a little girl into their city, Monstropolis, in this animated movie.')
        answer = str.lower(input())
        question = 'monsters, inc.'
        if answer == question or answer == 'monsters inc' or answer == 'monsters, inc' or answer == 'monsters inc.':
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('A blue monster and his green friend accidentally let a little girl into their city, Monstropolis, in this animated movie.')
    answer = str.lower(input())
    question = 'monsters, inc.'
    if answer == question or answer == 'monsters inc' or answer == 'monsters, inc' or answer == 'monsters inc.':
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 400
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 400
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 400
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 400
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=2, column=5)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def movies600():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 28 or dailydouble2 == 28:
        Label(text="", height=7, width=28).grid(row=3, column=5)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('This movie, the first in the Indiana Jones franchise, is the only one without "Indiana Jones" in the title.')
        answer = str.lower(input())
        question = 'raiders of the lost ark'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('This movie, the first in the Indiana Jones franchise, is the only one without "Indiana Jones" in the title.')
    answer = str.lower(input())
    question = 'raiders of the lost ark'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 600
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 600
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 600
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 600
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=3, column=5)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def movies800():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 29 or dailydouble2 == 29:
        Label(text="", height=7, width=28).grid(row=4, column=5)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('In this horror movie, a family heads to an isolated hotel for the winter where an evil and spiritual presence influences the father into violence.')
        answer = str.lower(input())
        question = 'the shining'
        if answer == question:
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('In this horror movie, a family heads to an isolated hotel for the winter where an evil and spiritual presence influences the father into violence.')
    answer = str.lower(input())
    question = 'the shining'
    if answer == question:
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 800
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 800
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 800
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 800
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=4, column=5)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
def movies1000():
    global questionNumber
    global points1
    global points2
    print('Question number: '+ str(questionNumber))

    x = True
    if dailydouble == 30 or dailydouble2 == 30:
        Label(text="", height=7, width=28).grid(row=5, column=5)
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points1:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points1 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
            while x == True:
                try:
                    print('Daily Double: How much would you like to wager?')
                    wager = int(input())
                    if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    while wager > points2:
                        print('Daily Double: Wager your score or lower')
                        wager = int(input())
                        if points2 < 1000:
                            while wager > 1000:
                                print('You can wager up to $1000')
                                wager = int(input())
                            x = False
                            break
                    x = False
                    break
                except:
                    pass
        print('In the movie "Free Willy," Willy is this type of creature.')
        answer = str.lower(input())
        question = 'killer whale'
        if answer == question or answer == 'orca':
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31] or multiplayer == False:
                points1 = points1 + wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32] and multiplayer == True:
                points2 = points2 + wager
                print('Player Two Points: ' + str(points2))
        elif answer != question:
            print('The correct answer is: ' + str(question))
            if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
                points1 = points1 - wager
                print('Player One Points: ' + str(points1))
            if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
                points2 = points2 - wager
                print('Player Two Points: ' + str(points2))
        questionNumber = questionNumber + 1
        if questionNumber >= 31 and multiplayer == True:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
            print('Player Two Points: ' + str(points2))
            if points1 > points2:
                print('Player One Wins!')
            if points1 < points2:
                print('Player Two Wins!')
            if points1 == points2:
                print('It\'s a tie!')
        elif questionNumber >= 31 and multiplayer == False:
            root.destroy()
            print('Game ended! Final Results:')
            print('Player One Points: ' + str(points1))
        return
    
    print('In the movie "Free Willy," Willy is this type of creature.')
    answer = str.lower(input())
    question = 'killer whale'
    if answer == question or answer == 'orca':
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 + 1000
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 + 1000
            print('Player Two Points: ' + str(points2))
    elif answer != question:
        print('The correct answer is: ' + str(question))
        if questionNumber in [1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31]or multiplayer == False:
            points1 = points1 - 1000
            print('Player One Points: ' + str(points1))
        if questionNumber in [2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32]and multiplayer == True:
            points2 = points2 - 1000
            print('Player Two Points: ' + str(points2))
    Label(text="", height=7, width=28).grid(row=5, column=5)
    questionNumber = questionNumber + 1
    if questionNumber >= 31 and multiplayer == True:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))
        print('Player Two Points: ' + str(points2))
        if points1 > points2:
            print('Player One Wins!')
        if points1 < points2:
            print('Player Two Wins!')
        if points1 == points2:
            print('It\'s a tie!')
    elif questionNumber >= 31 and multiplayer == False:
        root.destroy()
        print('Game ended! Final Results:')
        print('Player One Points: ' + str(points1))

Label(text="VIDEO GAMES", height=4, width=16, font=('bold', 16), fg='white', bg='mediumblue').grid(row=0, column=0)
Label(text="MUSIC", height=4, width=16, font=('bold', 16), fg='white', bg='mediumblue').grid(row=0, column=1)
Label(text="SCIENCE", height=4, width=16, font=('bold', 16), fg='white', bg='mediumblue').grid(row=0, column=2)
Label(text="GEOGRAPHY", height=4, width=16, font=('bold', 16), fg='white', bg='mediumblue').grid(row=0, column=3)
Label(text="POKÉMON", height=4, width=16, font=('bold', 16), fg='white', bg='mediumblue').grid(row=0, column=4)
Label(text="MOVIES", height=4, width=16, font=('bold', 16), fg='white', bg='mediumblue').grid(row=0, column=5)
Button(text="200", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=videogames200).grid(row=1, column=0)
Button(text="200", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=music200).grid(row=1, column=1)
Button(text="200", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=science200).grid(row=1, column=2)
Button(text="200", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=geography200).grid(row=1, column=3)
Button(text="200", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=pokemon200).grid(row=1, column=4)
Button(text="200", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=movies200).grid(row=1, column=5)
Button(text="400", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=videogames400).grid(row=2, column=0)
Button(text="400", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=music400).grid(row=2, column=1)
Button(text="400", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=science400).grid(row=2, column=2)
Button(text="400", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=geography400).grid(row=2, column=3)
Button(text="400", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=pokemon400).grid(row=2, column=4)
Button(text="400", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=movies400).grid(row=2, column=5)
Button(text="600", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=videogames600).grid(row=3, column=0)
Button(text="600", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=music600).grid(row=3, column=1)
Button(text="600", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=science600).grid(row=3, column=2)
Button(text="600", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=geography600).grid(row=3, column=3)
Button(text="600", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=pokemon600).grid(row=3, column=4)
Button(text="600", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=movies600).grid(row=3, column=5)
Button(text="800", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=videogames800).grid(row=4, column=0)
Button(text="800", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=music800).grid(row=4, column=1)
Button(text="800", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=science800).grid(row=4, column=2)
Button(text="800", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=geography800).grid(row=4, column=3)
Button(text="800", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=pokemon800).grid(row=4, column=4)
Button(text="800", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=movies800).grid(row=4, column=5)
Button(text="1000", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=videogames1000).grid(row=5, column=0)
Button(text="1000", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=music1000).grid(row=5, column=1)
Button(text="1000", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=science1000).grid(row=5, column=2)
Button(text="1000", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=geography1000).grid(row=5, column=3)
Button(text="1000", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=pokemon1000).grid(row=5, column=4)
Button(text="1000", height=4, width=16, font=('bold', 16), fg='yellow', bg='mediumblue', command=movies1000).grid(row=5, column=5)
mainloop()
