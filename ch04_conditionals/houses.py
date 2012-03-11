from gasp import *						# import everything from the gasp library

def draw_house(x, y):
    # begin_graphics()										# open the graphics canvas
    
    Box((x, y), 100, 100, filled=True, color=color.BLUE)					# the house
    Box((x + 35, y), 30, 50, filled=True, color=color.GREEN)					# the door
    Box((x + 20, y + 60), 20, 20, filled=True, color=color.YELLOW)				# the left window
    Box((x + 60, y + 60), 20, 20, filled=True, color=color.YELLOW)				# the right window
    # Line((x, y + 100), (x + 50, y + 140))							# the left roof
    # Line((x + 50, y + 140), (x + 100, y + 100))						# the right roof
    Polygon([(x, y + 100), (x + 50, y + 140), (x + 100, y + 100)], filled=True, color=color.RED)
    
    # update_when('key_pressed')								# keep the canvas open until a key is pressed
    # end_graphics()										# close the canvas (which would happen
    												# anyway, since the script ends here, but it
    												# is better to be explicit).

begin_graphics(title="Houses at Night", background=color.BLACK)

draw_house(20, 20)
draw_house(270, 20)
draw_house(520, 20)
draw_house(145, 160)
draw_house(395, 160)
draw_house(270, 320)

update_when('key_pressed')
end_graphics()

