from abc import ABC, abstractmethod
from functools import wraps
comodos = []
Dispositivos = []
Id = []
class comodosclass(ABC):
    pass
class comodos_abstract(comodosclass):
    def setarcomodos(self, nome):
        self.nome = nome

class Dispositivosclass(ABC):
    pass

class Dispositivos_info(Dispositivosclass):
    def informacoes(self, nome, device_id):
        self.nome = nome
        self.device_id = device_id
class Painelcontrole():
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Painelcontrole, cls).__new__(cls)
            cls._instance.comodos = comodos
            cls._instance.dispositivos = Dispositivos
            cls._instance.ids = Id
        return cls._instance

    def adicionar_comodo(self, nome):
        comodo = comodos_abstract()
        comodo.setarcomodos(nome)
    def adicionar_comodo(self, nome):
        comodo = comodos_abstract()
        comodo.setarcomodos(nome)
        self.comodos.append(comodo.nome)

    def adicionar_dispositivo(self, nome, device_id):
        dispositivo = Dispositivos_info()
        dispositivo.informacoes(nome, device_id)
        self.dispositivos.append(dispositivo.nome)
        self.ids.append(dispositivo.device_id)

    def listar_comodos(self):
        return self.comodos

    def listar_dispositivos(self):
        return list(zip(self.dispositivos, self.ids))
    
    def log_acesso(func):
        @wraps(func)
        def wrapper(self, *args, **kwargs):
            print(f"[LOG] {func.__name__} chamado para {self}")
            print( wrapper)
            return func(self, *args, **kwargs)
    
class Dispositivo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

    @abstractmethod
    def status(self):
        pass

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

class Lampada(Dispositivo):
    def __init__(self, nome, device_id):
        self.nome = nome
        self.device_id = device_id
        self._ligada = False

    @Painelcontrole.log_acesso
    def ligar(self):
        self._ligada = True

    @Painelcontrole.log_acesso
    def desligar(self):
        self._ligada = False

    def status(self):
        return "Ligada" if self._ligada else "Desligada"

    def __eq__(self, other):
        return isinstance(other, Lampada) and self.device_id == other.device_id

    def __repr__(self):
        return f"Lampada(nome={self.nome}, id={self.device_id}, status={self.status()})"

    def __str__(self):
        return f"Lâmpada '{self.nome}' [{self.device_id}] - {self.status()}"

class Termostato(Dispositivo):
    def __init__(self, nome, device_id):
        self.nome = nome
        self.device_id = device_id
        self._ligado = False
        self.temperatura = 22

    @Painelcontrole.log_acesso
    def ligar(self):
        self._ligado = True

    @Painelcontrole.log_acesso
    def desligar(self):
        self._ligado = False

    def status(self):
        return f"Ligado ({self.temperatura}°C)" if self._ligado else "Desligado"

    def __eq__(self, other):
        return isinstance(other, Termostato) and self.device_id == other.device_id

    def __repr__(self):
        return f"Termostato(nome={self.nome}, id={self.device_id}, status={self.status()})"

    def __str__(self):
        return f"Termostato '{self.nome}' [{self.device_id}] - {self.status()}"

class Camera(Dispositivo):
    def __init__(self, nome, device_id):
        self.nome = nome
        self.device_id = device_id
        self._ligada = False

    @Painelcontrole.log_acesso
    def ligar(self):
        self._ligada = True

    @Painelcontrole.log_acesso
    def desligar(self):
        self._ligada = False

    def status(self):
        return "Gravando" if self._ligada else "Desligada"

    def __eq__(self, other):
        return isinstance(other, Camera) and self.device_id == other.device_id

    def __repr__(self):
        return f"Camera(nome={self.nome}, id={self.device_id}, status={self.status()})"

    def __str__(self):
        return f"Câmera '{self.nome}' [{self.device_id}] - {self.status()}"

class Fechadura(Dispositivo):
    def __init__(self, nome, device_id):
        self.nome = nome
        self.device_id = device_id
        self._trancada = True

    @Painelcontrole.log_acesso
    def ligar(self):
        self._trancada = False

    @Painelcontrole.log_acesso
    def desligar(self):
        self._trancada = True

    def status(self):
        return "Trancada" if self._trancada else "Destrancada"

    def __eq__(self, other):
        return isinstance(other, Fechadura) and self.device_id == other.device_id

    def __repr__(self):
        return f"Fechadura(nome={self.nome}, id={self.device_id}, status={self.status()})"

    def __str__(self):
        return f"Fechadura '{self.nome}' [{self.device_id}] - {self.status()}"

class DispositivoCriar:
    tipos = {
        "lampada": Lampada,
        "termostato": Termostato,
        "camera": Camera,
        "fechadura": Fechadura,
    }

    @classmethod
    def registrar_tipo(cls, nome, classe):
        cls.tipos[nome.lower()] = classe

    @classmethod
    def criar(cls, tipo, nome, device_id):
        tipo = tipo.lower()
        if tipo in cls.tipos:
            return cls.tipos[tipo](nome, device_id)
        raise ValueError(f"Tipo de dispositivo '{tipo}' não registrado.")

