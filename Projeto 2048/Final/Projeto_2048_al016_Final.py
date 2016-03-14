#Nuno Tomas 81718   Joao Crespo 81811   grupo: al016


#O TAD coordenada sera utilizado para indexar as varias posicoes do tabuleiro. Cada posicao do tabuleiro e indexada atraves da linha respetiva (um inteiro entre 1 e 4) e da coluna respetiva (um inteiro entre 1 e 4), em que a posicao (1,1) corresponde ao canto superior esquerdo do tabuleiro


#---------------------------------------------------------------------------------------#
#                                       COORDENADAS                                     #
#---------------------------------------------------------------------------------------#

def cria_coordenada ( l , c ) :
    
    """cria_coordenada : int x int --> coordenada
    Operacao basica que cria um elemento do TAD coordenada e verifica se os argumentos sao numeros inteiros ou nao"""
    
    if 0 < l < 5 and 0 < c < 5 and isinstance ( l , int ) and isinstance ( c , int ):
            return ( l , c )
        
    else:
        raise ValueError ( "cria_coordenada: argumentos invalidos" )
    
def coordenada_linha ( coordenada ) :

    """coordenada --> inteiro
    Operacao basica que recebe um elemento do tipo coordenada e devolve o numero da linha correspondente"""

    return coordenada [ 0 ]
    
def coordenada_coluna ( coordenada ) :

    """coordenada --> inteiro
    Operacao basica que recebe um elemento do tipo coordenada e devolve o numero da coluna correspondente"""    
    
    return coordenada [ 1 ]

coordenada23 = [cria_coordenada(1,1), cria_coordenada(1,2),
              cria_coordenada(1,3), cria_coordenada(1,4),
              cria_coordenada(2,1), cria_coordenada(2,2),
              cria_coordenada(2,3), cria_coordenada(2,4),
              cria_coordenada(3,1), cria_coordenada(3,2),
              cria_coordenada(3,3), cria_coordenada(3,4),
              cria_coordenada(4,1), cria_coordenada(4,2),
              cria_coordenada(4,3), cria_coordenada(4,4)]              
    
def e_coordenada ( arg ) :

    """universal --> logico
    Recebe um argumento e diz se o argumento e do tipo coordenada23 em cima definida""" 
    
    return arg in coordenada23

def coordenadas_iguais ( coordenada1 , coordenada2 ) :

    """coordenada x coordenada --> logico
    Recebe dois elementos do tipo coordenada e devolve True caso sejam iguais e False caso contrario"""
    
    return coordenada_linha ( coordenada1 ) == coordenada_linha ( coordenada2 ) and coordenada_coluna ( coordenada2 ) == coordenada_coluna ( coordenada1 )


#---------------------------------------------------------------------------------------#
#                                       TABULEIRO                                       #
#---------------------------------------------------------------------------------------#

def cria_tabuleiro ( ) :

    """{} --> tabuleiro
    Funcao que nao recebe argumentos e que cria um tabuleiro vazio do jogo 2048"""
    
    lista_final = [ ]                               
    lista_aux = [ ]
    for i in range ( 4 ) :
        for e in range ( 4 ) :
            lista_aux = lista_aux + [ 0 ]
        lista_final = lista_final + [ lista_aux ]
        lista_aux= [ ]
    lista_final= lista_final + [ 0 ]
    return lista_final

    #cria uma lista assim: [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], 0] que corresponde a representacao interna do tabuleiro de jogo

def tabuleiro_posicao ( t , c ) :

    """ tabuleiro x coordenada --> inteiro
    Recebe um elemento do tipo tabuleiro e um elemento do tipo coordenada e devolve um inteiro correspondente ao valor presente no tabuleiro na coordenada indicada"""
    
    if e_coordenada ( c ) :
        return t [ coordenada_linha ( c ) -1 ] [ coordenada_coluna ( c ) -1 ]

    else:
        raise ValueError ( "tabuleiro_posicao: argumentos invalidos" )

def tabuleiro_pontuacao ( t ) :

    """tabuleiro --> int 
    Recebe um elemento do tipo tabuleiro e devolve a respetiva pontuacao"""
    
    return t [ -1 ]     #Desde que deixemos a pontuacao na ultima posicao, o tabuleiro pode ter as linhas que quisermos

def tabuleiro_posicoes_vazias ( t ) :

    """tabuleiro --> lista
    Recebe um elemento do tipo tabuleiro e devolve a lista com as posicoes vazias desse mesmo tabuleiro"""
    
    lista_final= [ ]
    for l in range ( len ( t )-1):
        for c in range ( len ( t [ l ] ) ) :
            if tabuleiro_posicao(t,cria_coordenada(l+1,c+1)) == 0 :                                                
                lista_final = lista_final + [ cria_coordenada ( l + 1 , c + 1 ) ]
    return lista_final

