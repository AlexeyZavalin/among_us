import random

COLORS = ['red', 'green', 'blue', 'white', 'brown', 'black', 'pink', 'purple', 'lightgreen', 'lightblue']


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
        while len(impostors_indexes) < impostors_amount:
            index_ = random.randint(0, len(players_list) - 1)
            if index_ not in impostors_indexes:
                impostors_indexes.append(index_)
        for impostors_index in impostors_indexes:
            players_list[impostors_index]['is_impostor'] = True
    return players_list


if __name__ == '__main__':
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
    for i in range(players_amount):
        name = f'player_{i + 1}'
        player = {
            'id': i + 1,
            'name': name,
            'color': COLORS[i],
            'is_impostor': False
        }
        players.append(player)

    # начинаем игру (создаем предателей)
    players = create_impostors(players, impostors_amount)
    if impostors_amount == 1:
        print('There is 1 impostor among us')
    else:
        print(f'There is {impostors_amount} impostor among us')

    # выводим усписок участников
    for player in players:
        print(f'{player["id"]}. {player["name"]} - {player["color"]}')

    # играем
    while 0 < impostors_amount < len(players) - impostors_amount:
        print('**********\nОставшиеся участники\n************')
        for player in players:
            print(f'{player["id"]}. {player["name"]} - {player["color"]}')
        print('Как вы думаете, кто предатель?')
        potential_impostor_id = int(input())
        # выбор номера участника
        player_to_kill = None

        # находим индекс участника
        for index, player in enumerate(players):
            if player['id'] == potential_impostor_id:
                player_to_kill = index
                break

        # убираем игрока из списка
        if player_to_kill is not None:
            if players[player_to_kill]['is_impostor']:
                print(f'{players[player_to_kill]["name"]} оказался предателем')
                impostors_amount = impostors_amount - 1
            else:
                print(f'{players[player_to_kill]["name"]} не был предателем')
            del players[player_to_kill]
        print(f'Осталось предателей: {impostors_amount} \n')

    # выводим результаты игры
    if impostors_amount == 0:
        print('*********\nПОБЕДА!!!\n**********')
    else:
        print('*********\nПоражение\n**********')
    for player in players:
        print(f'{player["id"]}. {player["name"]} - {player["color"]} - {"предатель" if player["is_impostor"] else "не предатель"}')
