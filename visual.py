from kivy.graphics import Color, Canvas, Ellipse


class Light(Canvas):
    circles = []

    def __init__(self, posx, posy, width):
            i = 0
            while(i < width):
                col = Color(1, 1, 1, .02)
                pose = (posx-(width-i)/2, posy-(width-i)/2)
                taille = (width - i, width - i)
                if i % 2 == 0:
                    cir = Ellipse(pos=pose, size=taille, Color=col)
                    self.circles.append(cir)
                i += 1