def tabuleiro_preenche_posicao( t , c , v ) :

    """tabuleiro x coordenada x inteiro --> tabuleiro
    Recebe um elemento do tipo tabuleiro, um elemento do tipo coordenada e um inteiro, e modifica o tabuleiro com o inteiro na coordenada correspondente"""
    
    if isinstance ( v , int ) and v >= 0 and e_coordenada ( c ) :
        t [ coordenada_linha ( c ) -1 ] [ coordenada_coluna ( c ) -1 ] = v
        return t
    
    else:
        raise ValueError ( "tabuleiro_preenche_posicao: argumentos invalidos" )    

def tabuleiro_actualiza_pontuacao ( t , v ) :

    """tabuleiro x inteiro --> tabuleiro
    Recebe um elemento do tipo tabuleiro e um inteiro nao negativo multiplo de 4 e modifica o tabuleiro acrescentando ao valor da respetica pontuacao"""
    
    if isinstance ( v , int ) and v >= 0 and v % 4 == 0 :
        t [ -1 ] = tabuleiro_pontuacao ( t ) + v
        return t
    
    else:
        raise ValueError ( "tabuleiro_actualiza_pontuacao: argumentos invalidos" )
    
def e_tabuleiro ( t ) :

    """ universal --> logico
    Recebe um elemento do tipo argumento e devolve True se o argumento for do tipo tabuleiro e False caso contrario """
    
    Flag = True
    if isinstance ( t , list ) and len ( t ) == 5 and isinstance ( t [ -1 ] , int ) :
        for i in range ( len(t)-1 ) :
            if isinstance ( t [ i ] , list ) and len ( t [ i ] ) == 4 :
                for e in range ( len ( t [ i ] ) ) :
                    Flag = isinstance ( tabuleiro_posicao(t, cria_coordenada(i+1, e+1)) , int ) * Flag
            else:
                Flag = False
    else:
        Flag = False
    return Flag == 1
        
def tabuleiros_iguais ( t1 , t2 ) :

    """tabuleiro x tabuleiro --> logico
    Recebe dois elementos do tipo tabuleiro e devolve True caso os tabuleiros tenham a mesma configuracao e pontucao e False caso contrario"""
    
    return t1 == t2

def escreve_tabuleiro ( t ) :

    """tabuleiro --> {} 
    Recebe um elemento do tipo tabuleiro e devolve a represntacao externa do tabuleiro de 2048"""
    
    str_aux = ''
    if e_tabuleiro ( t ) :
        for i in range ( 1,5 ) :
            for e in range ( 1,5 ) :
                str_aux = str_aux + '[ ' + str(tabuleiro_posicao(t, cria_coordenada (i,e) )) + ' ] '
            print ( str_aux )
            str_aux= ''
        print ('Pontuacao:' , tabuleiro_pontuacao ( t ) )
    else:
        raise ValueError ('escreve_tabuleiro: argumentos invalidos')
    
direcoes = ( 'N' , 'S', 'W' , 'E' )   #direcoes dos movimentos (norte, sul, este, oeste)

def tabuleiro_reduz ( t , d ) :

    """ tabuleiro x cad.caracteres --> tabuleiro
    Recebe um elemento do tipo tabuleiro e uma cadeia de caracteres correspondente a uma das 4 acoes possiveis ('N','S','W','E',). O tabuleiro reduz na direcao das 4 acoes possiveis modificando-o"""
    
    #primeiro puxa os numeros para a direcao indicada para ficarem todos juntos, depois soma os iguais e depois volta a puxar os numeros

    def mexe ( t , a , b , c , d ) :
        puxa ( t , a , b , c , d , 3 )          #3 vezes porque os numeros podem mexer-se um maximo de 3 vezes
        junta ( t , a , b , c , d)
        puxa ( t , a , b , c , d , 3 )
        
    def puxa ( t , a , b , c , d , x ) :
        if x == 0 :
            return t
        else:                         
            for i in a :                                                                                               
                for e in b :
                    if tabuleiro_posicao(t, cria_coordenada(i, e))==0 :
                        if cria_coordenada ( i + c , e + d ) not in tabuleiro_posicoes_vazias ( t ) :                                                           #se houver posicoes vazias 'a frente' do numero, move o numero para a posicao vazia
                                tabuleiro_preenche_posicao ( t , cria_coordenada ( i , e ) , tabuleiro_posicao ( t , cria_coordenada ( i + c , e + d ) ) )      
                                tabuleiro_preenche_posicao ( t , cria_coordenada ( i + c , e + d ) , 0 )                                                        #e preenche a posicao onde estava o numero com um 0
                                
        return puxa ( t , a , b , c , d , x - 1 )
    
    def junta ( t , a , b , c , d):
        for i in a:
            for e in b :
                if tabuleiro_posicao(t, cria_coordenada ( i , e )) == tabuleiro_posicao(t, cria_coordenada ( i + c , e + d )):                                  
                    tabuleiro_preenche_posicao ( t, cria_coordenada ( i , e ), 2* tabuleiro_posicao(t, cria_coordenada( i+c , e+d )))           #soma os numeros iguais
                    tabuleiro_preenche_posicao ( t , cria_coordenada ( i + c , e + d ) , 0 )                                                    # preenche a posicao que se moveu com um 0
                    tabuleiro_actualiza_pontuacao (t, tabuleiro_posicao(t, cria_coordenada( i , e )))                                           #actualiza a pontuacao de acordo com o novo numero gerado   
                                                                                                                                                
    if d == 'N' :
        mexe ( t , range ( 1 , 4 ) , range ( 1 , 5 ) , 1 , 0 )          
    elif d == 'S' :
        mexe ( t , range ( 4 , 1 , -1 ) , range ( 1 , 5 ) , -1 , 0 )
    elif d == 'E' :                                                         
        mexe ( t , range ( 1 , 5 ) , range ( 4 , 1 , -1 ) , 0 , -1 )
    elif d == 'W' :
        mexe ( t , range ( 1 , 5 ) , range ( 1 , 4 ) , 0 , 1 )
    else:
        raise ValueError('tabuleiro_reduz: argumentos invalidos')
        
    return t 

