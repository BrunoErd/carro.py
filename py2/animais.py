class Animal:
    quantidade_patas = 4
    tem_rabo = True
    especie = ''
    sexo = 'macho'

    class Cachorro:
        tem_rabo = True
        especie = 'Canis lupus familiaris'
        raca = 'Shitzu'
        nome = 'Sérgio'
        porte = 'Pequeno'

        def latir(self):
            return "auauauauauauauauauauauauauau"
        
        def comer(self):
            return 'NhamNhami'
        
        def dormir(self):
            return 'ZZZZZZZ'
        


meu_cachorro = Animal.Cachorro()


print(meu_cachorro.latir())
print(meu_cachorro.comer())
print(meu_cachorro.dormir())
