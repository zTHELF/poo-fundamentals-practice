from abc import ABC, abstractmethod

class ComponenteArma(ABC):
    def __init__(self, material: str):
        self.material = material
        self._limpio = True

    @abstractmethod
    def Mantenimiento(self):
        pass

class Canon(ComponenteArma):
    def __init__(self, material: str, longitud_pulgadas: float):
        super().__init__(material)
        self.longitud_pulgadas = longitud_pulgadas

    def Mantenimiento(self):
        print(f"Cañón de {self.material} ({self.longitud_pulgadas}\"): Limpieza realizada. Estado pulcro.")

class Cargador(ComponenteArma):
    def __init__(self, material: str, capacidad_balas: int):
        super().__init__(material)
        self.capacidad_balas = capacidad_balas

    def Mantenimiento(self):
        print(f"Cargador ({self.material}) cap: {self.capacidad_balas} tiros: Resorte verificado.")

# Uso
canon = Canon("Acero Inoxidable", 16.5)
canon.Mantenimiento()