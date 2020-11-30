from graphics import *
import random

win = GraphWin("PLATFORM", 800, 600)
win.setBackground("black")
imagem = Image(Point(400,300), "inicio.gif")
imagem.draw(win)

def menu():
    global mensagem_inicial
    mensagem_inicial = Text(Point(400, 570), "DESENVOLVIDO POR ANTONIO FILHO.")

    mensagem_inicial.setSize(10)
    mensagem_inicial.setFace("arial")
    mensagem_inicial.setStyle("bold")
    mensagem_inicial.setTextColor(color_rgb(233, 78, 27))
    mensagem_inicial.draw(win)

def facil():
    global iniciar, linhadecima, linhaesquerda, linhadireita, linhabaixo, colini, movel, pontos, pontuacao, col, lin, circulo, continuar, bateu, velocidade, passo, controles
    if tecla == "1":
        iniciar = False
        imagem.undraw()
        mensagem_inicial.undraw()
        plano = Image(Point(400,300), "fundoplatform.gif")
        plano.draw(win)

        linhadecima = Line(Point(0, 20), Point(800, 20))
        linhadecima.setWidth(40)
        linhadecima.setFill(color_rgb(233, 78, 27))
        linhadecima.draw(win)

        linhaesquerda = Line(Point(0, 0), Point(0, 600))
        linhaesquerda.setFill(color_rgb(233, 78, 27))
        linhaesquerda.setWidth(30)
        linhaesquerda.draw(win)

        linhadireita = Line(Point(800, 0), Point(800, 600))
        linhadireita.setWidth(30)
        linhadireita.setFill(color_rgb(233, 78, 27))
        linhadireita.draw(win)

        linhabaixo = Line(Point(30, 530), Point(770, 530))
        linhabaixo.setWidth(30)
        linhabaixo.setFill("black")
        linhabaixo.draw(win)

        colini = 400
        movel = Line(Point(colini - 100, 530), Point(colini + 100, 530))
        movel.setWidth(20)
        movel.setFill(color_rgb(233, 78, 27))
        movel.draw(win)

        pontos = 0
        pontuacao = Text(Point(400, 20), pontos)
        pontuacao.setSize(35)
        pontuacao.draw(win)

        col = 400
        lin = 60

        circulo = Circle(Point(col, lin), 20)
        circulo.setFill(color_rgb(233, 78, 27))
        circulo.draw(win)

        nivelamento = Text(Point(400,570), "LEVEL: ROOKIE")
        nivelamento.setSize(15)
        nivelamento.setTextColor(color_rgb(233, 78, 27))
        nivelamento.draw(win)



        continuar = True
        bateu = True
        velocidade = 10

        while continuar:
            if bateu == True:
                passo = int(random.randint(-10, 10))
                bateu = False
            if (col + passo) > 770:
                if passo > 0:
                    passo = (int(random.randint(-10, -5)))
            if (col + passo) < 30:
                if passo < 0:
                    passo = (int(random.randint(5, 10)))
                else:
                    passo = passo

            if (velocidade + lin) > 508:
                if (velocidade + lin) < 530:
                    if (colini - 115) < (col - 15) and (colini + 115) > (col + 15):
                        passo = (int(random.randint(-15, 15)))
                        velocidade = -velocidade
                        pontos += 10
                        pontuacao.undraw()
                        pontuacao = Text(Point(400, 20), pontos)
                        pontuacao.setSize(35)
                        pontuacao.draw(win)

            elif (lin + velocidade) < 60:
                velocidade = -velocidade
                passo = int(random.randint(-15, 15))

            if (lin + velocidade) > 560:
                movel.undraw()
                circulo.undraw()
                pontuacao.undraw()
                nivelamento.undraw()
                telafinal = Image(Point(400,300), "gameovermts.gif")
                telafinal.draw(win)
                total = Text(Point(400, 250), "VOCÊ FEZ " + str(pontos) + " PONTOS")
                total.setTextColor(color_rgb(233, 78, 27))
                total.setSize(20)
                total.draw(win)

                agradecimentos = Text(Point(400,570), "DESENVOLVIDO POR BRUNO RIOS, MATHEUS GUIMARÃES, LUCAS PORTO, ANTONIO FILHO E JOÃO PAULO.")
                agradecimentos.setTextColor(color_rgb(233, 78, 27))
                agradecimentos.setSize(10)
                agradecimentos.draw(win)

                reiniciar = True
                while reiniciar:
                    reinicio = win.checkKey()
                    if reinicio == "Escape":
                        agradecimentos.undraw()
                        total.undraw()
                        telafinal.undraw()
                        facil()
                        media()
                        dificil()

            circulo.undraw()
            col += passo
            lin += velocidade
            circulo = Circle(Point(col, lin), 20)
            circulo.setFill(color_rgb(233, 78, 27))
            circulo.draw(win)

            controles = win.checkKey()
            if controles == "Right":
                if (colini + 100 + 40) <= 800:
                    colini = colini + 40
                    movel.undraw()
                    movel = Line(Point(colini - 100, 530), Point(colini + 100, 530))
                    movel.setWidth(15)
                    movel.setFill(color_rgb(233, 78, 27))
                    movel.draw(win)
            if controles == "Left":
                if (colini - 100 - 40) >= 1:
                    colini = colini - 40
                    movel.undraw()
                    movel = Line(Point(colini - 100, 530), Point(colini + 100, 530))
                    movel.setWidth(15)
                    movel.setFill(color_rgb(233, 78, 27))
                    movel.draw(win)

