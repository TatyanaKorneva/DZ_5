import random
number_of_candies = int(input('введите количество конфет для игры: '))
gamer1 = input('введите имя 1 игрока: ')
gamer2 = "Bot"
current_gamer = gamer1
while number_of_candies > 0:
    print('количество оставшихся конфет: {}'.format(number_of_candies))
    while True:
        if current_gamer == gamer1:
            number_to_delete = int(input('ход игрока {} (1 - 28): '.format(current_gamer)))
        else:
            if number_of_candies>=28:
                number_to_delete=random.randint(1, 28)
            else:
                number_to_delete=random.randint(1, number_of_candies)
            print("ход игрока {} (1 - 28): {}".format(current_gamer, number_to_delete))
        if number_to_delete >= 1 and number_to_delete <= 28:
            break
    number_of_candies -= number_to_delete
    current_gamer = gamer2 if current_gamer == gamer1 else gamer1
print('Победил {}'.format(current_gamer))