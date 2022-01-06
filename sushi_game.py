import os

import pygame
import random

pygame.font.init()
pygame.mixer.init()

# game constants/variables
WIDTH, HEIGHT = 900, 500
FPS = 60
VEL_EASY = 6
FALLING_VEL_EASY = 5
VEL_NORMAL = 5
FALLING_VEL_NORMAL = 6
VEL_HARD = 7
FALLING_VEL_HARD = FALLING_VEL_NORMAL
MAX_COL = 1
GAME_FONT = pygame.font.SysFont("courier", 30, bold=True)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("COLLECT THAT SUSHI !!")
GOOD_SOUND = pygame.mixer.Sound(os.path.join("sushi_images", "good.mp3"))
BAD_SOUND = pygame.mixer.Sound(os.path.join("sushi_images", "bad.mp3"))

# events
COLLECT_GOOD = pygame.USEREVENT + 1
COLLECT_BAD = pygame.USEREVENT + 2

# images
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("sushi_images", 'background.jpeg')), (WIDTH, HEIGHT))
BASKET_IMG = pygame.transform.scale(pygame.image.load(os.path.join("sushi_images", "basket.png")), (120, 120))
ROLL_IMG = pygame.transform.scale(pygame.image.load(os.path.join("sushi_images", "salmon_avo.png")), (50, 50))
SASHIMI_IMG = pygame.transform.scale(pygame.image.load(os.path.join("sushi_images", "sashimi.png")), (50, 50))
RAMEN_IMG = pygame.transform.scale(pygame.image.load(os.path.join("sushi_images", "ramen.png")), (50, 50))
WASABI_IMG = pygame.transform.scale(pygame.image.load(os.path.join("sushi_images", "wasabi.png")), (50, 50))


def draw_window_easy_normal(basket, roll, wasabi, sashimi, ramen, score, timer):
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(BASKET_IMG, (basket.x, basket.y - 30))
    WIN.blit(ROLL_IMG, (roll.x, roll.y))
    WIN.blit(WASABI_IMG, (wasabi.x, wasabi.y))
    WIN.blit(SASHIMI_IMG, (sashimi.x, sashimi.y))
    WIN.blit(RAMEN_IMG, (ramen.x, ramen.y))

    # score tracker
    score_text = GAME_FONT.render("SCORE: " + str(score), True, (0, 0, 0))
    WIN.blit(score_text, (10, 10))

    # countdown clock
    timer_text = GAME_FONT.render("TIME: " + str(int(timer)), True, (0, 0, 0))
    WIN.blit(timer_text, (740, 10))
    pygame.display.update()


def draw_window_hard(basket, roll, wasabi, wasabi2, sashimi, ramen, score, timer):
    WIN.blit(BACKGROUND, (0, 0))
    WIN.blit(ROLL_IMG, (roll.x, roll.y))
    WIN.blit(WASABI_IMG, (wasabi.x, wasabi.y))
    WIN.blit(WASABI_IMG, (wasabi2.x, wasabi2.y))
    WIN.blit(SASHIMI_IMG, (sashimi.x, sashimi.y))
    WIN.blit(RAMEN_IMG, (ramen.x, ramen.y))
    WIN.blit(BASKET_IMG, (basket.x, basket.y - 30))

    # score tracker
    score_text = GAME_FONT.render("SCORE: " + str(score), True, (0, 0, 0))
    WIN.blit(score_text, (10, 10))

    # countdown clock
    timer_text = GAME_FONT.render("TIME: " + str(int(timer)), True, (0, 0, 0))
    WIN.blit(timer_text, (740, 10))
    pygame.display.update()


def basket_movement_easy(keys_pressed, basket):
    if keys_pressed[pygame.K_LEFT] and basket.x - VEL_EASY > 0:
        basket.x -= VEL_EASY
    if keys_pressed[pygame.K_RIGHT] and basket.x + VEL_EASY + basket.width < 900:
        basket.x += VEL_EASY


def basket_movement_normal_hard(keys_pressed, basket):
    if keys_pressed[pygame.K_LEFT] and basket.x - VEL_EASY > 0:
        basket.x -= VEL_NORMAL
    if keys_pressed[pygame.K_RIGHT] and basket.x + VEL_EASY + basket.width < 900:
        basket.x += VEL_NORMAL


def good_movement_easy(food, basket, good_items):
    food.y += FALLING_VEL_EASY
    if food.y > HEIGHT:
        food.x = random.randrange(0, WIDTH - 20)
        food.y = -10
    if basket.colliderect(food):
        food.y = -10
        food.x = random.randrange(0, WIDTH - 20)
        pygame.event.post(pygame.event.Event(COLLECT_GOOD))
        good_items.clear()


