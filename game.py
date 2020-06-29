
import pygame
import os
import random

pygame.init()

screen=pygame.display.set_mode((500,600))
pygame.display.set_caption("Hangman")
catogaries={"COUNTRIES":open(os.path.join("resources","countries.txt"),"r").readlines(),
    "BRANDS":open(os.path.join("resources","brands.txt"),"r").readlines(),
    "TV SHOWS":open(os.path.join("resources","tv_shows.txt"),"r").readlines(),
    "ANIMALS":open(os.path.join("resources","animals.txt"),"r").readlines()}

# Fonts
font_Word=pygame.font.Font(os.path.join("resources","Basketball.otf"),50)
font_catogary=pygame.font.Font(os.path.join("resources","font3.ttf"),23)
states=[0,
        pygame.image.load(os.path.join("resources","state1.png")),
		pygame.image.load(os.path.join("resources","state2.png")),
		pygame.image.load(os.path.join("resources","state3.png")),
		pygame.image.load(os.path.join("resources","state4.png")),
		pygame.image.load(os.path.join("resources","state5.png")),
		pygame.image.load(os.path.join("resources","state6.png")),
		pygame.image.load(os.path.join("resources","state7.png"))
]

if __name__=="__main__":
    run=True
    ValidLetters=[char for char in "abcdefghijklmnopqrstuvwxyz"]
    lis_cat=list(catogaries.keys())
    current_catogary=random.choice(lis_cat)
    lis=catogaries[current_catogary]
    lost=False
    won=False
    state=0
    current_word=(random.choice(lis).lower()).strip()
    masked_word=[]
    for char in current_word:
        if char.isalpha():
            masked_word.append("_")
        elif char.isspace():
            masked_word.append(' ')

    rend_word=font_Word.render(current_word.upper(),1,(0,0,0))
    rend_game_over=font_catogary.render("WRONG!",1,(0,0,0))
    rend_try_again=font_catogary.render('press "R" to try another word.',1,(0,0,0))
    rend_nice=font_Word.render("NICE!",1,(0,0,0))
    while run:
        screen.fill((187, 239, 242))
        rend_masked=font_Word.render(("".join(masked_word)),1,(0,0,0))
        rend_word=font_Word.render(current_word.upper(),1,(0,0,0))
        rend_cat=font_catogary.render(current_catogary,1,(0,0,0))
        if not(won or lost):    
            current_image=states[state]
            if current_image:
                screen.blit(current_image,(300-current_image.get_width(),50))
            screen.blit(rend_cat,((500-rend_cat.get_width())//2,300))
            screen.blit(rend_masked,((500-rend_masked.get_width())//2,400))
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                run = False
            if event.type==pygame.KEYDOWN:
                letter=chr(event.key)
                if letter in ValidLetters and not(won or lost):
                    if letter not in current_word:
                        state+=1
                    else:
                        for x in range(len(current_word)):
                            if current_word[x]==letter:
                                masked_word[x]= letter.upper()
                if letter=="r" and (won or lost):
                    won=False
                    lost=False
                    current_catogary=random.choice(lis_cat)
                    lis=catogaries[current_catogary]
                    current_word=(random.choice(lis).lower()).strip()
                    state=0
                    masked_word=[]
                    for char in current_word:
                        if char.isalpha():
                            masked_word.append("_")
                        elif char.isspace():
                            masked_word.append(' ')
    
        if state>=7:
            lost=True
            screen.blit(rend_game_over,((500-rend_game_over.get_width())//2,150))
            screen.blit(rend_word,((500-rend_word.get_width())//2,250))
            screen.blit(rend_try_again,((500-rend_try_again.get_width())//2,400))
        
        if "_" not in masked_word:
            won=True
            screen.blit(rend_nice,((500-rend_nice.get_width())//2,200))
            screen.blit(rend_try_again,((500-rend_try_again.get_width())//2,400))
        
        pygame.display.update()
    pygame.display.quit()