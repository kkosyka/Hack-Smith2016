#Hack@Smith2016
#Kalynn Version
#in Python, using Zelle's graphic library

######################################################################################################
#
#                             LIBRARIES
#
######################################################################################################

from graphics import*
from time import sleep
import pdb

######################################################################################################
#
#                             VARIABLES
#
######################################################################################################

WIDTH = 1200
HEIGHT = 730

win = GraphWin( "HACK@SMITH - Dream Map", WIDTH, HEIGHT)

MapCSV = "smithMapHack.csv"
SmithMap = "SmithMap.gif"

######################################################################################################
#
#                             CLASSES
#
######################################################################################################

class Button:
     """Implements a button, which contains a label (text),
     is rectangular (frame), and can be clicked (True) or not clicked."""

     def __init__(self, x1, y1, w, h, text ):
          """constructor: pass (x,y) of top left corner,
          and width and height.  Pass the text displayed in
          button."""
          p1 = Point( x1, y1 )
          p2 = Point( x1+w, y1+h )
          self.frame = Rectangle( p1, p2 )
          self.label = Text(Point( x1+w//2, y1+h//2 ), text )
          self.clicked = False
        
     def draw( self, win ):
          """display button on window."""
          self.frame.draw( win )
          self.label.draw( win )

     def setFill(self, color):
          self.frame.setFill(color)

     def isClicked( self, p ):
          """Checks if p is inside the frame of the button.  Returns True
          if p inside frame, False otherwise.  If p inside, button
          changes state and color."""
          x1, y1 = self.frame.getP1().getX(), self.frame.getP1().getY()
          x2, y2 = self.frame.getP2().getX(), self.frame.getP2().getY()

          if x1 <= p.getX() <= x2 and y1 <= p.getY() <= y2:
               self.clicked = not self.clicked
               self.frame.setFill( "pale violet red" )
               sleep(0.3)
               self.frame.setFill( "pink" )

               return True
          else:
               return False

######################################################################################################
#
#                             FUNCTIONS
#
######################################################################################################

def boxes(mapLines):
     polygons = []
     for line in mapLines:
          item = (str(line)).split(",")#get rid of lines that are too short

          #used for specific lines that create more pleasing polygons

          #designating each variable
          category = ((item[0])).lower()#insignificant
          nameList2 = item[1].lower().split(' ')
          name = "".join(nameList2)
          colorList2 = item[2].lower().split(' ')
          color = "".join(colorList2)
          coordinate = item[5:-2]
          category = str(item[0])
          categoryList = str(category[0:len(category)]).lower().split(" ")
          category = "".join(categoryList)

          if color == "red":
               if name == "quad":
                    color = "lavender"
               elif name == "greenstreet":
                    color = "honeydew"
               elif name == "centercampus":
                    color = "azure"
               elif name == "upperelmstreet":
                    color = "Misty Rose"
               else:
                    color = "Light Yellow"                    
               
          polygon = []

          for x, y in zip(range(0, len(coordinate), 2), range(1, len(coordinate), 2)): #alternate the numbers so every even is x and every odd is y
               X = coordinate[x].strip() #removing any excess un-needed info
               Y = coordinate[y].strip() #removing any excess un-needed info
               points = Point(X, Y) #creating point
               polygon.append(points)#add point to polygon
          polygons.append([name, color, polygon])
          
     return polygons
     #pdb.set_trace()
     #createMap(polygons)

def createMap(polygons):
     for name, color, polygon in polygons:
          #to create the map of each item/polygon and color coding

          poly = Polygon(polygon) #objectifying the polygon
          poly.draw(win) #draw on window
          poly.setFill(color)#fill in color based on that house

def makeButtons():
     quadButton = Button(530, 75, 138, 40, "Quad")
     quadButton.setFill("pink")
     quadButton.draw(win)
     
     greenStButton = Button(205, 430, 200, 40, "Green St")
     greenStButton.setFill("pink")
     greenStButton.draw(win)

     centerCampusButton = Button(500, 385, 195, 40, "Center Campus")
     centerCampusButton.setFill("pink")
     centerCampusButton.draw(win)

     upperElmStButton = Button(518, 575, 145, 40, "Upper Elm St")
     upperElmStButton.setFill("pink")
     upperElmStButton.draw(win)

     lowerElmStButton = Button(390, 680, 100, 40, "Lower Elm St")
     lowerElmStButton.setFill("pink")
     lowerElmStButton.draw(win)

     win.setBackground("Sky Blue")
     
     border = Rectangle(Point(8,8), Point(1000-265, HEIGHT))
     border.setWidth(10)
     border.setOutline("Medium Purple")
     border.draw(win)

     #name
     enterName = Entry(Point( 880, 70 ), 35)
     enterName.setFill( "white" )
     enterName.setTextColor("black")
     enterName.draw( win )


     r1 = Rectangle( Point( 760, 10 ), Point( 995, 50 ))
     r1.draw( win )
     r1.setOutline("violet red")
     r1.setFill( "pink" )

     label1 = Text( Point( 880, 30 ), "Name or Anonymous" )
     label1.setSize(20)
     label1.draw( win )

     # user location/area
     enterLocation = Entry( Point( 880, 150), 35 )
     enterLocation.setFill( "white" )
     enterLocation.setTextColor( "black" )
     enterLocation.draw( win )


     r2 = Rectangle( Point( 760, 90 ), Point( 996, 130 ))
     r2.draw( win )
     r2.setOutline("violet red")
     r2.setFill( "pink" )

     label2 = Text( Point( 880, 110 ), "Location" )
     label2.setSize(20)
     label2.draw( win )

     # keyword
     enterKeyword = Entry( Point( 880, 230), 35 )
     enterKeyword.setFill( "white" )
     enterKeyword.setTextColor( "black" )
     enterKeyword.draw( win )

     r3 = Rectangle( Point( 760, 170 ), Point( 996, 210 ))
     r3.draw( win )
     r3.setOutline("violet red")
     r3.setFill( "pink" )

     label3 = Text( Point( 880, 190 ), "Keyword" )
     label3.setSize(20)
     label3.draw( win )

     # details of the dream
     enterDream = Entry( Point( 970, 310), 70)
     enterDream.setFill( "white" )
     enterDream.setTextColor( "black" )
     enterDream.draw( win )

     r4 = Rectangle( Point( 760, 250 ), Point( 996, 290 ))
     r4.draw( win )
     r4.setOutline("violet red")
     r4.setFill( "pink" )

     label4 = Text( Point( 880, 270 ), "Dream" )
     label4.setSize(20)
     label4.draw( win )

     # submit button that appends the data the user inputed into a list
     submit = Button( 1015, 255, 70, 30, "Submit" )
     submit.setFill("pink")
     submit.draw( win )

     seeAll = Button(1095,255,70,30, "See All")
     seeAll.setFill("pink")
     seeAll.draw(win)

     clearAll = Button(1055,220,70,30, "Clear All")
     clearAll.setFill("pink")
     clearAll.draw(win)
     
     count = 0

     userInfo = []
     while True:
          
          newInfo = []
          
          clickedPoint = win.getMouse()
 
          if submit.isClicked(clickedPoint ):
               count += 1
               #counter = Text(Point(1010 + count*9, 30),count)
               #counter.setSize(13)
 
               #counter.draw(win)
               if count == 8:
                    STOP = Circle(Point(1100, 100), 80)
                    STOP.setFill("red")
                    STOP.draw(win)
 
               
               name = enterName.getText()
               location = enterLocation.getText()
               keyword = enterKeyword.getText()
               dream = enterDream.getText()

               enterName.setText("")
               enterLocation.setText("")
               enterKeyword.setText("")
               enterDream.setText("")

               newInfo.append(name)
               newInfo.append(location)
               newInfo.append(keyword)
               newInfo.append(dream)

               name, location, keyword, dream = newInfo
               userInfo.append(name)
               userInfo.append(location)
               userInfo.append(keyword)
               userInfo.append(dream)


          name1=""
          location1 = ""
          keyword1=""
          dream1=""
          name2 = ""
          location2 = ""
          keyword2 =""
          dream2 = ""
          name3 = ""
          location3 = ""
          keyword3 = ""
          dream3 = ""
          name4 = ""
          location4 = ""
          keyword4 = ""
          dream4 = ""
          name5 = ""
          location5 = ""
          keyword5 = ""
          dream5 = ""
          name6 = ""
          location6 = ""
          keyword6 = ""
          dream6 = ""
          name7 = ""
          location7 =""
          keyword7 = ""
          dream7=""
          name8=""
          location8 = ""
          keyword8 = ""
          dream8 = ""
          
          if len(userInfo) == 4:
               print("=4")
               name1 = userInfo[0].lower()
               location1 = userInfo[1].lower()
               keyword1 = userInfo[2].lower()
               dream1 = userInfo[3].lower()

          if len(userInfo) == 8:
               print("=8")
               name1 = userInfo[0].lower()
               location1 = userInfo[1].lower()
               keyword1 = userInfo[2].lower()
               dream1 = userInfo[3].lower()

               name2 = userInfo[4].lower()
               location2 = userInfo[5].lower()
               keyword2 = userInfo[6].lower()
               dream2 = userInfo[7].lower()
               
          if len(userInfo) == 12:
               print("=12")
               name1 = userInfo[0].lower()
               location1 = userInfo[1].lower()
               keyword1 = userInfo[2].lower()
               dream1 = userInfo[3].lower()

               name2 = userInfo[4].lower()
               location2 = userInfo[5].lower()
               keyword2 = userInfo[6].lower()
               dream2 = userInfo[7].lower()

               name3 = userInfo[8].lower()
               location3 = userInfo[9].lower()
               keyword3 = userInfo[10].lower()
               dream3 = userInfo[11].lower()
               
          if len(userInfo) == 16:
               print("=16")
               name1 = userInfo[0].lower()
               location1 = userInfo[1].lower()
               keyword1 = userInfo[2].lower()
               dream1 = userInfo[3].lower()

               name2 = userInfo[4].lower()
               location2 = userInfo[5].lower()
               keyword2 = userInfo[6].lower()
               dream2 = userInfo[7].lower()

               name3 = userInfo[8].lower()
               location3 = userInfo[9].lower()
               keyword3 = userInfo[10].lower()
               dream3 = userInfo[11].lower()

               name4 = userInfo[12].lower()
               location4 = userInfo[13].lower()
               keyword4 = userInfo[14].lower()
               dream4 = userInfo[15].lower()

          if len(userInfo) == 20:
               print("=20")
               name1 = userInfo[0].lower()
               location1 = userInfo[1].lower()
               keyword1 = userInfo[2].lower()
               dream1 = userInfo[3].lower()

               name2 = userInfo[4].lower()
               location2 = userInfo[5].lower()
               keyword2 = userInfo[6].lower()
               dream2 = userInfo[7].lower()

               name3 = userInfo[8].lower()
               location3 = userInfo[9].lower()
               keyword3 = userInfo[10].lower()
               dream3 = userInfo[11].lower()

               name4 = userInfo[12].lower()
               location4 = userInfo[13].lower()
               keyword4 = userInfo[14].lower()
               dream4 = userInfo[15].lower()

               name5 = userInfo[16].lower()
               location5 = userInfo[17].lower()
               keyword5 = userInfo[18].lower()
               dream5 = userInfo[19].lower()

          if len(userInfo) == 24:
               print("=24")
               name1 = userInfo[0].lower()
               location1 = userInfo[1].lower()
               keyword1 = userInfo[2].lower()
               dream1 = userInfo[3].lower()

               name2 = userInfo[4].lower()
               location2 = userInfo[5].lower()
               keyword2 = userInfo[6].lower()
               dream2 = userInfo[7].lower()

               name3 = userInfo[8].lower()
               location3 = userInfo[9].lower()
               keyword3 = userInfo[10].lower()
               dream3 = userInfo[11].lower()

               name4 = userInfo[12].lower()
               location4 = userInfo[13].lower()
               keyword4 = userInfo[14].lower()
               dream4 = userInfo[15].lower()

               name5 = userInfo[16].lower()
               location5 = userInfo[17].lower()
               keyword5 = userInfo[18].lower()
               dream5 = userInfo[19].lower()

               name6 = userInfo[20].lower()
               location6 = userInfo[21].lower()
               keyword6 = userInfo[22].lower()
               dream6 = userInfo[23].lower()


          if len(userInfo) == 28:
               print("=28")
               name1 = userInfo[0].lower()
               location1 = userInfo[1].lower()
               keyword1 = userInfo[2].lower()
               dream1 = userInfo[3].lower()

               name2 = userInfo[4].lower()
               location2 = userInfo[5].lower()
               keyword2 = userInfo[6].lower()
               dream2 = userInfo[7].lower()

               name3 = userInfo[8].lower()
               location3 = userInfo[9].lower()
               keyword3 = userInfo[10].lower()
               dream3 = userInfo[11].lower()

               name4 = userInfo[12].lower()
               location4 = userInfo[13].lower()
               keyword4 = userInfo[14].lower()
               dream4 = userInfo[15].lower()

               name5 = userInfo[16].lower()
               location5 = userInfo[17].lower()
               keyword5 = userInfo[18].lower()
               dream5 = userInfo[19].lower()

               name6 = userInfo[20].lower()
               location6 = userInfo[21].lower()
               keyword6 = userInfo[22].lower()
               dream6 = userInfo[23].lower()

               name7 = userInfo[24].lower()
               location7 = userInfo[25].lower()
               keyword7 = userInfo[26].lower()
               dream7 = userInfo[27].lower()

          if len(userInfo) == 32:
               print("=32")
               name1 = userInfo[0].lower()
               location1 = userInfo[1].lower()
               keyword1 = userInfo[2].lower()
               dream1 = userInfo[3].lower()

               name2 = userInfo[4].lower()
               location2 = userInfo[5].lower()
               keyword2 = userInfo[6].lower()
               dream2 = userInfo[7].lower()

               name3 = userInfo[8].lower()
               location3 = userInfo[9].lower()
               keyword3 = userInfo[10].lower()
               dream3 = userInfo[11].lower()

               name4 = userInfo[12].lower()
               location4 = userInfo[13].lower()
               keyword4 = userInfo[14].lower()
               dream4 = userInfo[15].lower()

               name5 = userInfo[16].lower()
               location5 = userInfo[17].lower()
               keyword5 = userInfo[18].lower()
               dream5 = userInfo[19].lower()

               name6 = userInfo[20].lower()
               location6 = userInfo[21].lower()
               keyword6 = userInfo[22].lower()
               dream6 = userInfo[23].lower()

               name7 = userInfo[24].lower()
               location7 = userInfo[25].lower()
               keyword7 = userInfo[26].lower()
               dream7 = userInfo[27].lower()

               name8 = userInfo[28].lower()
               location8 = userInfo[29].lower()
               keyword8 = userInfo[30].lower()
               dream8 = userInfo[31].lower()

               
          if quadButton.isClicked(clickedPoint): # if exit click, stop loop
               print(location2)
               if location1 == "quad":
                    text1 = Text(Point(990,335),(name1, "Quad"))
                    text1a = Text(Point(990,350), keyword1)
                    text1b = Text(Point(990,365), dream1)
                    text1.draw(win)
                    text1a.draw(win)
                    text1b.draw(win)
                    
               if location2 == "quad":
                    text2 = Text(Point(990,385),(name2, "Quad"))
                    text2a = Text(Point(990,400), keyword2)
                    text2b = Text(Point(990,415), dream2)
                    text2.draw(win)
                    text2a.draw(win)
                    text2b.draw(win)
                    
               if location3 == "quad":
                    text3 = Text(Point(990,435),(name3, "Quad"))
                    text3a = Text(Point(990,450), keyword3)
                    text3b = Text(Point(990,465), dream3)
                    text3.draw(win)
                    text3a.draw(win)
                    text3b.draw(win)
                    
               if location4 == "quad":
                    text4 = Text(Point(990,485),(name4, "Quad"))
                    text4a = Text(Point(990,500), keyword4)
                    text4b = Text(Point(990,515), dream4)
                    text4.draw(win)
                    text4a.draw(win)
                    text4b.draw(win)
                    
               if location5 == "quad":
                    text5 = Text(Point(990,535),(name5, "Quad"))
                    text5a = Text(Point(990,550), keyword5)
                    text5b = Text(Point(990,565), dream5)
                    text5.draw(win)
                    text5a.draw(win)
                    text5b.draw(win)
                    
               if location6 == "quad":
                    text6 = Text(Point(990,585),(name6, "Quad"))
                    text6a = Text(Point(990,600), keyword6)
                    text6b = Text(Point(990,615), dream6)
                    text6.draw(win)
                    text6a.draw(win)
                    text6b.draw(win)
                    
               if location7 == "quad":
                    text7 = Text(Point(990,635),(name7, "Quad"))
                    text7a = Text(Point(990,650), keyword7)
                    text7b = Text(Point(990,665), dream7)
                    text7.draw(win)
                    text7a.draw(win)
                    text7b.draw(win)
                    
               if location8 == "quad":
                    text8 = Text(Point(990,685),(name8, "Quad"))
                    text8a = Text(Point(990,700), keyword8)
                    text8b = Text(Point(990,715), dream8)
                    text8.draw(win)
                    text8a.draw(win)
                    text8b.draw(win)
                    
               continue

          if greenStButton.isClicked(clickedPoint):
               if location1 == "greenst" or location1 == "green st":
                    text1 = Text(Point(990,335),(name1, "Green St"))
                    text1a = Text(Point(990,350), keyword1)
                    text1b = Text(Point(990,365), dream1)
                    text1.draw(win)
                    text1a.draw(win)
                    text1b.draw(win)
                    
               if location2 == "greenst" or location2 == "green st":
                    text2 = Text(Point(990,385),(name2, "Green St"))
                    text2a = Text(Point(990,400), keyword2)
                    text2b = Text(Point(990,415), dream2)
                    text2.draw(win)
                    text2a.draw(win)
                    text2b.draw(win)
                    
               if location3 == "green st" or location3 == "green st":
                    text3 = Text(Point(990,435),(name3, "Green St"))
                    text3a = Text(Point(990,450), keyword3)
                    text3b = Text(Point(990,465), dream3)
                    text3.draw(win)
                    text3a.draw(win)
                    text3b.draw(win)
                    
               if location4 == "greenst" or location4 == "green st":
                    text4 = Text(Point(990,485),(name4, "Green St"))
                    text4a = Text(Point(990,500), keyword4)
                    text4b = Text(Point(990,515), dream4)
                    text4.draw(win)
                    text4a.draw(win)
                    text4b.draw(win)
                    
               if location5 == "greenst" or location5 == "green st":
                    text5 = Text(Point(990,535),(name5, "Green St"))
                    text5a = Text(Point(990,550), keyword5)
                    text5b = Text(Point(990,565), dream5)
                    text5.draw(win)
                    text5a.draw(win)
                    text5b.draw(win)
                    
               if location6 == "greenst" or location6 == "green st":
                    text6 = Text(Point(990,585),(name6, "Green St"))
                    text6a = Text(Point(990,600), keyword6)
                    text6b = Text(Point(990,615), dream6)
                    text6.draw(win)
                    text6a.draw(win)
                    text6b.draw(win)
                    
               if location7 == "greenst" or location7 == "green st":
                    text7 = Text(Point(990,635),(name7, "Green St"))
                    text7a = Text(Point(990,650), keyword7)
                    text7b = Text(Point(990,665), dream7)
                    text7.draw(win)
                    text7a.draw(win)
                    text7b.draw(win)
                    
               if location8 == "greenst" or location8 == "green st":
                    text8 = Text(Point(990,685),(name8, "Green St"))
                    text8a = Text(Point(990,700), keyword8)
                    text8b = Text(Point(990,715), dream8)
                    text8.draw(win)
                    text8a.draw(win)
                    text8b.draw(win)
                    
                    
               continue
          
          if centerCampusButton.isClicked(clickedPoint):
               if location1 == "centercampus" or location1 == "center campus":
                    text1 = Text(Point(990,335),(name1, "Center Campus"))
                    text1a = Text(Point(990,350), keyword1)
                    text1b = Text(Point(990,365), dream1)
                    text1.draw(win)
                    text1a.draw(win)
                    text1b.draw(win)
                    
               if location2 == "centercampus" or location2 == "center campus":
                    text2 = Text(Point(990,385),(name2, "Center Campus"))
                    text2a = Text(Point(990,400), keyword2)
                    text2b = Text(Point(990,415), dream2)
                    text2.draw(win)
                    text2a.draw(win)
                    text2b.draw(win)
                    
               if location3 == "centercampus" or location3 == "center campus":
                    text3 = Text(Point(990,435),(name3, "Center Campus"))
                    text3a = Text(Point(990,450), keyword3)
                    text3b = Text(Point(990,465), dream3)
                    text3.draw(win)
                    text3a.draw(win)
                    text3b.draw(win)
                    
               if location4 == "centercampus" or location4 == "center campus":
                    text4 = Text(Point(990,485),(name4, "Center Campus"))
                    text4a = Text(Point(990,500), keyword4)
                    text4b = Text(Point(990,515), dream4)
                    text4.draw(win)
                    text4a.draw(win)
                    text4b.draw(win)
                    
               if location5 == "centercampus" or location5 == "center campus":
                    text5 = Text(Point(990,535),(name5, "Center Campus"))
                    text5a = Text(Point(990,550), keyword5)
                    text5b = Text(Point(990,565), dream5)
                    text5.draw(win)
                    text5a.draw(win)
                    text5b.draw(win)
                    
               if location6 == "centercampus" or location6 == "center campus":
                    text6 = Text(Point(990,585),(name6, "Center Campus"))
                    text6a = Text(Point(990,600), keyword6)
                    text6b = Text(Point(990,615), dream6)
                    text6.draw(win)
                    text6a.draw(win)
                    text6b.draw(win)
                    
               if location7 == "centercampus" or location7 == "center campus":
                    text7 = Text(Point(990,635),(name7, "Center Campus"))
                    text7a = Text(Point(990,650), keyword7)
                    text7b = Text(Point(990,665), dream7)
                    text7.draw(win)
                    text7a.draw(win)
                    text7b.draw(win)
                    
               if location8 == "centercampus" or location8 == "center campus":
                    text8 = Text(Point(990,685),(name8, "Center Campus"))
                    text8a = Text(Point(990,700), keyword8)
                    text8b = Text(Point(990,715), dream8)
                    text8.draw(win)
                    text8a.draw(win)
                    text8b.draw(win)
                    
               continue
          
          if upperElmStButton.isClicked(clickedPoint):
               if location1 == "upperelmst" or location1 == "upper elm st":
                    text1 = Text(Point(990,335),(name1, "Upper Elm St"))
                    text1a = Text(Point(990,350), keyword1)
                    text1b = Text(Point(990,365), dream1)
                    text1.draw(win)
                    text1a.draw(win)
                    text1b.draw(win)
                    
               if location2 == "upperelmst" or location2 == "upper elm st":
                    text2 = Text(Point(990,385),(name2, "Upper Elm St"))
                    text2a = Text(Point(990,400), keyword2)
                    text2b = Text(Point(990,415), dream2)
                    text2.draw(win)
                    text2a.draw(win)
                    text2b.draw(win)
                    
               if location3 == "upperelmst" or location3 == "upper elm st":
                    text3 = Text(Point(990,435),(name3, "Upper Elm St"))
                    text3a = Text(Point(990,450), keyword3)
                    text3b = Text(Point(990,465), dream3)
                    text3.draw(win)
                    text3a.draw(win)
                    text3b.draw(win)
                    
               if location4 == "upperelmst" or location4 == "upper elm st":
                    text4 = Text(Point(990,485),(name4, "Upper Elm St"))
                    text4a = Text(Point(990,500), keyword4)
                    text4b = Text(Point(990,515), dream4)
                    text4.draw(win)
                    text4a.draw(win)
                    text4b.draw(win)
                    
               if location5 == "upperelmst" or location5 == "upper elm st":
                    text5 = Text(Point(990,535),(name5, "Upper Elm St"))
                    text5a = Text(Point(990,550), keyword5)
                    text5b = Text(Point(990,565), dream5)
                    text5.draw(win)
                    text5a.draw(win)
                    text5b.draw(win)
                    
               if location6 == "upperelmst" or location6 == "upper elm st":
                    text6 = Text(Point(990,585),(name6, "Upper Elm St"))
                    text6a = Text(Point(990,600), keyword6)
                    text6b = Text(Point(990,615), dream6)
                    text6.draw(win)
                    text6a.draw(win)
                    text6b.draw(win)
                    
               if location7 == "upperelmst" or location7 == "upper elm st":
                    text7 = Text(Point(990,635),(name7, "Upper Elm St"))
                    text7a = Text(Point(990,650), keyword7)
                    text7b = Text(Point(990,665), dream7)
                    text7.draw(win)
                    text7a.draw(win)
                    text7b.draw(win)
                    
               if location8 == "upperelmst" or location8 == "upper elm st":
                    text8 = Text(Point(990,685),(name8, "Upper Elm St"))
                    text8a = Text(Point(990,700), keyword8)
                    text8b = Text(Point(990,715), dream8)
                    text8.draw(win)
                    text8a.draw(win)
                    text8b.draw(win)
                    
               continue
    
          
          if lowerElmStButton.isClicked(clickedPoint):
               if location1 == "lowerelmst" or location1 == "lower elm st":
                    text1 = Text(Point(990,335),(name1, "Lower Elm St"))
                    text1a = Text(Point(990,350), keyword1)
                    text1b = Text(Point(990,365), dream1)
                    text1.draw(win)
                    text1a.draw(win)
                    text1b.draw(win)
                    
               if location2 == "lowerelmst" or location2 == "lower elm st":
                    text2 = Text(Point(990,385),(name2, "Lower Elm St"))
                    text2a = Text(Point(990,400), keyword2)
                    text2b = Text(Point(990,415), dream2)
                    text2.draw(win)
                    text2a.draw(win)
                    text2b.draw(win)
                    
               if location3 == "lowerelmst" or location3 == "lower elm st":
                    text3 = Text(Point(990,435),(name3, "Lower Elm St"))
                    text3a = Text(Point(990,450), keyword3)
                    text3b = Text(Point(990,465), dream3)
                    text3.draw(win)
                    text3a.draw(win)
                    text3b.draw(win)
                    
               if location4 == "lowerelmst" or location4== "lower elm st":
                    text4 = Text(Point(990,485),(name4, "Lower Elm St"))
                    text4a = Text(Point(990,500), keyword4)
                    text4b = Text(Point(990,515), dream4)
                    text4.draw(win)
                    text4a.draw(win)
                    text4b.draw(win)
                    
               if location5 == "lowerelmst" or location5 == "lower elm st":
                    text5 = Text(Point(990,535),(name5, "Lower Elm St"))
                    text5a = Text(Point(990,550), keyword5)
                    text5b = Text(Point(990,565), dream5)
                    text5.draw(win)
                    text5a.draw(win)
                    text5b.draw(win)
                    
               if location6 == "lowerelmst" or location6 == "lower elm st":
                    text6 = Text(Point(990,585),(name6, "Lower Elm St"))
                    text6a = Text(Point(990,600), keyword6)
                    text6b = Text(Point(990,615), dream6)
                    text6.draw(win)
                    text6a.draw(win)
                    text6b.draw(win)
                    
               if location7 == "lowerelmst" or location7 == "lower elm st":
                    text7 = Text(Point(990,635),(name7, "Lower Elm St"))
                    text7a = Text(Point(990,650), keyword7)
                    text7b = Text(Point(990,665), dream7)
                    text7.draw(win)
                    text7a.draw(win)
                    text7b.draw(win)
                    
               if location8 == "lowerelmst" or location8 == "lower elm st":
                    text8 = Text(Point(990,685),(name8, "Lower Elm St"))
                    text8a = Text(Point(990,700), keyword8)
                    text8b = Text(Point(990,715), dream8)
                    text8.draw(win)
                    text8a.draw(win)
                    text8b.draw(win)
                    
               continue

               
          if seeAll.isClicked(clickedPoint):
               try:
                    text1 = Text(Point(990,335),(name1, location1))
                    text1a = Text(Point(990,350), keyword1)
                    text1b = Text(Point(990,365), dream1)
                    text1.draw(win)
                    text1a.draw(win)
                    text1b.draw(win)
                    text2 = Text(Point(990,385),(name2, location2))
                    text2a = Text(Point(990,400), keyword2)
                    text2b = Text(Point(990,415), dream2)
                    text2.draw(win)
                    text2a.draw(win)
                    text2b.draw(win)
                    text3 = Text(Point(990,435),(name3, location3))
                    text3a = Text(Point(990,450), keyword3)
                    text3b = Text(Point(990,465), dream3)
                    text3.draw(win)
                    text3a.draw(win)
                    text3b.draw(win)
                    text4 = Text(Point(990,485),(name4, location4))
                    text4a = Text(Point(990,500), keyword4)
                    text4b = Text(Point(990,515), dream4)
                    text4.draw(win)
                    text4a.draw(win)
                    text4b.draw(win)
                    text5 = Text(Point(990,535),(name5, location5))
                    text5a = Text(Point(990,550), keyword5)
                    text5b = Text(Point(990,565), dream5)
                    text5.draw(win)
                    text5a.draw(win)
                    text5b.draw(win)
                    text6 = Text(Point(990,585),(name6, location6))
                    text6a = Text(Point(990,600), keyword6)
                    text6b = Text(Point(990,615), dream6)
                    text6.draw(win)
                    text6a.draw(win)
                    text6b.draw(win)
                    text7 = Text(Point(990,635),(name7, location7))
                    text7a = Text(Point(990,650), keyword7)
                    text7b = Text(Point(990,665), dream7)
                    text7.draw(win)
                    text7a.draw(win)
                    text7b.draw(win)
                    text8 = Text(Point(990,685),(name8, location8))
                    text8a = Text(Point(990,700), keyword8)
                    text8b = Text(Point(990,715), dream8)
                    text8.draw(win)
                    text8a.draw(win)
                    text8b.draw(win)
                    continue
               except:
                    continue

          if clearAll.isClicked(clickedPoint):
               try: 
                    text1.undraw()
                    text1a.undraw()
                    text1b.undraw()
                    text2.undraw()
                    text2a.undraw()
                    text2b.undraw()
                    text3.undraw()
                    text3a.undraw()
                    text3b.undraw()
                    text4.undraw()
                    text4a.undraw()
                    text4b.undraw()
                    text5.undraw()
                    text5a.undraw()
                    text5b.undraw()
                    text6.undraw()
                    text6a.undraw()
                    text6b.undraw()
                    text7.undraw()
                    text7a.undraw()
                    text7b.undraw()
                    text8.undraw()
                    text8a.undraw()
                    text8b.undraw()
                    continue
               except:
                    continue

          

def main():
     global win
     
     # put a logo of Smith in the middle of the window
     img = Image( Point(875/2.4, HEIGHT//2), "SmithMap.gif" ) #name of smith map gif on my comp
     img.draw( win )

     #to open the smith map csv that is has been collaborated by every csc111 student
     file = open(MapCSV, "r")
     lines = file.readlines()
     file.close()
     polygons = boxes(lines)
     createMap(polygons)
     makeButtons()



if __name__ == '__main__':
     main()
