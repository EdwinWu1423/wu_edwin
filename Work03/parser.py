from display import *
from matrix import *
from draw import *


"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    f = open(fname, 'r')
    line = f.read().split('\n')
    index = 0
    while index < len(line):
        if line[index] == "line":
            value = map(int, line[index+1].split(' '))
            add_edge(points, value[0], value[1], value[2], value[3], value[4], value[5])
            index += 2
        elif line[index] == "ident":
            ident(transform)
            index += 1
        elif line[index] == "scale":
            value = map(int, line[index +1].split(' '))
            matrix_mult(make_scale(value[0], value[1], value[2]), transform)
            index += 2
        elif line[index] == "move":
            value = map(int, line[index +1].split(' '))
            matrix_mult(make_translate(value[0], value[1], value[2]), transform,)
            index += 2
        elif line[index] =="rotate":
            value = line[index+1].split(' ')
            theta = int(value[1])
            if value[0] == "x":
                rM = make_rotX(theta)
            elif value[0] == "y":
                rM = make_rotY(theta)
            else:
                rM = make_rotZ(theta)
            matrix_mult(rM, transform)
            index += 2
        elif line[index] == "apply":
            matrix_mult(transform, points)
            for i in range(len(points)):
                intPoint = map(int, points[i])
                points[i] = intPoint
            index += 1
        elif line[index] == "display":
            clear_screen(screen)
            draw_lines(points, screen, color)
            display(screen)
            index += 1
        elif line[index] == "save":
            value = line[index+1].strip()
            clear_screen(screen)
            draw_lines(points, screen, color)
            save_extension(screen, value)
            index += 2
        else:
            index += 1
