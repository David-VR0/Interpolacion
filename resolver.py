from math import factorial
def delta(elementosy,n):
    restas=[]
    for i in range (0,n-1):
        restas.append(round(elementosy[i+1]-elementosy[i],4))
    return restas

def ObteniendoConstante(delta,h,n,e):
    resultadosConstantes=[]
    resultadosConstantes.append(e)
    for i in range (0,n-1):
        resultadosConstantes.append(round(delta[i][0]/(factorial(i+1)*pow(h,i+1)),4))
    return resultadosConstantes

def final(constante,elementosx,px):
    valor=constante[0]
    for i in range(1,len(elementosx)):
        x=1
        for j in range(0,i):
            x=x*(px-elementosx[j])
        valor+=constante[i]*x
    return valor


def inicio(elementosx,elementosy,n, px):
    IgualmenteEspaciados = True
    h=elementosx[1]-elementosx[0]
    deltas=[]
    espacios=elementosx[1]-elementosx[0]
    for i in range(1,n-1):
        if(espacios+elementosx[i]!=elementosx[i+1]):
            IgualmenteEspaciados = False
    if(IgualmenteEspaciados):
        deltaAux=elementosy
        for i in range(0,n-1):
            deltas.append(delta(deltaAux,n-i))
            deltaAux=deltas[i]


        constante = (ObteniendoConstante(deltas,h,n,elementosy[0]))

        resultado=final(constante,elementosx,px)


        return deltas,constante,resultado, IgualmenteEspaciados
    else:
        return 0,0,0,IgualmenteEspaciados