number_of_candies = int(input('введите количество конфет: '))
gamer1, gamer2 = input('введите имя 1 игрока: '), input('введите имя 2 игрока: ')
current_gamer = gamer1
while number_of_candies > 0:
    print('количество оставшихся конфет: {}'.format(number_of_candies))
    while True:
        number_to_delete = int(input('ход игрока {} (1 - 28): '.format(current_gamer)))
        if number_to_delete >= 1 and number_to_delete <= 28:
            break
    number_of_candies -= number_to_delete
    current_gamer = gamer2 if current_gamer == gamer1 else gamer1

print('Победил {}'.format(current_gamer))