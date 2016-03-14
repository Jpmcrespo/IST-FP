#Joao Pedro Crespo   Numero: 81811


# Este programa e' capaz de verificar se um numero de cartao de credito e' valido atraves da funcao verifica_cc e tambem gera numeros de cartoes de varias entidades atraves da funcao gera_num_cc


#DATA:

prim_dig=('1','2','3','4','5','6','7','8','9')
MII = ('Companhias aereas', 'Companhias aereas e outras tarefas futuras da industria', 'Viagens e entretenimento e bancario / financeiro', 'Servicos bancarios e financeiros', 'Servicos bancarios e financeiros', 'Merchandising e bancario / financeiro', 'Petroleo e outras atribuicoes futuras da industria', 'Saude, telecomunicacoes e outras atribuicoes futuras da industria', 'Atribuicao nacional')

inicio= (('4024', '4532', '4556'),('4026','426','4405','4508'),('5018', '5020', '5038'),('19','50','51','52','53','54'),('65',),('309','36','38','39'),('34','37'))
tamanho= ((16,13),(16,),(19,13),(16,),(16,),(14,),(15,))
empresa=('Visa','Visa Electron','Maestro','Master Card','Discover Card','Diners Club International','American Express')
rede= ('V','VE','M','MC','DC','DCI','AE')



#PARTE 1


def calc_soma(n):
        
        """Esta funcao recebe uma cadeia de carateres correspondente a um numero inteiro associado a um cartao de credito sem o ultimo digito. 
        a funcao calcula a soma de todos os digitos da cadeia de carateres da seguinte forma: primeiro inverte a cadeia, de seguida multiplica 
        por 2 os digitos que se encontram em posicoes impares. se os digitos multiplicados por 2 forem (estritamente) maiores que 9, o programa 
        subtrai 9 ao numero obtido e o resultado  e' o que conta para o calculo da soma dos digitos da cadeia de caracteres."""
        
        x=int(n)
        soma=0
        while x>0:              
                if (x%10)*2>=10:
                        soma = soma + (x%10)*2 - 9                      #em vez de inverter a cadeia e multiplicar os impares, fui de tras para a frente
                        x=x//10
                else:
                        soma = soma + (x%10)*2
                        x=x//10                      
                soma = soma +(x%10)
                x=x//10                    
        return(soma)


def luhn_verifica(c):
        
        """Esta funcao verifica se o numero de cartao e' valido de acordo com o algoritmo de luhn. Recorre a funcao "calc_soma" """
           
        y=int(c)                                #muda para inteiro
        res=y%10
        y=y//10
        y=str(y)                                #muda para string para funcionar com a "calc_soma"
        return (calc_soma(y) +res)%10==0 


def comeca_por(cad1,cad2):
        
        """Verifica se os primeiros elementos da primeira cadeia de caracteres correspondem aos elementos da segunda"""
        
        num_cad1=int(cad1)              
        num_cad2=int(cad2)
        while num_cad1>0:
                if num_cad1 == num_cad2:         
                        return True
                else:
                        num_cad1=num_cad1//10                        #enquanto a 1a cadeia nao for igual a 2a, ele vai "cortando" os ultimos numeros para chegar aos digitos iniciais
        return False


def comeca_por_um(cad, t_cads):
        
        """Verifica se a 1a cadeia comeca por um dos elementos do tuplo"""
        
        length=len(t_cads)
        for i in range(length):
                if comeca_por(cad, t_cads[i]):
                        return True
        return False


def valida_iin(x):
        
        """Funcao que determina qual a empresa a que corresponde o numero do cartao"""
        
        for i in range(len(inicio)):
                if len(x) in tamanho[i] and comeca_por_um(x,inicio[i]):
                        return empresa[i]
        return ''


def categoria(cat):
        
        """Analisa o primeiro digito da cadeia de carateres e devolve a categoria da entidade a que pertence"""
         
        if cat[0] in prim_dig:
                return MII[int(cat[0])-1]
        

def verifica_cc(cartao):
        
        """Funcao que verifica se o cartao e' valido para uma qualquer entidade"""
        
        cartao=str(cartao)
        if luhn_verifica(cartao) and valida_iin(cartao) != '':
                return (categoria(cartao) , valida_iin(cartao))
        else:
                return 'cartao invalido'


#PARTE 2
        
import random                                                         # importar a biblioteca random

def random_picker(tuplo):
        
        """Escolhe um elemento qualquer de um tuplo"""                # faz o mesmo que a random.choice
        
        escolha = tuplo[int(random.random()*len(tuplo))]
        return escolha


def gera_num_quase_cc(abreviatura):
        
        """Gera um numero de cartao de credito de acordo com a abreviatura que utilizador introduz"""
        
        numero=0
        
        for i in range(len(rede)):
                if abreviatura == rede[i]:
                        numero=numero + int(random_picker(inicio[i]))
                        len_escolha=len(str(numero))
                        tamanho_num=random_picker(tamanho[i])
                        numero=numero*10**(tamanho_num-1-len_escolha)+ int((random.random())*10**(tamanho_num-1-len_escolha))
                        return str(numero) 

def digito_verificacao(x):
        
        """Gera um digito de verificacao valido para o numero que o utilizador introduzir na funcao"""
        
        digito=10-(calc_soma(x)%10)
        if digito==10:
                digito=0
        return str(digito)


def gera_num_cc(cartao_final):
        
        """Junta as funcoes "gera_num_quase_cc" e "digito_verificacao" para devolver um numero de cartao de credito valido e completo""" 
        
        numero_inicial = gera_num_quase_cc(cartao_final)
        numero_final= numero_inicial + digito_verificacao(numero_inicial)
        return numero_final


#THE END  #linhas de codigo: 75 +/-