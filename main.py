import copy
from tkinter import *
import random
class rubik:
  def __init__(self,mode):
    self.mode = mode
  def define(self):
    if self.mode == "graphical":
      self.canvas = Canvas(self.root,height=500,width=500)
    self.green = ["g" for i in range(9)]
    self.white = ["w" for i in range(9)]
    self.red = ["r" for i in range(9)]
    self.yellow = ["y" for i in range(9)]
    self.blue = ["b" for i in range(9)]
    self.orange = ["o" for i in range(9)]
  def capture(self):
    self.greenoriginal = copy.copy(self.green)
    self.whiteoriginal = copy.copy(self.white)
    self.redoriginal = copy.copy(self.red)
    self.yelloworiginal = copy.copy(self.yellow)
    self.blueoriginal = copy.copy(self.blue)
    self.orangeoriginal = copy.copy(self.orange) 
  def up(self):
    self.orange[0] = self.greenoriginal[0]  
    self.orange[1] = self.greenoriginal[1]
    self.orange[2] = self.greenoriginal[2]
    self.green[0] = self.redoriginal[0]
    self.green[1] = self.redoriginal[1]
    self.green[2] = self.redoriginal[2]
    self.red[0] = self.blueoriginal[0]
    self.red[1] = self.blueoriginal[1]
    self.red[2] = self.blueoriginal[2]
    self.blue[0] = self.orangeoriginal[0]
    self.blue[1] = self.orangeoriginal[1]
    self.blue[2] = self.orangeoriginal[2]
    
    self.white[0] = self.whiteoriginal[6]
    self.white[1] = self.whiteoriginal[3]
    self.white[2] = self.whiteoriginal[0]
    self.white[3] = self.whiteoriginal[7]
    self.white[4] = self.whiteoriginal[4]
    self.white[5] = self.whiteoriginal[1]
    self.white[6] = self.whiteoriginal[8]
    self.white[7] = self.whiteoriginal[5]
    self.white[8] = self.whiteoriginal[2]
  def left(self):
    self.white[0] = self.orangeoriginal[8]
    self.white[3] = self.orangeoriginal[5]
    self.white[6] = self.orangeoriginal[2]
    self.red[0] = self.whiteoriginal[0]
    self.red[3] = self.whiteoriginal[3]
    self.red[6] = self.whiteoriginal[6]
    self.yellow[0] = self.redoriginal[0]
    self.yellow[3] = self.redoriginal[3]
    self.yellow[6] = self.redoriginal[6]
    self.orange[2] = self.yelloworiginal[6]
    self.orange[5] = self.yelloworiginal[3]
    self.orange[8] = self.yelloworiginal[0]
    
    self.green[0] = self.greenoriginal[6]
    self.green[1] = self.greenoriginal[3]
    self.green[2] = self.greenoriginal[0]
    self.green[3] = self.greenoriginal[7]
    self.green[4] = self.greenoriginal[4]
    self.green[5] = self.greenoriginal[1]
    self.green[6] = self.greenoriginal[8]
    self.green[7] = self.greenoriginal[5]
    self.green[8] = self.greenoriginal[2]
  def right(self):
    self.white[2] = self.redoriginal[2]
    self.white[5] = self.redoriginal[5]
    self.white[8] = self.redoriginal[8]
    self.red[2] = self.yelloworiginal[2]
    self.red[5] = self.yelloworiginal[5]
    self.red[8] = self.yelloworiginal[8]
    self.yellow[2] = self.orangeoriginal[6]
    self.yellow[5] = self.orangeoriginal[3]
    self.yellow[8] = self.orangeoriginal[0]
    self.orange[0] = self.whiteoriginal[8]
    self.orange[3] = self.whiteoriginal[5]
    self.orange[6] = self.whiteoriginal[2]
    
    self.blue[0] = self.blueoriginal[6] 
    self.blue[1] = self.blueoriginal[3] 
    self.blue[2] = self.blueoriginal[0] 
    self.blue[3] = self.blueoriginal[7] 
    self.blue[4] = self.blueoriginal[4] 
    self.blue[5] = self.blueoriginal[1]
    self.blue[6] = self.blueoriginal[8] 
    self.blue[7] = self.blueoriginal[5] 
    self.blue[8] = self.blueoriginal[2]
  def front(self):
    self.white[6] = self.greenoriginal[8]
    self.white[7] = self.greenoriginal[5]
    self.white[8] = self.greenoriginal[2]
    self.yellow[0] = self.blueoriginal[6]
    self.yellow[1] = self.blueoriginal[3]
    self.yellow[2] = self.blueoriginal[0]
    self.blue[0] = self.whiteoriginal[6]
    self.blue[3] = self.whiteoriginal[7]
    self.blue[6] = self.whiteoriginal [8]
    self.green[2] = self.yelloworiginal[0]
    self.green[5] = self.yelloworiginal[1]
    self.green[8] = self.yelloworiginal[2]
    
    self.red[0] = self.redoriginal[6]
    self.red[1] = self.redoriginal[3]
    self.red[2] = self.redoriginal[0]
    self.red[3] = self.redoriginal[7]
    self.red[4] = self.redoriginal[4]
    self.red[5] = self.redoriginal[1]
    self.red[6] = self.redoriginal[8]
    self.red[7] = self.redoriginal[5]
    self.red[8] = self.redoriginal[2]
  def back(self):
    self.white[0] = self.blueoriginal[2]
    self.white[1] = self.blueoriginal[5]
    self.white[2] = self.blueoriginal[8]
    self.blue[2] = self.yelloworiginal[8]
    self.blue[5] = self.yelloworiginal[7]
    self.blue[8] = self.yelloworiginal[6]
    self.green[0] = self.whiteoriginal[2]
    self.green[3] = self.whiteoriginal[1]
    self.green[6] = self.whiteoriginal[0]
    self.yellow[6] = self.greenoriginal[0]
    self.yellow[7] = self.greenoriginal[3]
    self.yellow[8] = self.greenoriginal[6]

    self.orange[0] = self.orangeoriginal[6]
    self.orange[1] = self.orangeoriginal[3]
    self.orange[2] = self.orangeoriginal[0]
    self.orange[3] = self.orangeoriginal[7]
    self.orange[4] = self.orangeoriginal[4]
    self.orange[5] = self.orangeoriginal[1]
    self.orange[6] = self.orangeoriginal[8]
    self.orange[7] = self.orangeoriginal[5]
    self.orange[8] = self.orangeoriginal[2]
  def down(self):
    self.red[6] = self.greenoriginal[6]
    self.red[7] = self.greenoriginal[7]
    self.red[8] = self.greenoriginal[8]
    self.blue[6] = self.redoriginal[6]
    self.blue[7] = self.redoriginal[7]  
    self.blue[8] = self.redoriginal[8]
    self.orange[6] = self.blueoriginal[6]
    self.orange[7] = self.blueoriginal[7]
    self.orange[8] = self.blueoriginal[8]
    self.green[6] = self.orangeoriginal[6]
    self.green[7] = self.orangeoriginal[7]
    self.green[8] = self.orangeoriginal[8]
    
    self.yellow[0] = self.yelloworiginal[6]
    self.yellow[1] = self.yelloworiginal[3]
    self.yellow[2] = self.yelloworiginal[0]
    self.yellow[3] = self.yelloworiginal[7]
    self.yellow[4] = self.yelloworiginal[4]
    self.yellow[5] = self.yelloworiginal[1]
    self.yellow[6] = self.yelloworiginal[8]
    self.yellow[7] = self.yelloworiginal[5]
    self.yellow[2] = self.yelloworiginal[2]
