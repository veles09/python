import graphics as gr


win = gr.GraphWin('Окно', 800,640)# переопределить метод круглая форма ока

korColor = gr.color_rgb(168, 89, 2)

nebo = gr.Rectangle(gr.Point(0,0),gr.Point(800,320))
nebo.setFill(gr.color_rgb(41, 208, 242))
nebo.draw(win)

zemlia = gr.Rectangle(gr.Point(0,320),gr.Point(800,640))
zemlia.setFill(korColor)
zemlia.draw(win)

sun = gr.Circle(gr.Point(630,130), 40)
sun.setFill("Yellow")
sun.draw(win)

# dom

home = gr.Rectangle(gr.Point(100,200),gr.Point(300,400))
home.setFill(gr.color_rgb(146, 160, 163))
home.draw(win)

#window

cherdak = gr.Polygon(gr.Point(100,200),gr.Point(200,130),gr.Point(300,200))
cherdak.setOutline("grey")
cherdak.setWidth(3)
cherdak.setFill('grey')
cherdak.draw(win)

w = gr.Rectangle(gr.Point(175,270), gr.Point(225,320))
l1 = gr.Line(gr.Point(200,270),gr.Point(200,320))
l2 = gr.Line(gr.Point(175,295),gr.Point(225,295))
w.setFill("Yellow")
w.draw(win)
l1.draw(win)
l2.draw(win)
def draw_cloud(x,y,r):
	cloud = gr.Circle(gr.Point(x,y),r)
	cloud.setFill("white")
	cloud.draw(win)

def clouds(x,y,r):
	draw_cloud(x,y,20)
	draw_cloud(x+20,y,20)
	draw_cloud(x-10,y+10,20)
	draw_cloud(x+10,y+10,20)
	draw_cloud(x+30,y+10,20)

clouds(100,100,20)
clouds(400,150,20)
clouds(450,50,30)





win.getMouse() # ждём нажатия кнопки мыши
win.close() # закрываем окно для графики