def good_movement_normal_hard(food, basket, good_items):
    food.y += FALLING_VEL_NORMAL
    if food.y > HEIGHT:
        food.x = random.randrange(0, WIDTH - 20)
        food.y = -10
    if basket.colliderect(food):
        food.y = -10
        food.x = random.randrange(0, WIDTH - 20)
        pygame.event.post(pygame.event.Event(COLLECT_GOOD))
        good_items.clear()


def bad_movement_easy(food, basket, bad_items):
    food.y += FALLING_VEL_EASY - 1
    if food.y > HEIGHT:
        food.x = random.randrange(0, WIDTH - 20)
        food.y = -10
    if basket.colliderect(food):
        food.y = -10
        food.x = random.randrange(0, WIDTH - 20)
        pygame.event.post(pygame.event.Event(COLLECT_BAD))
        bad_items.clear()


def bad_movement_normal(food, basket, bad_items):
    food.y += FALLING_VEL_NORMAL
    if food.y > HEIGHT:
        food.x = random.randrange(0, WIDTH - 20)
        food.y = -10
    if basket.colliderect(food):
        food.y = -10
        food.x = random.randrange(0, WIDTH - 20)
        pygame.event.post(pygame.event.Event(COLLECT_BAD))
        bad_items.clear()


def bad_movement_hard(food, basket, bad_items):
    food.y += FALLING_VEL_HARD + 2
    if food.y > HEIGHT:
        food.x = random.randrange(0, WIDTH - 20)
        food.y = -10
    if basket.colliderect(food):
        food.y = -10
        food.x = random.randrange(0, WIDTH - 20)
        pygame.event.post(pygame.event.Event(COLLECT_BAD))
        bad_items.clear()