#note that all moves are going to be referencing the sides with white on top and red facing the user. Green on left, blue on right, red on front, orange on back, white on top and yellow on bottom. The stops are labelled left to right on the list. 
  def clear(self):
    print("""
    
    











    
    
    """)  
  def format(self):
    self.row1 = f'   {self.white[0]}{self.white[1]}{self.white[2]}      '
    self.row2 = f'   {self.white[3]}{self.white[4]}{self.white[5]}      '
    self.row3 = f'   {self.white[6]}{self.white[7]}{self.white[8]}      '
    self.row4 = f'{self.green[0]}{self.green[1]}{self.green[2]}{self.red[0]}{self.red[1]}{self.red[2]}{self.blue[0]}{self.blue[1]}{self.blue[2]}{self.orange[0]}{self.orange[1]}{self.orange[2]}   '
    self.row5 = f'{self.green[3]}{self.green[4]}{self.green[5]}{self.red[3]}{self.red[4]}{self.red[5]}{self.blue[3]}{self.blue[4]}{self.blue[5]}{self.orange[3]}{self.orange[4]}{self.orange[5]}    '
    self.row6 = f'{self.green[6]}{self.green[7]}{self.green[8]}{self.red[6]}{self.red[7]}{self.red[8]}{self.blue[6]}{self.blue[7]}{self.blue[8]}{self.orange[6]}{self.orange[7]}{self.orange[8]}     '
    self.row7 = f'   {self.yellow[0]}{self.yellow[1]}{self.yellow[2]}'
    self.row8 = f'   {self.yellow[3]}{self.yellow[4]}{self.yellow[5]}'
    self.row9 = f'   {self.yellow[6]}{self.yellow[7]}{self.yellow[8]}'
  def draw(self):
    def draw_rect(row,row_num):
      row = [x for x in row]
      for i in range(len(row)):
        coords = [180+i*15, 200+row_num*15, 180+i*15-15, 200+row_num*15-15]
        #x1, y1,x2, y2
        if row[i] == " ":
          fill = ""
          outline = ""
        if row[i] == "g":
          fill = "green"
          outline= "black"
        if row[i] == "w":
          fill = "white"
          outline="black"
        if row[i] == "r":
          fill = "red"
          outline="black"
        if row[i] == "y":
          fill = "yellow"
          outline="black"
        if row[i] == "b":
          fill = "blue"
          outline="black"
        if row[i] == "o":
          fill = "orange"
          outline="black"

        self.canvas.create_rectangle(coords, fill=fill,outline=outline)
        self.canvas.pack()
     

    if self.mode == "ai_optimized":
      print(self.row1)
      print(self.row2)
      print(self.row3)
      print(self.row4)
      print(self.row5)
      print(self.row6)
      print(self.row7)
      print(self.row8)
      print(self.row9)

    else:
      draw_rect(self.row1, 0)
      draw_rect(self.row2, 1)
      draw_rect(self.row3, 2)
      draw_rect(self.row4, 3)
      draw_rect(self.row5, 4)
      draw_rect(self.row6, 5)
      draw_rect(self.row7, 6)
      draw_rect(self.row8, 7)
      draw_rect(self.row9, 8) 
  def events(self):
    def move(move):
      self.clear()
      self.capture()
      move()
      self.format()
      self.draw()
    def prime(move):
      self.clear()
      self.capture()
      move()
      self.capture()
      move()
      self.capture()
      move()
      self.format()
      self.draw()
    def double(move):
      self.clear()
      self.capture()
      move()
      self.capture()
      move()
      self.format()
    
      
  

  #defining prime and non-prime moves
    def u(event):
      move(self.up)
    def u_prime(event):
      prime(self.up)
    def l(event):
      move(self.left) 
    def l_prime(event):
      prime(self.left)
    def r(event):
      move(self.right)  
    def r_prime(event):
      prime(self.right)
    def f(event):
      move(self.front)
    def f_prime(event):
      prime(self.front)
    def b(event):
      move(self.back)
    def b_prime(event):
      prime(self.back)
    def d(event):
      move(self.down)
    def d_prime(event):
      prime(self.down)
    def solve(event):
     #= self.clear()
      self.clear()
      self.green = ["g" for i in range(9)]
      self.white = ["w" for i in range(9)]
      self.red = ["r" for i in range(9)]
      self.yellow = ["y" for i in range(9)]
      self.blue = ["b" for i in range(9)]
      self.orange = ["o" for i in range(9)]
      self.format()
      self.draw()
    def mix(event):
      #self.clear()
      self.green = ["g" for i in range(9)]
      self.white = ["w" for i in range(9)]
      self.red = ["r" for i in range(9)]
      self.yellow = ["y" for i in range(9)]
      self.blue = ["b" for i in range(9)]
      self.orange = ["o" for i in range(9)]
      mix = []
      moves = ['u','U','l','L','r','R','f','F']
      for i in range(30):
        mix.append(moves[random.randint(0,7)])
      
      for i in mix:
        if i == "u":
          move(self.up)
        if i == "U":
          prime(self.up)
        if i == "l":
          move(self.left) 
        if i == "L":
          prime(self.left)
        if i == "r":
          move(self.right) 
        if i == "R":
          prime(self.right)
        if i == "f":
          move(self.front)
        if i == "F":
          prime(self.front)
        if i == "b":
          move(self.back)
        if i == "B":
          prime(self.back)
        if i == "d":
          move(self.down)
        if i == "D":
          prime(self.down)
  #binding moves to keys
    self.root.bind('<U>', u_prime)
    self.root.bind('<u>', u)
    self.root.bind('<L>', l_prime)
    self.root.bind('<l>', l)
    self.root.bind('<R>', r_prime)
    self.root.bind('<r>', r)
    self.root.bind('<F>',f_prime)
    self.root.bind('<f>', f)
    self.root.bind('<B>',b_prime)
    self.root.bind('<b>', b)
    self.root.bind('<d>',d)
    self.root.bind('<D>',d_prime)

    self.root.bind('<m>',mix)
    self.root.bind('<s>',solve)
         
  def main(self):
    if self.mode == "graphical":
      self.root = Tk()
      self.root.title('Rubik\'s Cube')

      self.define()
      self.format()
      self.draw()
      self.events()
      self.root.mainloop()
    if self.mode == "ai_optimized":
      self.clear()
      self.define()
      self.format()
      self.draw()
      #self.events()

def main():
  cube = rubik("graphical")
  cube.main()

#main()