def copia_tabuleiro(t):

    """tabuleiro --> tabuleiro
    Recebe um elemento do tipo tabuleiro e devolve uma copia do mesmo"""
    
    lista_final = [ ]                                   #copia_tabuleiro tem que criar um novo elemento do tipo tabuleiro, percorrendo todos os elementos
    lista_aux = [ ]                                     # do tabuleiro original, senao quando mudamos o tabuleiro original, mudamos tambem a copia
    for i in range ( 4 ) :
        for e in range ( 4 ) :
            lista_aux = lista_aux + [ t[i][e] ]
        lista_final = lista_final + [ lista_aux ]
        lista_aux= [ ]
    lista_final += [tabuleiro_pontuacao(t)]
    return lista_final

def tabuleiro_terminado ( t ) :

    """tabuleiro --> logico
    Recebe um elemento do tipo tabuleiro e devolve True caso o tabuleiro nao tenha mais movimentos possiveis e False caso contrario"""
    
    tabuleiro_antigo=copia_tabuleiro (t)
    if tabuleiro_posicoes_vazias ( t ) == [ ]:       # primeiro ve se o tabuleiro tem alguma posicao vazia, se tiver, nao esta terminado
        for i in direcoes :
            tabuleiro_reduz (t, i )                 #reduz para todas as direcoes, par ver se e possivel fazer alguma jogada
        return tabuleiro_pontuacao(tabuleiro_antigo)== tabuleiro_pontuacao(t)    #se for possivel, a pontuacao vai ser alterada
    else:
        return False
    
def pede_jogada ():

    """pede_jogada() --> cad.caracteres
    Nao recebe qualquer argumento e apenas pede para introduzir uma direcao das 4 opcoes possiveis usadas do tabuleiro_reduz. Caso invalido pede novamente para introduzir a direcao"""
    
    i = str(input('Introduza uma jogada (N, S, E, W): ') )
    if i not in direcoes:
        print('Jogada invalida.')
        return pede_jogada()
    else:
        return i
    
from random import random
        
def preenche_posicao_aleatoria ( t ) : 

    """Recebe um elemento do tipo tabuleiro e preenche uma posicao livre, aleatoriamente, com o numero 2 ou 4"""
    
    if tabuleiro_posicoes_vazias ( t ) != 0:
        ran=int(random()*100)               #determinar se vai preencher com 2 ou com 4          
        y=len(tabuleiro_posicoes_vazias(t)) 
        x=int(random()*y)                   #determinar em que posicao do tabuleiro vai ser preenchido
        if ran<80:                          #80% de probabilidade de ser o numero 2 
            return tabuleiro_preenche_posicao (t, tabuleiro_posicoes_vazias(t)[x], 2)
        else:
            return tabuleiro_preenche_posicao (t, tabuleiro_posicoes_vazias(t)[x], 4)


#---------------------------------------------------------------------------------------#
#                                       JOGO                                            #
#---------------------------------------------------------------------------------------#
        
        
def jogo_2048():

    """jogo_2048 --> {}
    Nao recebe qualquer argumento e permite jogar o jogo completo de 2048"""

    t = preenche_posicao_aleatoria ( preenche_posicao_aleatoria ( cria_tabuleiro() ) )      #comeca por preencher 2 posicoes aleatorias com 2 ou 4
    escreve_tabuleiro(t)                                                                    
    while not tabuleiro_terminado(t):               #enquanto o tabuleiro nao esta terminado, ou seja, enquanto o jogo nao acabou:
        copia=copia_tabuleiro(t)
        jog = pede_jogada()
        tabuleiro_reduz(t, jog)
        if not tabuleiros_iguais(t, copia):         #so preenche a posicao aleatoria se o tabuleiro for alterado, por exemplo, 
            t = preenche_posicao_aleatoria(t)       #se as pecas nao puderem ser movidas para cima e carregarmos 'N', o tabuleiro fica igual
        escreve_tabuleiro(t)
    
    
#THE END
