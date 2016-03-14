calc_soma('34')
def calc_soma(n):
        x=eval(n)        
        soma=0
        while x>0:   
                
                if (x%10)*2>=10:
                        soma = soma + (x%10)*2 - 9
                        x=x//10
                else:
                        soma = soma + (x%10)*2
                        x=x//10                      
                soma = soma +(x%10)
                x=x//10                    
        return(soma)
        
def luhn_verifica(c):
        y=eval(c)
        res=y%10
        y=y//10
        y=str(y)
        return (calc_soma(y) +res)%10==0 


def comeca_por(cad1,cad2):
        num_cad1=eval(cad1)
        num_cad2=eval(cad2)
        lencad1=len(cad1)
        while lencad1>len(cad2):
                num_cad1=num_cad1//10
                lencad1=lencad1-1
        return num_cad1==num_cad2

def comeca_por_um(cad,t_cads):
        for i in range(len(t_cads)):
                comeca_por(cad,t_cads[i])
                return cad == t_cads[i]
