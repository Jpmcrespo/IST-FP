#projeto 2
#Nuno Tomas 81718 
#Joao Crespo 81811

def cria_coordenada ( l , c ) :
    """cria_coordenada : int x int --> coordenada
    Operacao basica que cria um elemento do TAD coordenada"""
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
    """universal → logico
    Recebe um argumento e diz se o argumento e' do tipo coordenada""" 
    return arg in coordenada23

def coordenadas_iguais ( coordenada1 , coordenada2 ) :
    """coordenada x coordenada → lógico
    Recebe dois elementos do tipo coordenada e devolve True caso sejam iguais"""
    
    return coordenada_linha ( coordenada1 ) == coordenada_linha ( coordenada2 ) and coordenada_coluna ( coordenada2 ) == coordenada_coluna ( coordenada1 )

def cria_tabuleiro ( ) :
    """{} → tabuleiro
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


def tabuleiro_posicao ( t , c ) :
    """ tabuleiro × coordenada → inteiro
    recebe um elemento do tipo tabuleiro e um elemento do tipo coordenada e devolve um inteiro correspondente ao valor presente no tabuleiro na coordenada indicada"""
    if e_coordenada ( c ) :
        return t [ coordenada_linha ( c ) -1 ] [ coordenada_coluna ( c ) -1 ]

    else:
        raise ValueError ( "tabuleiro_posicao: argumentos invalidos" )

def tabuleiro_pontuacao ( t ) :
    """tabuleiro →int 
    recebe um elemento do tipo tabuleiro e devolve a respetiva pontuacao"""
    return t [ -1 ]

def tabuleiro_posicoes_vazias ( t ) :
    """tabuleiro → lista"""
    
    lista_final= [ ]
    for l in range ( len ( t ) -1 ) :
        for c in range ( len ( t [ l ] ) ) :
            if t [ l ] [ c ] == 0 :
                lista_final = lista_final + [ cria_coordenada ( l + 1 , c + 1 ) ]
    return lista_final

def tabuleiro_preenche_posicao( t , c , v ) :
    if isinstance ( v , int ) and v >= 0 and e_coordenada ( c ) :
        t [ coordenada_linha ( c ) -1 ] [ coordenada_coluna ( c ) -1 ] = v
        return t
    else:
        raise ValueError ( "tabuleiro_preenche_posicao: argumentos invalidos" )    

def tabuleiro_actualiza_pontuacao ( t , v ) :
    if isinstance ( v , int ) and v >= 0 and v % 4 == 0 :
        t [ -1 ] = tabuleiro_pontuacao ( t ) + v
        return t
    else:
        raise ValueError ( "tabuleiro_actualiza_pontuacao: argumentos invalidos" )
    
def e_tabuleiro ( t ) :
    Flag = True
    if isinstance ( t , list ) and len ( t ) == 5 and isinstance ( t [ 4 ] , int ) :
        for i in range ( 4 ) :
            if isinstance ( t [ i ] , list ) and len ( t [ i ] ) == 4 :
                for e in range ( len ( t [ i ] ) ) :
                    Flag = isinstance ( t [ i ] [ e ] , int ) * Flag
            else:
                Flag = False
    else:
        Flag = False
    return Flag == 1
        
def tabuleiros_iguais ( t1 , t2 ) :
    return t1 == t2

def escreve_tabuleiro ( t ) :
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
    
direcoes = ( 'N' , 'S', 'W' , 'E' )
z=[[2,4,2,4],
   [2,2,2,2],
   [2,4,4,4],
   [4,2,4,2],4]

def tabuleiro_reduz ( t , d ) :
    def mexe ( t , a , b , c , d ) :
        puxa ( t , a , b , c , d , 3 )
        junta ( t , a , b , c , d)
        puxa ( t , a , b , c , d , 3 )
        
    def puxa ( t , a , b , c , d , x ) :
        if x == 0 :
            return t
        else:                         
            for i in a :
                for e in b :
                    if tabuleiro_posicao(t, cria_coordenada(i, e))==0 :
                        if cria_coordenada ( i + c , e + d ) not in tabuleiro_posicoes_vazias ( t ) :
                                tabuleiro_preenche_posicao ( t , cria_coordenada ( i , e ) , tabuleiro_posicao ( t , cria_coordenada ( i + c , e + d ) ) ) 
                                tabuleiro_preenche_posicao ( t , cria_coordenada ( i + c , e + d ) , 0 )
                                
        return puxa ( t , a , b , c , d , x - 1 )
    
    def junta ( t , a , b , c , d):
        for i in a:
            for e in b :
                if tabuleiro_posicao(t, cria_coordenada ( i , e )) == tabuleiro_posicao(t, cria_coordenada ( i + c , e + d )):
                    tabuleiro_preenche_posicao ( t, cria_coordenada ( i , e ), 2* tabuleiro_posicao(t, cria_coordenada( i+c , e+d )))
                    tabuleiro_preenche_posicao ( t , cria_coordenada ( i + c , e + d ) , 0 )
                    tabuleiro_actualiza_pontuacao (t, tabuleiro_posicao(t, cria_coordenada( i , e )))
                                                                                                                                                
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
    lista_final = [ ]
    lista_aux = [ ]
    for i in range ( 4 ) :
        for e in range ( 4 ) :
            lista_aux = lista_aux + [ t[i][e] ]
        lista_final = lista_final + [ lista_aux ]
        lista_aux= [ ]
    lista_final += [tabuleiro_pontuacao(t)]
    return lista_final

def tabuleiro_terminado ( t ) :
    tabuleiro_antigo=copia_tabuleiro (t)
    if tabuleiro_posicoes_vazias ( t ) == [ ] :
        for i in direcoes :
            tabuleiro_reduz (t, i )
        return tabuleiro_pontuacao(tabuleiro_antigo)== tabuleiro_pontuacao(t)  
    else:
        return False
    
def pede_jogada ():
    i = str(input('Introduza uma jogada (N, S, E, W): ') )
    if i not in direcoes:
        print('Jogada invalida.')
        return pede_jogada()
    else:
        return i
    
from random import random
        
def preenche_posicao_aleatoria ( t ) :    
    if tabuleiro_posicoes_vazias ( t ) != 0:
        ran=int(random()*100)
        y=len(tabuleiro_posicoes_vazias(t)) 
        x=int(random()*y)
        if ran<80:
            return tabuleiro_preenche_posicao (t, tabuleiro_posicoes_vazias(t)[x], 2)
        else:
            return tabuleiro_preenche_posicao (t, tabuleiro_posicoes_vazias(t)[x], 4)
        
def jogo_2048():
    t = preenche_posicao_aleatoria ( preenche_posicao_aleatoria ( cria_tabuleiro() ) )
    escreve_tabuleiro(t)
    while not tabuleiro_terminado(t): 
        copia=copia_tabuleiro(t)
        jog = pede_jogada()
        tabuleiro_reduz(t, jog)
        if not tabuleiros_iguais(t, copia):                 
            t = preenche_posicao_aleatoria(t)
        escreve_tabuleiro(t)