class Comodo:
    def __init__(self, nome):
        self.nome = nome
        self.dispositivos = []

    def adicionar_dispositivo(self, dispositivo):
        if dispositivo not in self.dispositivos:
            self.dispositivos.append(dispositivo)

    def __add__(self, other):
        novo = Comodo(f"{self.nome} + {other.nome}")
        ids = {d.device_id for d in self.dispositivos}
        novo.dispositivos = self.dispositivos[:]
        for d in other.dispositivos:
            if d.device_id not in ids:
                novo.dispositivos.append(d)
        return novo

    def __eq__(self, other):
        return set(d.device_id for d in self.dispositivos) == set(d.device_id for d in other.dispositivos)

    def __repr__(self):
        return f"Comodo(nome={self.nome}, dispositivos={self.dispositivos})"

    def __str__(self):
        return f"Cômodo '{self.nome}' com {len(self.dispositivos)} dispositivos"

    def __len__(self):
        return len(self.dispositivos)

    def __contains__(self, dispositivo):
        return dispositivo in self.dispositivos

    def ligar_todos(self):
       pass

    def desligar_todos(self):
        pass

class CentralControle:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(CentralControle, cls).__new__(cls)
            cls._instance.comodos = []
            cls._instance.device_ids = set()
        return cls._instance

    def adicionar_comodo(self, comodo):
        self.comodos.append(comodo)

    def adicionar_dispositivo(self, comodo, dispositivo):
        if dispositivo.device_id in self.device_ids:
            print(f"Dispositivo com ID {dispositivo.device_id} já cadastrado!")
            return
        comodo.adicionar_dispositivo(dispositivo)
        self.device_ids.add(dispositivo.device_id)

    def ligar_todos(self):
        for comodo in self.comodos:
            comodo.ligar_todos()

    def desligar_todos(self):
        for comodo in self.comodos:
            comodo.desligar_todos()

    def __repr__(self):
        return f"CentralControle(comodos={self.comodos})"

    def __str__(self):
        return f"Central de Controle com {len(self.comodos)} cômodos"

class Cenario:
    def __init__(self, nome, comandos):
        self.nome = nome
        self.comandos = comandos

    def executar(self):
        print(f"Executando cenário: {self.nome}")
        for comando in self.comandos:
            comando()

if __name__ == "__main__":

    sala = Comodo("Sala")
    quarto = Comodo("Quarto")
    cozinha = Comodo("Cozinha")

    lamp1 = DispositivoCriar.criar("lampada", "Luz Sala", 1)
    lamp2 = DispositivoCriar.criar("lampada", "Luz Quarto", 2)
    term1 = DispositivoCriar.criar("termostato", "Termostato Sala", 3)
    cam1 = DispositivoCriar.criar("camera", "Câmera Cozinha", 4)
    fech1 = DispositivoCriar.criar("fechadura", "Fechadura Entrada", 5)

    central1 = CentralControle()
    central2 = CentralControle()
    print("Singleton funcionando?", central1 is central2)

    central1.adicionar_comodo(sala)
    central1.adicionar_comodo(quarto)
    central1.adicionar_comodo(cozinha)

    central1.adicionar_dispositivo(sala, lamp1)
    central1.adicionar_dispositivo(quarto, lamp2)
    central1.adicionar_dispositivo(sala, term1)
    central1.adicionar_dispositivo(cozinha, cam1)
    central1.adicionar_dispositivo(sala, fech1)

    print(sala)
    print("Lampada 1 está na sala?", lamp1 in sala)
    print("Dispositivos na sala:", len(sala))
    print("Sala == Quarto?", sala == quarto)
    sala_quarto = sala + quarto
    print("Sala + Quarto:", sala_quarto)

    central1.ligar_todos()
    central1.desligar_todos()

    cenario_noturno = Cenario("Modo Noturno", [
        
    ])
    cenario_noturno.executar()

    class sensorTemperatura(Dispositivo):
        def __init__(self, nome, device_id):
            self.nome = nome
            self.device_id = device_id
            self._ativo = True

        @Painelcontrole.log_acesso
        def ligar(self):
            self._ativo = True

        @Painelcontrole.log_acesso
        def desligar(self):
            self._ativo = False

        def status(self):
            return "Ativo" if self._ativo else "Inativo"

        def __eq__(self, other):
            return isinstance(other, sensorTemperatura) and self.device_id == other.device_id

        def __repr__(self):
            return f"sensorTemperatura(nome={self.nome}, id={self.device_id}, status={self.status()})"

        def __str__(self):
            return f"Sensor de temperatura '{self.nome}' [{self.device_id}] - {self.status()}"

    DispositivoCriar.registrar_tipo("sensorTemperatura", sensorTemperatura)
    sensor1 = DispositivoCriar.criar("sensorTemperatura", "Sensor Cozinha", 29)
    central1.adicionar_dispositivo(cozinha, sensor1)
    print(sensor1)
