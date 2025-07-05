from multiprocessing import Process, Queue
import datetime

#utilizando o multiprocessing
'''
def tarefa(nome):
    print(f'{nome} inciou')
    print(datetime.datetime.now())
    print(f'{nome} terminou')
if __name__ == "__main__":
    p1 = Process(target = tarefa, args =("Processo 1",))
    p2  = Process(target = tarefa, args =("Processo 2",))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
'''
#Multi processing sando o pool
################################
'''def quadrado(x):
    print(datetime.datetime.now())
    return x*x

if __name__ == '__main__':
    with Pool(4) as pool: #Criando 4 processos
        resultados = pool.map(quadrado, [1,2,3,4,5])
        print(resultados)
    print(f'Todos os processos terminaram em: {datetime.datetime.now()}')'''
#Controle de execução usand Queue
##############################
'''def produtor(q):
    q.put('Mensagem o produtor: Olá consumidor')

def consumidor(q):
    msg = q.get()
    print('consumidor recebeu:', msg)
if __name__ == '__main__':
    q = Queue()
    p1 = Process(target= produtor, args = (q,))
    p2 = Process(target =consumidor, args = (q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()'''

