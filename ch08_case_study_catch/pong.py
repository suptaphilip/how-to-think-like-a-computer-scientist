#!/usr/bin/env python

from gasp import *

PLAYER_1_WINS = 1
PLAYER_2_WINS = 0
QUIT = -1

# def distance(x1, y1, x2, y2):
#     return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def hit(bx, by, r, px, py, h):
    """
        >>> hit(760, 100, 10, 780, 100, 100)
        False
        >>> hit(770, 100, 10, 780, 100, 100)
        True
        >>> hit(770, 200, 10, 780, 100, 100)
        False
        >>> hit(770, 210, 10, 780, 100, 100)
        False
    """
    dis_x = abs(px - bx) <= r
    dis_y = by <= (py + h / 2) and by >= (py - h / 2)
    return dis_x and dis_y

def play_round():
    ball_x = 400
    ball_y = 300
    ball = Circle((ball_x, ball_y), 10, filled=True, color=color.WHITE)
    if random_between(0, 1) == 1:
        dx = 4
    else:
        dx = -4
    dy = random_between(-5, 5)
    
    mitt1_x = 0
    mitt1_y = random_between(20, 280)
    mitt1 = Box((mitt1_x, mitt1_y), 20, 80, filled=True, color=color.BLUE)
    
    mitt2_x = 780
    mitt2_y = random_between(20, 280)
    mitt2 = Box((mitt2_x, mitt2_y), 20, 80, filled=True, color=color.RED)
    
    while True:
        if ball_y >= 590 or ball_y <= 10:
            dy *= -1
        ball_x += dx
        ball_y += dy
        if ball_x > 800:
            remove_from_screen(ball)
            remove_from_screen(mitt1)
            remove_from_screen(mitt2)
            return PLAYER_1_WINS
        elif ball_x < 0:
            remove_from_screen(ball)
            remove_from_screen(mitt1)
            remove_from_screen(mitt2)
            return PLAYER_2_WINS
        move_to(ball, (ball_x, ball_y))
        
        if key_pressed('a') and mitt1_y <= 520:
            mitt1_y += 5
        elif key_pressed('s') and mitt1_y >= 0:
            mitt1_y -= 5
        
        move_to(mitt1, (mitt1_x, mitt1_y))
        
        if key_pressed('k') and mitt2_y <= 520:
            mitt2_y += 5
        elif key_pressed('j') and mitt2_y >= 0:
            mitt2_y -= 5
        
        move_to(mitt2, (mitt2_x, mitt2_y))
        
        if key_pressed('q'):
            return QUIT
        
        # if distance(ball_x, ball_y, mitt_x, mitt_y) <= 30:
        #     remove_from_screen(ball)
        #     remove_from_screen(mitt)
        #     return PLAYER_WINS
        
        if hit(ball_x, ball_y, 20, mitt1_x, mitt1_y, 80):
            dx *= -1
        elif hit(ball_x, ball_y, 20, mitt2_x, mitt2_y,80):
            dx *= -1
        
        if ball_x >= 800:
            remove_from_screen(ball)
            remove_from_screen(mitt1)
            remove_from_screen(mitt2)
            return PLAYER_1_WINS
        elif ball_x <= 0:
            remove_from_screen(ball)
            remove_from_screen(mitt1)
            remove_from_screen(mitt2)
            return PLAYER_2_WINS
        
        update_when('next_tick')


def play_game():
    player_1_score = 0
    player_2_score = 0
    
    while True:
        p1msg = Text("Player 1: %d Points" % player_1_score, (10, 570), color=color.WHITE, size=24)
        p2msg = Text("Player 2: %d Points" % player_2_score, (540, 570), color=color.WHITE, size=24)
        sleep(3)
        remove_from_screen(p1msg)
        remove_from_screen(p2msg)
        
        result = play_round()
        
        if result == PLAYER_1_WINS:
            player_1_score += 1
        elif result == PLAYER_2_WINS:
            player_2_score += 1
        else:
            return QUIT
        
        if player_1_score == 5:
            return PLAYER_1_WINS
        elif player_2_score == 5:
            return PLAYER_2_WINS


begin_graphics(800, 600, title='Catch', background=color.BLACK)
set_speed(120)

result = play_game()

if result == PLAYER_1_WINS:
    Text("Player 1 Wins!", (340, 290), color=color.WHITE, size=32)
elif result == PLAYER_2_WINS:
    Text("Player 2 Wins!", (340, 290), color=color.WHITE, size=32)

sleep(4)

end_graphics()

