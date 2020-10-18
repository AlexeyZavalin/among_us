import random
import pygame
import time

COLORS = ('red', 'green', 'blue', 'white', 'brown', 
          'black', 'pink', 'purple', 'lightgreen', 'lightblue')


def create_impostors(players_list, impostors_amount_):
    """
    :param players_list: list of dictionaries with participants
    :param impostors_amount_: integer number for impostors count
    :return: changed players list with impostors
    """
    # выбираем случайного участника, если всего 1 предатель
    if impostors_amount_ == 1:
        players_list[random.randint(0, len(players_list) - 1)]['is_impostor'] = True
    # выбираем несколько случайных участников, если предателей больше одного
    else:
        impostors_indexes = []
        while len(impostors_indexes) < impostors_amount_:
            index_ = random.randint(0, len(players_list) - 1)
            if index_ not in impostors_indexes:
                impostors_indexes.append(index_)
        for impostors_index in impostors_indexes:
            players_list[impostors_index]['is_impostor'] = True
    return players_list


def draw_text(screen, text, coords=(350, 350), color=(1, 2, 3), size=70):
    """
    add text on screen
    :param screen: pygame window
    :param text: string text to show
    :param coords: tuple coords for text
    :param color: rgb tuple color for text
    :param size: int size for text
    :return:
    """
    font = pygame.font.Font(None, size)
    text = font.render(text, True, color)
    screen.blit(text, coords)


def main():
    pygame.init()

    # вводим количество предателей
    print('Сколько будет предателей? от 1 до 3')
    impostors_amount = int(input())

    # минимальное число участников
    min_players_amount = 4

    if impostors_amount == 2:
        min_players_amount = 7
    elif impostors_amount == 3:
        min_players_amount = 9

    print(f'Сколько всего будет игроков? от {min_players_amount} до 10:')
    players_amount = int(input())
    while players_amount < min_players_amount or players_amount > 10:
        print(f'Вы ввели неверное количество игроков, введите еще раз. от {min_players_amount} до 10:')
        players_amount = int(input())

    # заполняем список участников
    players = []
    sum_widths = (100 * players_amount) + (15 * players_amount - 1)
    left = int((1200 - sum_widths) / 2)
    for i in range(players_amount):
        name = f'player_{i + 1}'
        bottom = 400 + random.randint(-20, 20)
        player = {
            'id': i + 1,
            'name': name,
            'color': COLORS[i],
            'is_impostor': False,
            'coords': (left, bottom)
        }
        left = left + 115
        players.append(player)

    # начинаем игру (создаем предателей)
    players = create_impostors(players, impostors_amount)

    color = (60, 93, 169)
    size = (1200, 600)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Among Us')
    done = False
    while 0 < impostors_amount < len(players) - impostors_amount and not done:
        for player in players:
            print(f'{player["color"]} - {player["is_impostor"]}')
        # создаем экран и заполняем его объектами
        screen.fill(color)
        rects = []
        for i, player in enumerate(players):
            player_img = pygame.image.load(f'imgs/{player["color"]}.png')
            player_rect = player_img.get_rect(bottomleft=player['coords'])
            rects.append(player_rect)
            screen.blit(player_img, player_rect)
            draw_text(screen, 'Кто предатель?', coords=(350, 100))
            pygame.display.update()

        click_on_player = False

        while not click_on_player:
            # проверяем событие
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    click_on_player = True
                    done = True

                # если кликнули ЛКМ
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        picked_player = None
                        for i, player in enumerate(players):
                            # проверили, кликнули ли мы по игроку
                            if rects[i].collidepoint(pygame.mouse.get_pos()):
                                picked_player = players[i]

                        if picked_player:
                            click_on_player = True
                            player_to_kill = None
                            for index, player in enumerate(players):
                                if player['id'] == picked_player['id']:
                                    player_to_kill = index
                                    break
                            # убираем игрока из списка
                            if player_to_kill is not None:
                                if players[player_to_kill]['is_impostor']:
                                    impostors_amount = impostors_amount - 1
                                    screen.fill(color)
                                    draw_text(screen, 'Этот игрок оказался предателем!')
                                    pygame.display.update()
                                    time.sleep(2)
                                else:
                                    screen.fill(color)
                                    draw_text(screen, 'Этот игрок не был предателем!')
                                    pygame.display.update()
                                    time.sleep(2)
                                del players[player_to_kill]
    # Проверка итогов игры
    if impostors_amount == 0:
        screen.fill(color)
        draw_text(screen, 'Победа', size=150)
        pygame.display.update()
        time.sleep(3)
    else:
        screen.fill(color)
        draw_text(screen, 'Поражение', size=150)
        pygame.display.update()
        time.sleep(3)


if __name__ == '__main__':
    main()