def media():
    global iniciar, linhadecima, linhaesquerda, linhadireita, linhabaixo, colini, movel, pontos, pontuacao, col, lin, circulo, continuar, bateu, velocidade, passo, controles
    if tecla == "2":
        iniciar = False
        imagem.undraw()
        mensagem_inicial.undraw()
        plano = Image(Point(400,300), "fundoplatform.gif")
        plano.draw(win)



        linhadecima = Line(Point(0, 20), Point(800, 20))
        linhadecima.setWidth(40)
        linhadecima.setFill(color_rgb(233, 78, 27))
        linhadecima.draw(win)

        linhaesquerda = Line(Point(0, 0), Point(0, 600))
        linhaesquerda.setFill(color_rgb(233, 78, 27))
        linhaesquerda.setWidth(30)
        linhaesquerda.draw(win)

        linhadireita = Line(Point(800, 0), Point(800, 600))
        linhadireita.setWidth(30)
        linhadireita.setFill(color_rgb(233, 78, 27))
        linhadireita.draw(win)

        linhabaixo = Line(Point(30, 530), Point(770, 530))
        linhabaixo.setWidth(30)
        linhabaixo.setFill("black")
        linhabaixo.draw(win)

        colini = 400
        movel = Line(Point(colini - 75, 530), Point(colini + 75, 530))
        movel.setWidth(15)
        movel.setFill(color_rgb(233, 78, 27))
        movel.draw(win)

        pontos = 0
        pontuacao = Text(Point(400, 20), pontos)
        pontuacao.setSize(35)
        pontuacao.draw(win)

        col = 400
        lin = 60

        nivelamento = Text(Point(400, 570), "LEVEL: PRO")
        nivelamento.setTextColor(color_rgb(233, 78, 27))
        nivelamento.setSize(15)
        nivelamento.draw(win)

        circulo = Circle(Point(col, lin), 20)
        circulo.setFill(color_rgb(233, 78, 27))
        circulo.draw(win)

        continuar = True
        bateu = True
        velocidade = 15

        while continuar:
            if bateu == True:
                passo = int(random.randint(-10, 10))
                bateu = False
            if (col + passo) > 770:
                if passo > 0:
                    passo = (int(random.randint(-10, -3)))
            if (col + passo) < 30:
                if passo < 0:
                    passo = (int(random.randint(3, 10)))
                else:
                    passo = passo

            if (velocidade + lin) > 508:
                if (velocidade + lin) < 530:
                    if (colini - 85) < (col - 15) and (colini + 85) > (col + 15):
                        passo = (int(random.randint(-15, 15)))
                        velocidade = -velocidade
                        pontos += 10
                        pontuacao.undraw()
                        pontuacao = Text(Point(400, 20), pontos)
                        pontuacao.setSize(35)
                        pontuacao.draw(win)

            elif (lin + velocidade) < 60:
                velocidade = -velocidade
                passo = int(random.randint(-15, 15))

            if (lin + velocidade) > 560:
                movel.undraw()
                circulo.undraw()
                pontuacao.undraw()
                nivelamento.undraw()
                telafinal = Image(Point(400,300), "gameovermts.gif")
                telafinal.draw(win)
                total = Text(Point(400, 250), "VOCÊ FEZ " + str(pontos) + " PONTOS")
                total.setTextColor(color_rgb(233, 78, 27))
                total.setSize(20)
                total.draw(win)
                agradecimentos = Text(Point(400,570), "DESENVOLVIDO POR BRUNO RIOS, MATHEUS GUIMARÃES, LUCAS PORTO, ANTONIO FILHO E JOÃO PAULO.")
                agradecimentos.setTextColor(color_rgb(233, 78, 27))
                agradecimentos.setSize(10)
                agradecimentos.draw(win)
                reiniciar = True
                while reiniciar:
                    reinicio = win.checkKey()
                    if reinicio == "Escape":
                        agradecimentos.undraw()
                        telafinal.undraw()
                        total.undraw()
                        facil()
                        media()
                        dificil()

            circulo.undraw()
            col += passo
            lin += velocidade
            circulo = Circle(Point(col, lin), 20)
            circulo.setFill(color_rgb(233, 78, 27))
            circulo.draw(win)

            controles = win.checkKey()
            if controles == "Right":
                if (colini + 75 + 40) <= 800:
                    colini = colini + 40
                    movel.undraw()
                    movel = Line(Point(colini - 75, 530), Point(colini + 75, 530))
                    movel.setWidth(15)
                    movel.setFill(color_rgb(233, 78, 27))
                    movel.draw(win)
            if controles == "Left":
                if (colini - 75 - 40) >= 1:
                    colini = colini - 40
                    movel.undraw()
                    movel = Line(Point(colini - 75, 530), Point(colini + 75, 530))
                    movel.setWidth(15)
                    movel.setFill(color_rgb(233, 78, 27))
                    movel.draw(win)

