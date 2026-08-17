from abc import ABC, abstractmethod

class ComponenteCarro(ABC):
    def __init__(self, marca: str):
        self.marca = marca
        self._desgaste_porcentaje = 0

    @abstractmethod
    def diagnosticar(self):
        pass

class Motor(ComponenteCarro):
    def __init__(self, marca: str, cilindros: int):
        super().__init__(marca)
        self.cilindros = cilindros

    def diagnosticar(self):
        print(f"Motor {self.marca} ({self.cilindros} cilindros): Desgaste al {self._desgaste_porcentaje}%")

class SistemaFrenos(ComponenteCarro):
    def __init__(self, marca: str, es_abs: bool):
        super().__init__(marca)
        self.es_abs = es_abs

    def diagnosticar(self):
        tipo = "ABS" if self.es_abs else "Estándar"
        print(f"Frenos {self.marca} [{tipo}]: Desgaste de pastillas al {self._desgaste_porcentaje}%")

# Uso
frenos = SistemaFrenos("Brembo", True)
frenos.diagnosticar()