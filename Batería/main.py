from abc import ABC, abstractmethod

class ComponenteBateria(ABC):
    def __init__(self, id_serie: str):
        self.id_serie = id_serie
        self._temperatura_c = 25.0

    @abstractmethod
    def verificar_salud(self):
        pass

class CeldaLitio(ComponenteBateria):
    def __init__(self, id_serie: str, voltaje_nominal: float):
        super().__init__(id_serie)
        self.voltaje_nominal = voltaje_nominal

    def verificar_salud(self):
        print(f"Celda [{self.id_serie}]: Voltaje {self.voltaje_nominal}V, Temp: {self._temperatura_c}°C")

class BMS(ComponenteBateria): # Building Management System / Controlador
    def __init__(self, id_serie: str, celdas_monitoreadas: int):
        super().__init__(id_serie)
        self.celdas_monitoreadas = celdas_monitoreadas

    def verificar_salud(self):
        print(f"BMS Controlador [{self.id_serie}]: Monitoreando {self.celdas_monitoreadas} celdas.")

# Uso
celda1 = CeldaLitio("CELL-001", 3.7)
celda1.verificar_salud()