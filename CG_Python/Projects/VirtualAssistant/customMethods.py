import random
import pyqrcode
import png
import os

def rps(player1):
    player1 = input("Rock..Paper..Scissors..: ").lower().strip()
    player2 = random.choice(['Rock','Paper','Scissors']).lower()

    print(player2)

    if player1 == 'rock':
        if player2 == 'rock':
            return("Draw")
        elif player2 == 'paper':
            return("computer wins")
        elif player2 == 'scissors':
            return("player wins")

    elif player1 == 'paper':
        if player2 == 'rock':
            return("player wins")
        elif player2 == 'paper':
            return("Draw")
        elif player2 == 'scissors':
            return("computer wins")

    elif player1 == 'scissors':
        if player2 == 'rock':
            return("computer wins")
        elif player2 == 'paper':
            return("player wins")
        elif player2 == 'scissors':
            return("Draw")

    else:
        return("Invalid Input")

def qrgen(link):
    url = pyqrcode.create(link)
    url.png('myqrcode.png',scale=6)

def numgame(player1):
    player1 = int(input("Enter a number between 1 and 10: "))
    player2 = int(random.randint(1,10))

    if player1 == player2:
        return("You win!")
    elif player1 < player2:
        return("Too low! Try again.")
    else:
        return("Too high! Try again.")

def video():
    video_path = "C:/Users/vegij/Videos/movies/Se7en(1995).mp4"
    os.startfile(video_path)