import turtle # contient les fonctions graphiques

# Creation de la fenetre :
window = turtle.Screen() # retourner la fenetre
window.title(" PING PONG GAME ") # le titre de la fenetre
window.bgcolor("black") # back ground couleur de la fenetre
window.setup(width = 800, height = 600) # la dimension de la fenetre
window.tracer(0) # pour controler la vitesse de la fenetre
# Gauche racket :
racket_gauche = turtle.Turtle() # creation de racket gauche
racket_gauche.speed(0) # la plus grand vitesse pour recreer la racket gauche
racket_gauche.shape("square") # la forme de racket gauche
racket_gauche.shapesize(stretch_wid = 5, stretch_len = 1) # pour definir la taille de la racket gauche
racket_gauche.color("firebrick1") # la couleur de la racket gauche
racket_gauche.penup() # pour effacer les traces de la racket gauche
racket_gauche.goto(-350, 0) # la place de la racket gauche dans la fenetre
# Droite racket :
racket_droite = turtle.Turtle() # creation de racket droit
racket_droite.speed(0) # la plus grand vitesse pour recreer la racket droite
racket_droite.shape("square") # la forme de racket droite
racket_droite.shapesize(stretch_wid = 5, stretch_len = 1) # pour definir la taille de la racket droite
racket_droite.color("DeepSkyBlue3") # la couleur de la racket droite
racket_droite.penup() # pour effacer les traces de la racket droite
racket_droite.goto(350, 0) # la place de la racket droite dans la fenetre
# Ball :
ball = turtle.Turtle() # creation de la ball
ball.speed(0) # la plus grand vitesse pour recreer la ball
ball.shape("circle") # la forme de la ball
ball.color("white") # la couleur de la ball
ball.penup() # pour effacer les traces de la ball
ball.goto(0, 0) # la place de la ball dans la fenetre
ball.dx = 0.5
ball.dy = 0.5
# Fonctions :
def racket_gauche_up ():
    if racket_gauche.ycor()+50 < 290:
        racket_gauche.sety(racket_gauche.ycor() + 20) # pour mouvoir la racket gauche vers le haut
def racket_gauche_down ():
    if racket_gauche.ycor()-50 > -290:
        racket_gauche.sety(racket_gauche.ycor() - 20) # pour mouvoir la racket gauche vers la bas
def racket_droite_up ():
    if racket_droite.ycor()+50 < 290:
        racket_droite.sety(racket_droite.ycor() + 20) # pour mouvoir la racket droite vers le haut
def racket_droite_down ():
    if racket_droite.ycor()-50 > -290:
        racket_droite.sety(racket_droite.ycor() - 20) # pour mouvoir la racket droite vers la bas
# Clavier bouttons :
window.listen()
window.onkeypress(racket_gauche_up, "w") # si le boutton == "w" alors use fonction racket_gauche_up
window.onkeypress(racket_gauche_down, "s") # si le boutton == "s" alors use fonction racket_gauche_down
window.onkeypress(racket_droite_up, "Up") # si le boutton == "Up" alors use fonction racket_droite_up
window.onkeypress(racket_droite_down, "Down") # si le boutton == "Down" alors use fonction racket_droite_down
# Score blue :
score_b = 0
score_blue = turtle.Turtle()
score_blue.speed(0)
score_blue.color("DeepSkyBlue3")
score_blue.penup()
score_blue.hideturtle()
score_blue.goto(0, 260)
score_blue.write(f" Score : {score_b}", align = "center", font = ("Consolas", 22, "normal"))
# Score red :
score_r = 0
score_red = turtle.Turtle()
score_red.speed(0)
score_red.color("firebrick1")
score_red.penup()
score_red.hideturtle()
score_red.goto(0, -260)
score_red.write(f" Score : {score_r}", align = "center", font = ("Consolas", 22, "normal"))

while True:
    window.update() # pour creer la fenetre encore une fois
    # Mouvements de la ball :
    ball.setx(ball.xcor() + ball.dx) # pour mouvoir la ball dans l'axe des x
    ball.sety(ball.ycor() + ball.dy) # pour mouvoir la ball dans l'axe des y
    # Border and ball conditions :
    # si la ball touche en haut de la fenetre
    if ball.ycor() > 290: 
        ball.sety(290)
        ball.dy *= -1
    # si la ball touche en bas de la fenetre
    if ball.ycor() < -290: 
        ball.sety(-290)
        ball.dy *= -1
    # si la ball marke un but sur le joueur de la droite
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_r += 1
        score_red.clear()
        score_red.write(f" Score : {score_r}", align = "center", font = ("Consolas", 22, "normal"))
    # si la ball marke un but sur le joueur de la gauche
    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        score_blue.clear()
        score_blue.write(f" Score : {score_b}", align = "center", font = ("Consolas", 22, "normal"))
    # Rackets and ball conditions :
    # si la ball touche la racket droite
    if 340 < ball.xcor() < 350 and racket_droite.ycor()-50 < ball.ycor() < racket_droite.ycor() + 50:
        ball.setx(340)
        ball.dx *= -1
    # si la ball touche la racket g
    if -350 < ball.xcor() < -340 and racket_gauche.ycor()-50 < ball.ycor() < racket_gauche.ycor() + 50:
        ball.setx(-340)
        ball.dx *= -1