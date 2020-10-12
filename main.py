import random

if __name__ == '__main__':
    print('РОЗЫГРЫШ 1 КГ ПЕЛЬМЕНЕЙ!!!')
    participants = []

    # adding participants to list
    while len(participants) < 3:
        in_list = True

        print('Введите имя')
        name = input()
        participants.append(name)

    print('Вот наш список участников:')
    for key, participant in enumerate(participants):
        print(f'{key + 1}. {participant}')
    print('Кому же достенутся вкуснейшие пельмени????')

    start = True
    while start:
        print('Начать розыгрыш? (да/нет)')
        answer = input()
        if answer == 'да':
            winner = participants[random.randint(0, len(participants) - 1)]
            print(f'Победителем становится: {winner}, ему достается 1кг сочных пельменей!')
            start = False