def end_message(text):
    message = GAME_FONT.render(text, True, (0, 0, 0))
    pygame.draw.rect(WIN, (255, 255, 255), (WIDTH // 2 - ((message.get_width() + 150)/2), (HEIGHT / 2 - ((message.get_height() + 100)/2)), message.get_width() + 150, message.get_height() + 100))
    WIN.blit(message, (WIDTH // 2 - message.get_width() / 2, HEIGHT / 2 - message.get_height() / 2))

    pygame.display.update()
    pygame.time.delay(5000)


def main():
    basket = pygame.Rect(WIDTH / 2 - BASKET_IMG.get_width() / 2, 390, 120, 10)
    roll = pygame.Rect(20, 30, 50, 50)
    wasabi = pygame.Rect(200, 30, 50, 50)
    wasabi2 = pygame.Rect(400, -100, 50, 50)
    sashimi = pygame.Rect(500, 30, 50, 50)
    ramen = pygame.Rect(700, 30, 50, 50)
    score = 0

    good_items = [1]
    bad_items = [1]

    timer = 60
    last_count = pygame.time.get_ticks()

    run = True
    main_menu = True
    easy_mode = False
    normal_mode = False
    hard_mode = False
    while run:
        pygame.time.Clock().tick(FPS)
        if pygame.key.get_pressed()[pygame.K_1]:
            main_menu = False
            easy_mode = True
            normal_mode = False
            hard_mode = False
        if pygame.key.get_pressed()[pygame.K_2]:
            main_menu = False
            easy_mode = False
            normal_mode = True
            hard_mode = False
        if pygame.key.get_pressed()[pygame.K_3]:
            main_menu = False
            easy_mode = False
            normal_mode = False
            hard_mode = True
        if main_menu:
            WIN.blit(BACKGROUND, (0, 0))
            pygame.draw.rect(WIN, (255, 255, 255), (200, 68, 500, 200))
            easy_message = GAME_FONT.render("EASY MODE: Press 1", True, (0, 0, 0))
            WIN.blit(easy_message, (WIDTH / 2 - easy_message.get_width() / 2, 100))
            normal_message = GAME_FONT.render("NORMAL MODE: Press 2", True, (0, 0, 0))
            WIN.blit(normal_message, (WIDTH / 2 - normal_message.get_width() / 2, 150))
            hard_message = GAME_FONT.render("HARD MODE: Press 3", True, (0, 0, 0))
            WIN.blit(hard_message, (WIDTH / 2 - hard_message.get_width() / 2, 200))
            menu_message1 = GAME_FONT.render("Collect as much sushi as you can in 1 minute!", True, (0, 0, 0))
            WIN.blit(menu_message1, (WIDTH / 2 - menu_message1.get_width() / 2, 300))
            menu_message2 = GAME_FONT.render("BEWARE OF WASABI", True, (0, 0, 0))
            WIN.blit(menu_message2, (WIDTH / 2 - menu_message2.get_width() / 2, 350))
            return_message = GAME_FONT.render("Press Space at anytime to return to menu", True, (0, 0, 0))
            WIN.blit(return_message, (WIDTH / 2 - return_message.get_width() / 2, 400))
            pygame.display.update()

        elif easy_mode:
            # countdown timer
            if timer > 0:
                count = pygame.time.get_ticks()
                if count - last_count > 1000:
                    timer -= 1
                    last_count = count
            if timer <= 0:
                end_message("Your Score is " + str(score) + "!")
                main()

            # keeping track of the score
            if event.type == COLLECT_GOOD and len(good_items) < MAX_COL:
                score += 100
                good_items.append(1)
                GOOD_SOUND.set_volume(0.5)
                GOOD_SOUND.play()
            if event.type == COLLECT_BAD and len(bad_items) < MAX_COL:
                if score < 100:
                    score = 0
                    bad_items.append(1)
                    BAD_SOUND.set_volume(0.15)
                    BAD_SOUND.play()
                else:
                    score -= 100
                    bad_items.append(1)
                    BAD_SOUND.set_volume(0.15)
                    BAD_SOUND.play()

            keys_pressed = pygame.key.get_pressed()
            basket_movement_easy(keys_pressed, basket)
            good_movement_easy(roll, basket, good_items)
            good_movement_easy(sashimi, basket, good_items)
            good_movement_easy(ramen, basket, good_items)
            bad_movement_easy(wasabi, basket, bad_items)
            draw_window_easy_normal(basket, roll, wasabi, sashimi, ramen, score, timer)

        elif normal_mode:
            # countdown timer
            if timer > 0:
                count = pygame.time.get_ticks()
                if count - last_count > 1000:
                    timer -= 1
                    last_count = count
            if timer <= 0:
                end_message("Your Score is " + str(score) + "!")
                main()

            # keeping track of the score
            if event.type == COLLECT_GOOD and len(good_items) < MAX_COL:
                score += 100
                good_items.append(1)
                GOOD_SOUND.set_volume(0.5)
                GOOD_SOUND.play()
            if event.type == COLLECT_BAD and len(bad_items) < MAX_COL:
                if score < 200:
                    score = 0
                    bad_items.append(1)
                    BAD_SOUND.set_volume(0.15)
                    BAD_SOUND.play()
                else:
                    score -= 200
                    bad_items.append(1)
                    BAD_SOUND.set_volume(0.15)
                    BAD_SOUND.play()

            keys_pressed = pygame.key.get_pressed()
            basket_movement_normal_hard(keys_pressed, basket)
            good_movement_normal_hard(roll, basket, good_items)
            good_movement_normal_hard(sashimi, basket, good_items)
            good_movement_normal_hard(ramen, basket, good_items)
            bad_movement_normal(wasabi, basket, bad_items)
            draw_window_easy_normal(basket, roll, wasabi, sashimi, ramen, score, timer)

        elif hard_mode:
            # countdown timer
            if timer > 0:
                count = pygame.time.get_ticks()
                if count - last_count > 1000:
                    timer -= 1
                    last_count = count
            if timer <= 0:
                end_message("Your Score is " + str(score) + "!")
                main()

            # keeping track of the score
            if event.type == COLLECT_GOOD and len(good_items) < MAX_COL:
                score += 100
                good_items.append(1)
                GOOD_SOUND.set_volume(0.5)
                GOOD_SOUND.play()
            if event.type == COLLECT_BAD and len(bad_items) < MAX_COL:
                if score < 200:
                    score = 0
                    bad_items.append(1)
                    BAD_SOUND.set_volume(0.15)
                    BAD_SOUND.play()
                else:
                    score -= 200
                    bad_items.append(1)
                    BAD_SOUND.set_volume(0.15)
                    BAD_SOUND.play()

            keys_pressed = pygame.key.get_pressed()
            basket_movement_normal_hard(keys_pressed, basket)
            good_movement_normal_hard(roll, basket, good_items)
            good_movement_normal_hard(sashimi, basket, good_items)
            good_movement_normal_hard(ramen, basket, good_items)
            bad_movement_hard(wasabi, basket, bad_items)
            bad_movement_hard(wasabi2, basket, bad_items)
            draw_window_hard(basket, roll, wasabi, wasabi2, sashimi, ramen, score, timer)

        if pygame.key.get_pressed()[pygame.K_SPACE]:
            main_menu = True
            score = 0
            timer = 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.QUIT()


if __name__ == "__main__":
    main()