import copy
from tkinter import *
class rubik:
  def define(self):
    self.green = ["g" for i in range(9)]
    self.white = ["w" for i in range(9)]
    self.red = ["r" for i in range(9)]
    self.yellow = ["y" for i in range(9)]
    self.blue = ["b" for i in range(9)]
    self.orange = ["o" for i in range(9)]
    #self.greenoriginal = ["g" for i in range(9)]
    #self.whiteoriginal = ["w" for i in range(9)]
    #self.redoriginal = ["r" for i in range(9)]
    #self.yelloworiginal = ["y" for i in range(9)]
    #self.blueoriginal = ["b" for i in range(9)]
    #self.orangeoriginal = ["o" for i in range(9)]
  
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
    self.blue[1] = self.blueoriginal[5] 
    self.blue[2] = self.blueoriginal[0] 
    self.blue[3] = self.blueoriginal[7] 
    self.blue[4] = self.blueoriginal[4] 
    self.blue[5] = self.blueoriginal[1] #dfdsf
    self.blue[6] = self.blueoriginal[8] 
    self.blue[7] = self.blueoriginal[3] #efdsfds
    self.blue[8] = self.blueoriginal[2] 

#note that all moves are going to be referencing the sides with white on top and red facing the user. Green on left, blue on right, red on front, orange on back, white on top and yellow on bottom. The stops are labelled left to right on the list. 

  def clear(self):
    print("""
    
    











    
    
    """)  
  def _print(self):
    self.row1 = f'   {self.white[0]}{self.white[1]}{self.white[2]}      '
    self.row2 = f'   {self.white[3]}{self.white[4]}{self.white[5]}      '
    self.row3 = f'   {self.white[6]}{self.white[7]}{self.white[8]}      '
    self.row4 = f'{self.green[0]}{self.green[1]}{self.green[2]}{self.red[0]}{self.red[1]}{self.red[2]}{self.blue[0]}{self.blue[1]}{self.blue[2]}{self.orange[0]}{self.orange[1]}{self.orange[2]}   '
    self.row5 = f'{self.green[3]}{self.green[4]}{self.green[5]}{self.red[3]}{self.red[4]}{self.red[5]}{self.blue[3]}{self.blue[4]}{self.blue[5]}{self.orange[3]}{self.orange[4]}{self.orange[5]}    '
    self.row6 = f'{self.green[6]}{self.green[7]}{self.green[8]}{self.red[6]}{self.red[7]}{self.red[8]}{self.blue[6]}{self.blue[7]}{self.blue[8]}{self.orange[6]}{self.orange[7]}{self.orange[8]}     '
    self.row7 = f'   {self.yellow[0]}{self.yellow[1]}{self.yellow[2]}'
    self.row8 = f'   {self.yellow[3]}{self.yellow[4]}{self.yellow[5]}'
    self.row9 = f'   {self.yellow[6]}{self.yellow[7]}{self.yellow[8]}'

    #print(self.row1)
    #print(self.row2)  
    #print(self.row3)
    #print(self.row4)
    #print(self.row5)
    #print(self.row6)
    #print(self.row7)
    #print(self.row8)
    #print(self.row9)
  def draw(self,root,canv):
    self.canvas = canv
    def draw_rect(row,row_num):
      row = [x for x in row]
      for i in range(len(row)):
        coords = [250+i*10, 250+row_num*10, 250+i*10-10, 250+row_num*10-10]
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
     

   
    draw_rect(self.row1, 0)
    draw_rect(self.row2, 1)
    draw_rect(self.row3, 2)
    draw_rect(self.row4, 3)
    draw_rect(self.row5, 4)
    draw_rect(self.row6, 5)
    draw_rect(self.row7, 6)
    draw_rect(self.row8, 7)
    draw_rect(self.row9, 8)
    

  

    




def main(root):
  canvas = Canvas(root,height=500,width=500)
  def move(move):
    cube.clear()
    cube.capture()
    move()
    cube._print()
  
  def prime(move):
    cube.clear()
    cube.capture()
    move()

    cube.capture()
    move()
    
    cube.capture()
    move()
    cube._print()

  cube = rubik()
  cube.clear()
  cube.define()
  cube._print()
 
  def u(event):
    
    move(cube.up)
    cube.draw(root,canvas)
  def u_prime(event):
    #technically its uprime
    prime(cube.up)
    cube.draw(root,canvas)
  
  def l(event):
    move(cube.left)
    cube.draw(root,canvas)
  def l_prime(event):
    prime(cube.left)
    cube.draw(root,canvas)
  
  def r(event):
    move(cube.right)
    cube.draw(root,canvas)
  def r_prime(event):
    prime(cube.right)
    cube.draw(root,canvas)
    
  cube.draw(root,canvas)

  root.bind('<U>', u_prime)
  root.bind('<u>', u)

  root.bind('<L>', l_prime)
  root.bind('<l>', l)

  root.bind('<R>', r_prime)
  root.bind('<r>', r)

 

 
root = Tk()
root.title('Mask Generator')
#canvas = Canvas(root,height=1000,width=1000, bg='black')
#canvas.create_rectangle([0,0,0,0], fill='black',outline="black")
#canvas.pack()
main(root)
root.mainloop()

