field = list(range(1,10))

def playing_field(field):
   print("-" * 13)
   for i in range(3):
      print("|", field[0+i*3], "|", field[1+i*3], "|", field[2+i*3], "|")
      print("-" * 13)

def take_input(right_of_way):
   valid = False
   while not valid:
      response_move = input("Ход " + right_of_way+": ")
      try:
         response_move = int(response_move)
      except:
         print("Некорректный ввод. Вы уверены, что ввели число?")
         continue
      if response_move >= 1 and response_move <= 9:
         if(str(field[response_move-1]) not in "XO"):
            field[response_move-1] = right_of_way
            valid = True
         else:
            print("Эта клетка уже занята!")
      else:
        print("Некорректный ввод. Введите число от 1 до 9.")

def check_win(field):
   win_coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for each in win_coord:
       if field[each[0]] == field[each[1]] == field[each[2]]:
          return field[each[0]]
   return False

def main(field):
    counter = 0
    win = False
    while not win:
        playing_field(field)
        if counter % 2 == 0:
           take_input("X")
        else:
           take_input("O")
        counter += 1
        if counter > 4:
           tmp = check_win(field)
           if tmp:
              print(tmp, "выиграл!")
              win = True
              break
        if counter == 9:
            print("Ничья!")
            break
    playing_field(field)
main(field)

input("Нажмите Enter для выхода!")