def dificil():
    global iniciar, linhadecima, linhaesquerda, linhadireita, linhabaixo, colini, movel, pontos, pontuacao, col, lin, circulo, continuar, bateu, velocidade, passo, controles
    if tecla == "3":
        iniciar = False
        imagem.undraw()
        mensagem_inicial.undraw()
        plano = Image(Point(400,300), "fundoplatform.gif")
        plano.draw(win)


        linhadecima = Line(Point(0, 20), Point(800, 20))
        linhadecima.setWidth(40)
        linhadecima.setFill(color_rgb(233, 78, 27))
        linhadecima.draw(win)

        linhaesquerda = Line(Point(0, 0), Point(0, 600))
        linhaesquerda.setFill(color_rgb(233, 78, 27))
        linhaesquerda.setWidth(30)
        linhaesquerda.draw(win)

        linhadireita = Line(Point(800, 0), Point(800, 600))
        linhadireita.setWidth(30)
        linhadireita.setFill(color_rgb(233, 78, 27))
        linhadireita.draw(win)

        linhabaixo = Line(Point(30, 530), Point(770, 530))
        linhabaixo.setWidth(30)
        linhabaixo.setFill("black")
        linhabaixo.draw(win)

        colini = 400
        movel = Line(Point(colini - 50, 530), Point(colini + 50, 530))
        movel.setWidth(15)
        movel.setFill(color_rgb(233, 78, 27))
        movel.draw(win)

        pontos = 0
        pontuacao = Text(Point(400, 20), pontos)
        pontuacao.setSize(35)
        pontuacao.draw(win)

        col = 400
        lin = 60

        circulo = Circle(Point(col, lin), 20)
        circulo.setFill(color_rgb(233, 78, 27))
        circulo.draw(win)

        nivelamento = Text(Point(400,570), "LEVEL: EXPERT")
        nivelamento.setSize(15)
        nivelamento.setTextColor(color_rgb(233, 78, 27))
        nivelamento.setFace("helvetica")
        nivelamento.draw(win)

        continuar = True
        bateu = True
        velocidade = 20

        while continuar:
            if bateu == True:
                passo = int(random.randint(-10, 10))
                bateu = False
            if (col + passo) > 770:
                if passo > 0:
                    passo = (int(random.randint(-10, -3)))
            if (col + passo) < 30:
                if passo < 0:
                    passo = (int(random.randint(3, 10)))
                else:
                    passo = passo

            if (velocidade + lin) > 508:
                if (velocidade + lin) < 530:
                    if (colini - 65) < (col - 15) and (colini + 65) > (col + 15):
                        passo = (int(random.randint(-15, 15)))
                        velocidade = -velocidade
                        pontos += 10
                        pontuacao.undraw()
                        pontuacao = Text(Point(400, 20), pontos)
                        pontuacao.setSize(35)
                        pontuacao.draw(win)

            elif (lin + velocidade) < 60:
                velocidade = -velocidade
                passo = int(random.randint(-15, 15))

            if (lin + velocidade) > 560:
                plano.undraw()
                movel.undraw()
                circulo.undraw()
                pontuacao.undraw()
                nivelamento.undraw()
                telafinal = Image(Point(400,300), "gameovermts.gif")
                telafinal.draw(win)
                total = Text(Point(400, 250), "VOCÊ FEZ " + str(pontos) + " PONTOS")
                total.setTextColor(color_rgb(233, 78, 27))
                total.setSize(20)
                total.draw(win)
                agradecimentos = Text(Point(400,570), "DESENVOLVIDO POR ANTONIO FILHO.")
                agradecimentos.setTextColor(color_rgb(233, 78, 27))
                agradecimentos.setSize(10)
                agradecimentos.draw(win)

                reiniciar = True
                while reiniciar:
                    reinicio = win.checkKey()
                    if reinicio == "Escape":
                        agradecimentos.undraw()
                        telafinal.undraw()
                        total.undraw()
                        facil()
                        media()
                        dificil()

            circulo.undraw()
            col += passo
            lin += velocidade
            circulo = Circle(Point(col, lin), 20)
            circulo.setFill(color_rgb(233, 78, 27))
            circulo.draw(win)

            controles = win.checkKey()
            if controles == "Right":
                if (colini + 50 + 40) <= 800:
                    colini = colini + 40
                    movel.undraw()
                    movel = Line(Point(colini - 50, 530), Point(colini + 50, 530))
                    movel.setWidth(15)
                    movel.setFill(color_rgb(233, 78, 27))
                    movel.draw(win)
            if controles == "Left":
                if (colini - 50 - 40) >= 1:
                    colini = colini - 40
                    movel.undraw()
                    movel = Line(Point(colini - 50, 530), Point(colini + 50, 530))
                    movel.setWidth(15)
                    movel.setFill(color_rgb(233, 78, 27))
                    movel.draw(win)

menu()
iniciar = True
while iniciar:
    tecla = win.checkKey()
    facil()
    media()
    dificil()

    time.sleep(0.01)
