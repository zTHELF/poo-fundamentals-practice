class ComponenteCarro {
  #desgaste = 5;
  constructor(marca) {
    this.marca = marca;
  }
  get desgaste() { return this.#desgaste; }
  diagnosticar() { console.log(`Componente: ${this.marca}`); }
}

class Transmision extends ComponenteCarro {
  constructor(marca, tipo) { // tipo: "Manual" o "Automática"
    super(marca);
    this.tipo = tipo;
  }
  diagnosticar() {
    console.log(`Transmisión ${this.tipo} (${this.marca}): Desgaste al ${this.desgaste}%`);
  }
}

const caja = new Transmision("ZF", "Automática");
caja.diagnosticar();