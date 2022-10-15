control = ''
started = False;
while True:
    control = input('>').lower()
    if control == 'help':
        print('Start - to start car \nStop - to stop car \nQuit - to quit game')
    elif control == 'start':
        if started:
            print('Car already started')
        else:
            started = True
            print('Car started, broom... broom...')
    elif control == 'stop':
        if not started:
            print('Car already stopped')
        else:
            started = False
            print('Car stopped, pss...')
    elif control == 'quit':
        print('Bye!')
        break
    else:
        print('Command not clear!')
