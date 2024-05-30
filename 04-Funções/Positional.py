def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):

    print(modelo, ano, placa, marca, motor, combustivel)



#criar_carro(Modelo="Palio", ano=1999, Placa="ABC-1234", Marca="Fiat", motor="1.0", combustivel="Gasolina") 
criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")  
##
##
##
##

##Keyword only
                    
def criar_carro(*,modelo, ano, placa, marca, motor, combustivel):  #Desta forma é possivel dar nome as informações que serão inseridas

    print(modelo, ano, placa, marca, motor, combustivel)


 
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") 
#criar_carro("Palio", 1999, "ABC-1234", "Fiat", "1.0", "Gasolina")  #ESTE FORMATO FICA INVÁLIDO QUANDO COLOCAMOS * NO COMEÇO DA DECLARAÇÃO 



def criar_carro(modelo, ano, placa,/,*, marca, motor, combustivel):  #DESTA FORMA É POSSIVEL NOMEAR* E DEIXAR POR POSIÇÃO/
     print(modelo, ano, placa, marca, motor, combustivel)


 
criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #FORMATO VÁLIDO PORQUE NO INICIO É POR POSICAO E APOS * POR NOMES
#criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina") #FORMATO INVALIDO PORQUE TEM QUE SER HIBRIDO DE ACORDO COM A DECLARAÇÃO

