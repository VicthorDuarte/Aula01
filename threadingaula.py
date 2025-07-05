import threading
import time
from multiprocessing import Process
#Threads
def tarefa(nome):
    print(f'{nome} inciou')
    time.sleep(2)
    print(f'{nome} terminou')
    t1 = threading.Thread(target=tarefa, args=('Thread 1',))
    t2 = threading.Thread(target=tarefa, args=('Thread 2',))
    t3 = threading.Thread(target=tarefa, args=('Thread 3',))
    t4 = threading.Thread(target=tarefa, args=('Thread 4',))

    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t4.join()
    print('Todas as threads terminaram')
#utilizando threads em classes
class minha_thread(threading.Thread):
    def run(self):
        print(f'{self.name} trabalhando!')
        time.sleep(1)
t = minha_thread()
t.start()
t.join()

threads = []
for i in range(5):
     t = threading.Thread(target=tarefa, args=(f'Tarefa {i}',))
     t.start()
     threads.append(t)
     print(threads)
for t in threads:
    t.join()
#Lock threading
########################################################################
lock = threading.Lock()
contador = 0
def incrementar ():
    print(f'Thread : {threads}')
    global contador
    for i in range(100000):
        with lock:
            contador += +1
t1 = threading.Thread(target = incrementar)
t2 = threading.Thread(target = incrementar)
t1.start()
t2.start()
t1.join()
t2.join()
print("contador final:", contador)