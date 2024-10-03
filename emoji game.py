
from guizero import *
import os
from random import shuffle, randint


emojis_dir = 'emojis'

emojis = [os.path.join(emojis_dir, f) for f in os.listdir(emojis_dir) if os.path.isfile(os.path.join(emojis_dir, f))]

shuffle(emojis)



def match_emoji(matched):
    if matched:
        result.value = 'Correct'
        score.value = int(score.value) + 1
    else:
        result.value= 'Incorrect'

    setup_round()

def setup_round():
    for picture in pictures:
        picture.image = emojis.pop()
       
    for button in buttons:
        button.image = emojis.pop()
        button.update_command(match_emoji, [False])

    matched_emoji = emojis.pop()

    random_picture = randint(0,8)

    pictures[random_picture].image = matched_emoji

    random_button = randint(0,8)

    buttons[random_button].image = matched_emoji

    buttons[random_button].update_command(match_emoji, [True])


def counter():
    timer.value = int(timer.value) - 1
    if int(timer.value) == 0:
        timer.cancel(counter)
        result.value = 'Game Over'
        warn('Time Out',"You've run out of time")
        timer.value = 30
        result.value = ''
        score.value='0'
        setup_round()
        timer.repeat(1000, counter)


app = App('Emoji Match')

result = Text(app)

game_box = Box(app)

scoreboard = Box(app)

label = Text(scoreboard, text='Score', align='left')

score = Text(scoreboard, text='0', align = 'left')

pictures_box = Box(game_box, layout='grid')

buttons_box = Box(game_box,layout='grid')

buttons = []
pictures = []

for x in range(0,3):
    for y in range(0,3):
        picture = Picture(pictures_box, grid=[x,y])
        pictures.append(picture)

        button = PushButton(buttons_box, grid = [x,y])
        buttons.append(button)



extra_features = Box(app)
timer = Text(extra_features, text="Get Ready")

setup_round()

timer.value = 30
timer.repeat(1000,counter)

app.display()
