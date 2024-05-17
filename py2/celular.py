class Celular():
    bateria = 'infinita'
    tela = '4x3'
    tem_camera = True
    tem_botao = True
    tem_antena = True
    cor = 'cinza'
    modelo = 'tijolao'

    def ligacao(self):
        print('ligando.....')

    def mensagem(self):
        print('Enviando mensagem')

    def jogo_cobrinha(self):
        print('Jogando o jogo da cobrinha')


my_phone = Celular()

print(my_phone.bateria) 

my_phone.jogo_cobrinha()
