# general setup
import pygame


pygame.init()
screen = pygame.display.set_mode([800,600])
 



class Player(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 80
    

    def draw(self):
        color = (255, 255, 255)
        return pygame.draw.rect(screen, color, pygame.Rect(self.x, self.y, self.width, self.height))


class Ball(object):
    def __init__(self):
        self.x = 400
        self.y = 300
        self.width = 20
        self.height = 20
        self.movex = 1
        self.movey = 1
    def draw(self):
        color = (255,255,255)
        return pygame.draw.rect(screen,color,pygame.Rect(self.x,self.y, self.width, self.height))
    def move(self):
        self.x += self.movex
        self.y += self.movey

p1 = Player(0, 300)
p2 = Player(790, 250)
ball = Ball()
score1 = 0
score2 = 0
# beef of our code
running = True
gameStart = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
 
    screen.fill((0,0,0)) # clearing the screen
    player1data = p1.draw()
    player2data = p2.draw()
    ball.draw()



    if gameStart:
        ball.move()


    #keyboard stuff
    key_input = pygame.key.get_pressed()
    if key_input[pygame.K_SPACE]:
        ball.move()
        gameStart = True
    if key_input[pygame.K_UP]:
        p2.y -= 5
    elif key_input[pygame.K_DOWN]:
        p2.y += 5
    if key_input[pygame.K_w]:
        p1.y -= 5
    elif key_input[pygame.K_s]:
        p1.y += 5
    
    
    wallBottom = pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, 550, 800, 50))
    wallTop = pygame.draw.rect(screen, (255,255,255), pygame.Rect(0, 0, 800, 50))
    if wallBottom.collidepoint((ball.x, ball.y)) or wallTop.collidepoint((ball.x, ball.y)):
        ball.movey = -ball.movey
    

    # Player collision code

    if player1data.collidepoint((ball.x, ball.y)) or player2data.collidepoint((ball.x, ball.y)):
        ball.movex= - ball.movex
    
    if ball.x > p2.x:
        score1 +=1 
        ball.x = 400
        ball.y = 300
        gameStart = False
    elif ball.x < p1.x:
        score2 +=1 
        ball.x = 400
        ball.y = 300
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('Player 1: ' + str(score1), True, (255,0,0), (100, 255, 0))
    textRect = text.get_rect()
    textRect.center = (300,30)
    screen.blit(text, textRect)
    pygame.display.set_caption('caption text')
    text = font.render('Player 2: ' + str(score2), True, (255,0,0), (100, 255, 0))
    textRect = text.get_rect()
    textRect.center = (500,30)
    screen.blit(text, textRect)



    text = font.render('GAMEOVER', True, (255,0,0), (100, 255, 0))
    textGameOver = text.get_rect()
    textGameOver.center = (-100,-100)
    screen.blit(text, textGameOver)

    if score1 > 5 or score2 > 5:
        textGameOver.center = (400,300)
        screen.blit(text, textGameOver)
        



    pygame.display.update()
 


 
# closing code
pygame.quit()