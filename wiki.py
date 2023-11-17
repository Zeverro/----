import wikipedia
wikipedia.set_lang('ru')
#print(ny.section('География'))
k=0
kk=0
while k==0:
    G = input()
    
    print (wikipedia.search(G))
    while kk==0:
        GG = (input('Выберите: '))
        if GG in wikipedia.search(G):
            self = wikipedia.page(GG)
            print ('- ', self.title)
            print (self.summary)
            print ('-', '  |', self.url, '|')
            kk=1
        else:
            print('Пожалуйста выберите из списка!')
    kk=0
    
    
