class ComponenteBateria {
  #temperatura = 24.5;
  constructor(idSerie) {
    this.idSerie = idSerie;
  }
  get temperatura() { return this.#temperatura; }
  verificarSalud() {}
}

class Electrolito extends ComponenteBateria {
  constructor(idSerie, tipoQuimico) {
    super(idSerie);
    this.tipoQuimico = tipoQuimico;
  }
  verificarSalud() {
    console.log(`Electrolito [${this.idSerie}] (${this.tipoQuimico}): Temp actual ${this.temperatura}°C`);
  }
}

const liquido = new Electrolito("ELEC-A", "Polímero de Litio");
liquido.verificarSalud();