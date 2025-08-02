from multiprocessing import Process, Queue

def produtor(q):
    q.put("mensagem do produtor")

def consumidor(q):
    msg = q.get()
    print("Consumidor recebeu:", msg)

if __name__ == '__main__':
    q = Queue()
    p1 = Process(target=produtor, args=(q,))
    p2 = Process(target=consumidor, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()