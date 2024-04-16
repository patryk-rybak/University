#! python3
# Patryk Rybak 333139

# Usage: py.exe main.py encryption <img_path> <message>
#        py.exe main.py decryption <img_message_path> <img_key_path>

# zeruje wszytkie najmniej znaczace bity odpowiadajace za barwy i na ich miejscach koduje wiadomosc
# wartosci pierwszego pixela pelnia funckje uwierzytelniajaca, drugi zmodyfikowany obraz musi miec w tym miejscu te same wartosci aby odkodowanie bylo mozliwe 

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import random
import sys
from PIL import Image


def messageToBinary(mess):
    return ''.join([format(ord(i), '08b') for i in mess])


def encryption(img_path, mess):
    x_img_mess = mpimg.imread(img_path)
    img_mess = np.array(x_img_mess)
    x_img_key = mpimg.imread(img_path)
    img_key = np.array(x_img_key)

    if img_mess.shape[0] * img_mess.shape[1] * 3  - 3 - img_mess.shape[0] < len(mess):
        print("The message is too large, try a lighter message or an img with a higher resolution")
        quit()

    for i in range(3):
        # creates 
        temp = random.randint(0, 255)
        img_mess[0][0][i] = temp
        img_key[0][0][i] = temp

    mess = messageToBinary(mess)
    for row in range(1, img_mess.shape[0]):
        for pixel in range(img_mess.shape[1]):
            for i in range(3):
                if mess == '':
                    img_mess[row][pixel][i] = int(format(img_mess[row][pixel][i], '08b')[:-1] + '0', 2)
                else:
                    img_mess[row][pixel][i] = int(format(img_mess[row][pixel][i], '08b')[:-1] + mess[0], 2)
                mess = mess[1:]

    return img_mess, img_key


def decryption(img_mess, img_key):
    ''' dla argumentow w postacji sciezek do jpg
    img_mess = mpimg.imread(img_mess)
    img_key = mpimg.imread(img_key)
    '''
    for i in range(3):
        if img_mess[0][0][i] != img_key[0][0][i]:
            print('Invalid key')
            quit()

    output = ''
    temp = ''
    for row in range(1, img_mess.shape[0]):
        for pixel in range(img_mess.shape[1]):
            for i in range(3):
                temp += format(img_mess[row][pixel][i], '08b')[-1]
                if len(temp) == 8:
                    if temp == '00000000': temp = ''
                    else:
                        output += chr(int(temp, 2))
                        temp = ''
    return output


if __name__ == '__main__':
    if len(sys.argv) < 3 or (sys.argv[1] != 'encryption' and sys.argv[1] != 'decryption'):
        print("Usage: py.exe main.py encryption <img_path> <message>\nUsage: py.exe main.py decryption <img_message_path> <img_key_path>")
    elif sys.argv[1] == 'encryption':
        message = ' '.join(sys.argv[3:])
        mess, key = encryption(sys.argv[2], message)

        f, (ax1, ax2) = plt.subplots(2, 1, constrained_layout=True)
        ax1.set_title("Original")
        ax1.imshow(mpimg.imread(sys.argv[2]))
        ax2.set_title("With message")
        ax2.imshow(mess)

        im = Image.fromarray(mess)
        im.save('mess.jpg')
        im2 = Image.fromarray(key)
        im2.save('key.jpg')

        
        print("Message: ", decryption(mess, key))
        #print(decryption('mess.jpg', 'key.jpg'))
        # z jakiegos powodu wczytane jpg maja inne wrtosci rbg niz te ustalone przed zapisem
        plt.show()
    elif sys.argv[1] == 'decryption':
        # ta czesc niestety nie dziala przez roznice miedzy zapisywanymi wartosciami rgb i odczytywanymi. Dlaczego one sie roznia???
        print(decryption(sys.argv[2], sys.argv[3]))
    else:
        print('Sth went wrong...')
    
