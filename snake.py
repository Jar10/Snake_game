import pygame
import random

# Inisialisasi Pygame
pygame.init()

# Ukuran layar
screen_width = 1000
screen_height = 600

# Warna
black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 255, 0)
red = (255, 0, 0)

# Ukuran dan kecepatan ular
snake_size = 20
snake_speed = 10

# Level kesulitan
easy_speed = 10
medium_speed = 15
hard_speed = 20

# Membuat layar
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Nostalgia")

clock = pygame.time.Clock()

# Gambar latar belakang
background_image = pygame.image.load("go'a.png").convert()
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

# Fungsi untuk menampilkan pesan teks
def show_message(text, color, font_size, x, y):
    font = pygame.font.Font(pygame.font.get_default_font(), font_size)
    message = font.render(text, True, color)
    screen.blit(message, (x, y))

# Fungsi untuk menggambar ular
def draw_snake(snake_list):
    for snake in snake_list:
        pygame.draw.rect(screen, green, (snake[0], snake[1], snake_size, snake_size))
        pygame.draw.rect(screen, black, (snake[0], snake[1], snake_size, snake_size), 2)

# Fungsi untuk menggambar tembok
def draw_walls():
    # Garis atas
    pygame.draw.line(screen, white, (0, 0), (screen_width, 0), 2)
    # Garis bawah
    pygame.draw.line(screen, white, (0, screen_height - 1), (screen_width, screen_height - 1), 2)
    # Garis kiri
    pygame.draw.line(screen, white, (0, 0), (0, screen_height), 2)
    # Garis kanan
    pygame.draw.line(screen, white, (screen_width - 1, 0), (screen_width - 1, screen_height), 2)

# Fungsi utama game
def game_loop():
    game_over = False
    game_quit = False

    # Koordinat awal ular
    x = screen_width / 2
    y = screen_height / 2

    # Perubahan koordinat ular
    dx = 0
    dy = 0

    # List koordinat badan ular
    snake_list = []
    snake_length = 1

    # Koordinat makanan
    food_x = round(random.randrange(0, screen_width - snake_size) / 20) * 20
    food_y = round(random.randrange(0, screen_height - snake_size) / 20) * 20

    # Skor
    score = 0

    # Level kesulitan
    level = "easy"
    
    # Kecepatan ular berdasarkan level kesulitan
    if level == "easy":
        snake_speed = easy_speed
    elif level == "medium":
        snake_speed = medium_speed
    elif level == "hard":
        snake_speed = hard_speed


    while not game_quit:
        while game_over:
            screen.blit(background_image, (0, 0))
            show_message("Game Over! Press C to Play Again or Q to Quit", red, 36, 150, 250)
            show_message("Score: " + str(score), white, 24, 350, 300)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_quit = True
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_quit = True
                        game_over = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_quit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx != snake_size:
                    dx = -snake_size
                    dy = 0
                elif event.key == pygame.K_RIGHT and dx != -snake_size:
                    dx = snake_size
                    dy = 0
                elif event.key == pygame.K_UP and dy != snake_size:
                    dx = 0
                    dy = -snake_size
                elif event.key == pygame.K_DOWN and dy != -snake_size:
                    dx = 0
                    dy = snake_size
                elif event.key == pygame.K_a and dx != snake_size:
                    dx = -snake_size
                    dy = 0
                elif event.key == pygame.K_d and dx != -snake_size:
                    dx = snake_size
                    dy = 0
                elif event.key == pygame.K_w and dy != snake_size:
                    dx = 0
                    dy = -snake_size
                elif event.key == pygame.K_s and dy != -snake_size:
                    dx = 0
                    dy = snake_size
                elif event.key == pygame.K_1:
                    level = "easy"
                    snake_speed = easy_speed
                elif event.key == pygame.K_2:
                    level = "medium"
                    snake_speed = medium_speed
                elif event.key == pygame.K_3:
                    level = "hard"
                    snake_speed = hard_speed

        if 0 <= x < screen_width and 0 <= y < screen_height:
            x += dx
            y += dy
        else:
            game_over = True

        screen.blit(background_image, (0, 0))
        pygame.draw.rect(screen, red, (food_x, food_y, snake_size, snake_size))

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]

        for segment in snake_list[:-1]:
            if segment == snake_head:
                game_over = True

        draw_snake(snake_list)
        draw_walls()

        if x == food_x and y == food_y:
            food_x = round(random.randrange(0, screen_width - snake_size) / 20) * 20
            food_y = round(random.randrange(0, screen_height - snake_size) / 20) * 20
            snake_length += 1
            score += 1

        show_message("Score: " + str(score), white, 24, 10, 10)
        show_message("Level: " + level, white, 24, 10, 40)

        pygame.display.update()
        clock.tick(snake_speed)

    pygame.quit()

# Menjalankan game
game_loop()
