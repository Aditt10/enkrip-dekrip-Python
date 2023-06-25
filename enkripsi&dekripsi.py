import string

abjad = string.printable

def enkrip(pesan) :
    global abjad
    
    key = int(input('masukan key               ;'))
    cipher = ''
    for i in pesan:
        if i in abjad:
            k = abjad.find(i)
            k = (k +key)%100
            cipher =cipher+abjad[k]
        else:
            cipher = cipher+i
    return cipher


def dekripsi(cipher):
    global abjad 
    key = int(input('masukan key        ;'))
    pesan = ''
    for i in cipher:
        if i in abjad:
            k = abjad.find(i)
            k = (k - key)%100
            pesan = pesan+abjad[k]
        else:
            pesan = pesan + i 
    return pesan
if __name__ == '__main__':
    print ('***************************************')
    print ('------------- Muhamad Aditia-----------')
    print ('***************************************')
    
    option =int(input('1.Enkripsi\n2. Dekripsi\npilih option             :'))
    if option == 1:
        pesan = input('masuka pesan (plaintext)')
        print(enkrip(pesan))
    elif option == 2:
        cipher = input('masukan pesan (chiphertext)')
        print(dekripsi(cipher))
    else :
        print('masukan option 1 atau 2!!')
        
        