class ComponenteArma {
  #limpio = true;
  constructor(material) {
    this.material = material;
  }
  get limpio() { return this.#limpio; }
  mantenimiento() {}
}

class MecanismoGatillo extends ComponenteArma {
  constructor(material, pesoPresionLbs) {
    super(material);
    this.pesoPresionLbs = pesoPresionLbs;
  }
  mantenimiento() {
    console.log(`Gatillo (${this.material}): Ajustado a ${this.pesoPresionLbs} lbs de presión. Limpio: ${this.limpio}`);
  }
}

const gatillo = new MecanismoGatillo("Polímero/Acero", 3.5);
gatillo.mantenimiento();