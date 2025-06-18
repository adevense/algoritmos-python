# contar quantas lintas presentes em args
def minha_funcao(a,b,*args):
    ''' print(args)
    for arg in args:
        print(f'- {arg}')'''
    for arg in args:
        if isinstance(arg, list):
            print(f'Lista: {arg}')
            

        

minha_funcao(1, 2, 3, 4,[5,6], [7,8,9])

