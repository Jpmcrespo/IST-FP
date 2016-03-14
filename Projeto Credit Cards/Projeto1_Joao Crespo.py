#Joao Pedro Crespo   Numero: 81811


# Este programa e capaz de verificar se um numero de cartao de credito e valido atraves da funcao verifica_cc e tambem gera numeros de cartoes de varias entidades atraves da funcao gera_num_cc


#PARTE 1



def calc_soma(n):
        
        
        """Esta funcao recebe uma cadeia de carateres correspondente a um numero inteiro associado a um cartao de credito sem o ultimo digito. a funcao calcula a soma de todos os digitos da cadeia de carateres da seguinte forma: primeiro inverte a cadeia, de seguida multiplica por 2 os digitos que se encontram em posicoes impares. se os digitos multiplicados por 2 forem (estritamente) maiores que 9, o programa subtrai 9 ao numero obtido e o resultado  e o que conta para o calculo da soma dos digitos da cadeia de caracteres."""
        
        
        x=int(n)
        soma=0
        while x>0:              
                if (x%10)*2>=10:
                        soma = soma + (x%10)*2 - 9                      #em vez de inverter e multiplicar os impares, fui de tras para a frente
                        x=x//10
                else:
                        soma = soma + (x%10)*2
                        x=x//10                      
                soma = soma +(x%10)
                x=x//10                    
        return(soma)


def luhn_verifica(c):
        
        """ esta funcao verifica se o numero de cartao e valido de acordo com o algoritmo de luhn. Recorre a funcao "calc_soma" """
        
        
        y=int(c)                                #muda para inteiro
        res=y%10
        y=y//10
        y=str(y)                                #muda para string para funcionar com a "calc_soma"
        return (calc_soma(y) +res)%10==0 


def comeca_por(cad1,cad2):
        
        """verifica se os primeiros elementos da primeira cadeia de caracteres correspondem aos elementos da segunda"""
        
        num_cad1=int(cad1)              
        num_cad2=int(cad2)
        while num_cad1>0:
                if num_cad1 == num_cad2:         
                        return True
                else:
                        num_cad1=num_cad1//10                        #enquanto a 1a cadeia nao for igual a 2a, ele vai "cortando" os ultimos numeros para chegar aos digitos iniciais
        return False


def comeca_por_um(cad, t_cads):
        
        
        """verifica se a 1a cadeia comeca por um dos elementos do tuplo"""
        
        length=len(t_cads)
        for i in range(length):
                if comeca_por(cad, t_cads[i]):
                        return True

        return False


def valida_iin(card): 
        
        """analisa o tamanho da cadeia e os seus carateres iniciais e devolve a rede emissora a que pertence"""
        
        
        if len(card) == 16 and comeca_por_um(card,('4026', '426','4405','4508')):         #modo compacto, sem espacos desnecessarios
                return 'Visa Electron'
        elif len(card) in (16,13) and comeca_por_um(card,('4024', '4532', '4556')):
                return 'Visa'
        elif len(card) == 16 and comeca_por_um(card,('19','50','51','52','53','54')):
                return 'Master Card'
        elif len(card) in (19,13) and comeca_por_um(card,('5018', '5020', '5038')):
                return 'Maestro'
        elif len(card) == 16 and comeca_por_um(card,('65',)):
                return 'Discover Card'
        elif len(card) == 14 and comeca_por_um(card,('309','36','38','39')):
                return 'Diners Club International'
        elif len(card) == 15 and comeca_por_um(card,('34','37')):
                return 'American Express'
        else:
                return ''


def categoria(cat):
        
        
        """analisa o primeiro digito da cadeia de carateres e devolve a categoria da entidade a que pertence"""
        
        
        if cat[0] == '1':
                return 'Companhias aereas'                                              #modo compacto, sem espacos desnecessarios
        elif cat[0] == '2':
                return 'Companhias aereas e outras tarefas futuras da industria'
        elif cat[0] == '3':
                return 'Viagens e entretenimento e bancario / financeiro'        
        elif cat[0] in ('4','5'):
                return 'Servicos bancarios e financeiros'  
        elif cat[0] == '6':
                return 'Merchandising e bancario / financeiro'
        elif cat[0] == '7':
                return 'Petroleo e outras atribuicoes futuras da industria'        
        elif cat[0] == '8':
                return 'Saude, telecomunicacoes e outras atribuicoes futuras da industria'        
        elif cat[0] == '9':
                return 'Atribuicao nacional'
        

def verifica_cc(cartao):
        
        
        """ funcao que verifica se o cartao e valido para uma qualquer entidade"""
        
        
        cartao=str(cartao)
        if luhn_verifica(cartao) and valida_iin(cartao) != '':
                return (categoria(cartao) , valida_iin(cartao))
        else:
                return 'cartao invalido'



#PARTE 2
        
import random                                                           # importar a biblioteca random


def gera_num_quase_cc(rede):
        
        
        """ gera um numero de cartao de credito correspondente a abreviatura que o utilizador introduziu como cadeia de carateres mas sem o ultimo digito (o de verificacao)"""
        
        
        numero=0
        if rede == 'AE':                                                #aqui a escolha dos expoentes e dado pelo numero de caracteres que o numero deve ter menos o tamanho da cadeia de caracteres do random(choice)
                numero= numero+random.choice((34,37))
                len_escolha=len(str(numero))
                numero= numero*10**(14-len_escolha) + int((random.random())*10**(14-len_escolha))
                return str(numero)  
        
        
        elif rede == 'DCI':
                numero= numero+random.choice((309,36,38,39))
                len_escolha=len(str(numero))
                numero= numero*10**(13-len_escolha) + int((random.random())*10**(13-len_escolha))
                return str(numero)
        
        
        elif rede == 'DC':
                numero= numero+random.choice((65,))                     
                len_escolha=len(str(numero))
                numero= numero*10**(15-len_escolha) + int((random.random())*10**(15-len_escolha))
                return str(numero) 
        
        
        elif rede == 'M':
                numero= numero+random.choice((5018,5020,5038))
                len_escolha=len(str(numero))
                len_numero=random.choice((18,12))
                numero= numero*10**(len_numero-len_escolha) + int((random.random())*10**(len_numero-len_escolha))
                return str(numero)
        
        
        elif rede == 'MC':
                numero= numero+random.choice((50,51,52,53,54,19))      
                len_escolha=len(str(numero))
                numero= numero*10**(15-len_escolha) + int((random.random())*10**(15-len_escolha))
                return str(numero) 
        
        
        elif rede == 'VE':
                numero= numero+random.choice((4026,426,4405,4508,))      
                len_escolha=len(str(numero))
                numero= numero*10**(15-len_escolha) + int((random.random())*10**(15-len_escolha))
                return str(numero)
        
        
        elif rede == 'V':
                numero= numero+random.choice((4024,4532,4556))
                len_escolha=len(str(numero))
                len_numero=random.choice((12,15))
                numero= numero*10**(len_numero-len_escolha) + int((random.random())*10**(len_numero-len_escolha))
                return str(numero)        


def digito_verificacao(x):
        
        
        """ gera um digito de verificacao valido para o numero que o utilizador introduzir na funcao"""
        
        
        digito=10-(calc_soma(x)%10)
        if digito==10:
                digito=0
        return str(digito)


def gera_num_cc(cartao_final):
        
        
        """junta as funcoes "gera_num_quase_cc" e "digito_verificacao" para devolver um numero de cartao de credito valido e completo""" 
        
        
        numero_inicial = gera_num_quase_cc(cartao_final)
        numero_final= numero_inicial + digito_verificacao(numero_inicial)
        return numero_final


#THE END