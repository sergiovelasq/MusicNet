class Button:
   def __init__(self):
       self.clicked = False
   def click(self):
       self.clicked = True
 
btn = Button()
gui_framework.CreateButton().onclick(btn.click)
while not btn.clicked:
   time.sleep(0.1) # so you don't melt your computer :)


