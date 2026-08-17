from abc import ABC, abstractmethod

class ParteAvion(ABC):
    def __init__(self, nombre: str, estado: str):
        self.nombre = nombre
        self._estado = estado

    @abstractmethod
    def inspeccionar(self):
        pass

class Turbina(ParteAvion):
    def __init__(self, nombre: str, estado: str, empuje_lbs: int):
        super().__init__(nombre, estado)
        self.empuje_lbs = empuje_lbs

    def inspeccionar(self):
        print(f"Turbina '{self.nombre}': Estado {self._estado}, Empuje max: {self.empuje_lbs} lbs.")

class TrenDeAterrizaje(ParteAvion):
    def __init__(self, nombre: str, estado: str, esta_desplegado: bool):
        super().__init__(nombre, estado)
        self.esta_desplegado = esta_desplegado

    def inspeccionar(self):
        estado_tren = "Desplegado" if self.esta_desplegado else "Retraído"
        print(f"Tren de Aterrizaje '{self.nombre}': {estado_tren}.")

# Uso
turbina_izq = Turbina("Rolls-Royce Trent 1000", "Óptimo", 78000)
turbina_izq.inspeccionar()