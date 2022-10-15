




i = 1
while i > 0:
    control = input('>')
    if control.lower() == 'help':
        print('Start - to start car \nStop - to stop car \nQuit - to quit game')
    elif control.lower() == 'start':
        print('Car started, broom... broom...')
    elif control.lower() == 'stop':
        print('Car stopped, pss...')
    elif control.lower() == 'quit':
        print('Bye!...')
        break
    else:
        print('Command not clear!')










