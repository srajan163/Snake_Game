from food import Food
ALIGINMENT="center"
FONT= ("Amaze",20,"normal")
class Scoreboard(Food):
    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.goto(0,260)
        self.penup()
        self.hideturtle()
        self.Scoreboard_score()






    def Scoreboard_score(self):
        self.write(f"Score = {self.score}", align=ALIGINMENT, font=FONT)


    def Game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGINMENT, font=FONT)




    def increase_score(self):
        self.score+=1
        self.clear()
        self.Scoreboard_score()