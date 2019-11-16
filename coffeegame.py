import pygame

def main():
    pygame.init()
    screen=pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.set_caption("Coffee Game")
    exit=False
    clock1=pygame.time.Clock()
    white=(255,255,255)
    sugar=pygame.image.load("sugar.jpeg")
    sugarcounter=500
    coffee=pygame.image.load("coffee.jpg")
    coffeecounter=500
    money=pygame.image.load("money.jpg")
    moneycounter=0

    pygame.mixer.music.load("soundtrack.mp3")
    pygame.mixer.music.play()
    moneysound=pygame.mixer.Sound("money.wav")

    while exit!=True:#Main Loop
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit=True
                elif event.key == pygame.K_SPACE:
                    if coffeecounter>=15 and sugarcounter>=10:
                        moneysound.play()
                        coffeecounter=coffeecounter-15
                        sugarcounter=sugarcounter-10
                        moneycounter=moneycounter+2000
                    else:
                        pygame.mixer.Sound.play(pygame.mixer.Sound("fail.wav"))
                elif event.key == pygame.K_c:
                    moneysound.play()
                    coffeecounter=coffeecounter+500
                    moneycounter=moneycounter-15000
                elif event.key == pygame.K_s:
                    moneysound.play()
                    sugarcounter=sugarcounter+500
                    moneycounter=moneycounter-2000
        clock1.tick(20)
        screen.fill(white)
        screen.blit(coffee,(0, 200))
        f=pygame.font.Font(None, 100)
        screen.blit(f.render(str(coffeecounter), True, [0,0,0], [255,255,255,255]), (120,560))
        screen.blit(money, (425, 200))
        screen.blit(f.render("$", True, [0, 0, 0], [255, 255, 255, 255]), (450, 560))
        screen.blit(f.render(str(moneycounter), True, [0,0,0], [255,255,255,255]), (500,560))
        screen.blit(sugar, (850, 35))
        screen.blit(f.render(str(sugarcounter), True, [0, 0, 0], [255, 255, 255, 255]), (1100, 560))
        pygame.display.update()

    pygame.quit()

main()