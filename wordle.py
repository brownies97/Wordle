#Rifath Hanif

from graphics import *
import random

def main():
    
    makeWindow = GraphWin("Wordle",700,700)
    makeWindow.setBackground("lightgray")

    answer = wordsFile().strip()
    
    
    squaresArray = displaySquares(makeWindow)
    attemptCounter = 0

    user_input,enterButton = drawTextboxButton(makeWindow)
    
    while True:
        clickPoint = makeWindow.getMouse()
        if buttonClicked(clickPoint, enterButton):
            #button clicked, check word
        
            if validEntry(user_input.getText()):          #check if word valid
                #assume word is valid
                attemptCounter+=1
                ifFinished = updateBoard(user_input.getText(),squaresArray,makeWindow,
                                         attemptCounter,answer)

                if user_input.getText() == answer:
                    print("You got the answer")
                    break
                elif attemptCounter == 6:
                    break
                else: print("keep trying")
                if not ifFinished:
                    break
            else: print("Only enter 5 letter words!")
                
            
    print("GameOver")
    print(answer)
    print(answer)
    makeWindow.close()
    
def validEntry(user_input):
    list_of_words = open("list_of_words.txt","r")
    user_input = str(user_input).strip()
    if len(user_input) == 5:
        for eachWord in list_of_words:
            temp = eachWord.strip()
            if user_input == temp:
                return True
        return True
    else: 
        return False

    

def updateBoard(userInput, squaresArray, makeWindow, attemptCounter, theAnswer):
    if attemptCounter == 6:
        print("You're a loser. stahp")
        return False

    arr_of_characters = []
    for eachLetter in userInput:
        arr_of_characters.append(eachLetter)

    centerofSquares = []*5
    for eachSquare in squaresArray[attemptCounter-1]:
        centerofSquares.append(eachSquare.getCenter())
    
    for i in range(5):
        newText = Text(centerofSquares[i],arr_of_characters[i])
        newText.draw(makeWindow)

        for j in range(5):
            if arr_of_characters[i] == theAnswer[j]:
                squaresArray[attemptCounter-1][i].setFill("yellow")
                
        if arr_of_characters[i] == theAnswer[i]:
            squaresArray[attemptCounter-1][i].setFill("lightgreen")
            
    return True

def wordsFile():
    list_of_words = open("list_of_words.txt","r")
    arr_words = []
    totalWords = 0

    #put all words into an array to randomly select
    for eachWord in list_of_words:
        totalWords+=1
        arr_words.append(eachWord)
    answer = arr_words[random.randrange(1,totalWords)]
    list_of_words.close()
    return answer

def drawTextboxButton(makeWindow):
    textBox = Entry(Point(300,550),10)
    textBox.draw(makeWindow)

    enterButton = Rectangle(Point(100,540),Point(170,560))
    enterButton.setFill("silver")
    enterButton.draw(makeWindow)

    enterTextBtn = Text(Point(135,550), "Enter")
    enterTextBtn.draw(makeWindow)

    return textBox, enterButton

def buttonClicked(point, rectangle):
    """ Is point inside rectangle? """

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()

def displaySquares(makeWindow):
    squaresArray = []*5
    rows=0
    
    temp=110

    for y in range(10,510,100):
        tempArray = []*5        #create temp array
        for x in range(10,510,100):    
            newSquare = Rectangle(Point(x,y), Point(x+100,temp))
            newSquare.setFill('pink')
            newSquare.draw(makeWindow)            
            tempArray.append(newSquare)     #add row values to temp array
        
        squaresArray.append(tempArray)      #add temp array to main array
        temp+=100                           #XY coords counter // disregard

    return squaresArray                     #return 2d array of squares

    
main()
