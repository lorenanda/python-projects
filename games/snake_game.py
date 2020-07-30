import curses
from random import randint

#setup window
curses.initscr() #init screen
win = curses.newwin(20, 60, 0, 0) #20 rows, 60 columns (y,x)
win.keypad(1) #use arrow keys
curses.noecho()
curses.curs_set(0)
win.border(0) #draw a border
win.nodelay(1) #don't wait for the next user input

#snake and food
snake = [(4, 10), (4, 9), (4, 8)] #use a tuple because it's immutable, we don't have to change the coordinates
food = (10, 20)

win.addch(food[0], food[1], '*') #add the character for the food
#game logic
score = 0

ESC = 27 #define the esc key
key = curses.KEY_RIGHT #start by moving the snake to the right


while key != ESC:
    win.addstr(0, 2, 'Score ' + str(score) + ' ')
    win.timeout(150 - (len(snake)) // 5 + len(snake) // 10 % 120) #increase the speed when the snake gets bigger

    prev_key = key
    event = win.getch()
    key = event if event != -1 else prev_key
    
    if key not in [curses.KEY_LEFT, curses.KEY_RIGHT, curses.KEY_UP, curses.KEY_DOWN, ESC]:
        key = prev_key

#calculate the next coordinates
    y = snake[0][0]
    x = snake[0][1]
    
    if key == curses.KEY_DOWN:
        y += 1 
    if key == curses.KEY_UP:
        y -= 1 
    if key == curses.KEY_LEFT:
        x -= 1 
    if key == curses.KEY_RIGHT:
        x += 1 

    snake.insert(0, (y, x)) #O(n)

    #end game if the snake hits the border
    if y == 0:
        break
    if y == 19:
        break
    if x == 0:
        break
    if x == 59:
        break

    #end game if the snake runs over itself
    if snake[0] in snake[1:]: #if the first element of the snake is already in the snake
        break
    
    if snake[0] == food:
        score += 1 #increase the lenght
        food = ()
        while food == ():
            food = (randint(1, 18), randint(1,58))
            if food in snake:
                food = ()
        win.addch(food[0], food[1], '*')
    else:
        #move the snake
        last = snake.pop() #remove the last element/coordinate
        win.addch(last[0], last[1], ' ')
    
    win.addch(snake[0][0], snake[0][1], '#')


curses.endwin() #end the window
print(f"Final score: {score}") #keep track of score