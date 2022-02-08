escolha = str(input('Encriptar(a) ou decriptar(b)?'))


def letter(msg, new, x, cod, letra):
    if msg[x] == letra:
            new = new + cod
    return new        


def crypt(msg):
    x = 0
    tam = len(msg)
    newmsg = ''
    while x != tam:
        newmsg = letter(msg, newmsg, x, '123', 'a')
        newmsg = letter(msg, newmsg, x, '329', 'b')
        newmsg = letter(msg, newmsg, x, '231', 'c')
        newmsg = letter(msg, newmsg, x, '435', 'd')
        newmsg = letter(msg, newmsg, x, '019', 'e')
        newmsg = letter(msg, newmsg, x, '358', 'f')
        newmsg = letter(msg, newmsg, x, '906', 'g')
        newmsg = letter(msg, newmsg, x, '235', 'h')
        newmsg = letter(msg, newmsg, x, '783', 'i')
        newmsg = letter(msg, newmsg, x, '007', 'j')
        newmsg = letter(msg, newmsg, x, '832', 'k')
        newmsg = letter(msg, newmsg, x, '921', 'l')
        newmsg = letter(msg, newmsg, x, '865', 'm')
        newmsg = letter(msg, newmsg, x, '101', 'n')
        newmsg = letter(msg, newmsg, x, '412', 'o')
        newmsg = letter(msg, newmsg, x, '888', 'p')
        newmsg = letter(msg, newmsg, x, '242', 'q')
        newmsg = letter(msg, newmsg, x, '355', 'r')
        newmsg = letter(msg, newmsg, x, '331', 's')
        newmsg = letter(msg, newmsg, x, '515', 't')
        newmsg = letter(msg, newmsg, x, '727', 'u')
        newmsg = letter(msg, newmsg, x, '928', 'v')
        newmsg = letter(msg, newmsg, x, '456', 'w')
        newmsg = letter(msg, newmsg, x, '132', 'x')
        newmsg = letter(msg, newmsg, x, '646', 'y')
        newmsg = letter(msg, newmsg, x, '987', 'z')
        newmsg = letter(msg, newmsg, x, 'eee', 'é')
        newmsg = letter(msg, newmsg, x, 'aaa', 'ã')
        newmsg = letter(msg, newmsg, x, '000', ' ')
        newmsg = letter(msg, newmsg, x, '003', '!')
        newmsg = letter(msg, newmsg, x, '002', ',')
        newmsg = letter(msg, newmsg, x, '001', '.')
        x+=1    
    return newmsg    

def reverseletter(msg, new, x, cod, letra):
    digitos = msg[x] + msg[x+1] + msg[x+2]
    if digitos == cod:
        new = new + letra   
    return new

def decrypt(msg):
    x = 0
    tam = len(msg)
    checa = tam%3
    newmsg = str('')
    if checa != 0:
        print('Isso não é um código rcrypt...')
    else:
        while x!= tam:
         newmsg = reverseletter(msg, newmsg, x, '123', 'a')
         newmsg = reverseletter(msg, newmsg, x, '329', 'b')
         newmsg = reverseletter(msg, newmsg, x, '231', 'c')
         newmsg = reverseletter(msg, newmsg, x, '435', 'd')
         newmsg = reverseletter(msg, newmsg, x, '019', 'e')
         newmsg = reverseletter(msg, newmsg, x, '358', 'f')
         newmsg = reverseletter(msg, newmsg, x, '906', 'g')
         newmsg = reverseletter(msg, newmsg, x, '235', 'h')
         newmsg = reverseletter(msg, newmsg, x, '783', 'i')
         newmsg = reverseletter(msg, newmsg, x, '007', 'j')
         newmsg = reverseletter(msg, newmsg, x, '832', 'k')
         newmsg = reverseletter(msg, newmsg, x, '921', 'l')
         newmsg = reverseletter(msg, newmsg, x, '865', 'm')
         newmsg = reverseletter(msg, newmsg, x, '101', 'n')
         newmsg = reverseletter(msg, newmsg, x, '412', 'o')
         newmsg = reverseletter(msg, newmsg, x, '888', 'p')
         newmsg = reverseletter(msg, newmsg, x, '242', 'q')
         newmsg = reverseletter(msg, newmsg, x, '355', 'r')
         newmsg = reverseletter(msg, newmsg, x, '331', 's')
         newmsg = reverseletter(msg, newmsg, x, '515', 't')
         newmsg = reverseletter(msg, newmsg, x, '727', 'u')
         newmsg = reverseletter(msg, newmsg, x, '928', 'v')
         newmsg = reverseletter(msg, newmsg, x, '456', 'w')
         newmsg = reverseletter(msg, newmsg, x, '132', 'x')
         newmsg = reverseletter(msg, newmsg, x, '646', 'y')
         newmsg = reverseletter(msg, newmsg, x, '987', 'z')
         newmsg = reverseletter(msg, newmsg, x, 'eee', 'é')
         newmsg = reverseletter(msg, newmsg, x, 'aaa', 'ã')
         newmsg = reverseletter(msg, newmsg, x, '000', ' ')
         newmsg = reverseletter(msg, newmsg, x, '003', '!')
         newmsg = reverseletter(msg, newmsg, x, '002', ',')
         newmsg = reverseletter(msg, newmsg, x, '001', '.')
         x+=3
        return newmsg 
                



if escolha == 'a':
  msg = str(input('Me fala uma mensagem: '))  
  cod = crypt(msg)
  print(cod)
            
elif escolha == 'b':
  msg = str(input('Me fala uma mensagem: '))  
  cod = decrypt(msg)
  print(cod)
    
    