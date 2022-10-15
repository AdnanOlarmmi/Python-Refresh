# weight = int(input('Weight: '))
# weightUnit = input('(K)g or (L)bs: ')
# conversionRate = 0.45
#
# if weightUnit.lower() == 'k':
#     # print('Weight in L: ' + str(weight * conversionRate));
#     print(f'Weight in L: {weight / conversionRate}L')
# elif weightUnit.lower() == 'l':
#     # print('Weight in Kg: ' + str(weight / conversionRate))
#     print(f'Weight in Kg: {weight * conversionRate}Kg')

# secretNumber = 5
# i = 0
# while i < 3:
#     guess = int(input('Guess: '))
#     i += 1
#     if guess == secretNumber:
#         print("You are right")
#         break
# else:
#     print('You used up all trial')


# i = 1
# while i > 0:
#     control = input('>')
#     if control.lower() == 'help':
#         print('Start - to start car \nStop - to stop car \nQuit - to quit game')
#     elif control.lower() == 'start':
#         print('Car started, broom... broom...')
#     elif control.lower() == 'stop':
#         print('Car stopped, pss...')
#     elif control.lower() == 'quit':
#         print('Bye!...')
#         break
#     else:
#         print('Command not clear!')

# control = ''
# started = False;
# while True:
#     control = input('>').lower()
#     if control == 'help':
#         print('Start - to start car \nStop - to stop car \nQuit - to quit game')
#     elif control == 'start':
#         if started:
#             print('Car already started')
#         else:
#             started = True
#             print('Car started, broom... broom...')
#     elif control == 'stop':
#         if not started:
#             print('Car already stopped')
#         else:
#             started = False
#             print('Car stopped, pss...')
#     elif control == 'quit':
#         print('Bye!')
#         break
#     else:
#         print('Command not clear!')


# arr = [10, 20, 30]
# total = 0
# for item in arr:
#     total += item
#
# print(total)

# numbers = [2, 2, 2, 2, 5]
# for number in numbers:
#     output = ''
#     for i in range(number):
#         output += 'x'
#     print(output)

# numbers = [-2, -9, -5, -1]
# maxNum = numbers[0]
# for number in numbers:
#     if number > maxNum:
#         maxNum = number
# print(maxNum)

# arr = [4, 4, 4, 3, 3, 3, 1]
# newArr = []
#
# for item in arr:
#     # print(item)
#     # print(arr.count(item))
#     if item not in newArr:
#         # print(item)
#        newArr.append(item)
#
# print(newArr)

numbers = {"1": "One",
           "2": "Two",
           "3": "Three",
           "4": "Four",
           "5": "Five",
           "6": "Six",
           "7": "Seven",
           "8": "Eight",
           "9": "Nine",
           "0": "Zero",
           }
# phone = input('Phone: ')
# output = ""
# for ch in phone:
#     output += numbers.get(ch, "^") + " "
#
# print(output)

emoji = {
    ":)": "😀",
    ":(": "😒"
}


def emoji_converter(msg):
    words = msg.split(" ")
    output = ""
    for word in words:
        output += emoji.get(word, word) + " "
    return output


message = input("> :")
print(emoji_converter(message))
