class ParteAvion {
  #estado;
  constructor(nombre, estado) {
    this.nombre = nombre;
    this.#estado = estado;
  }
  get estado() { return this.#estado; }
  inspeccionar() { console.log(`Parte: ${this.nombre}`); }
}

class Ala extends ParteAvion {
  constructor(nombre, estado, longitudMetros) {
    super(nombre, estado);
    this.longitudMetros = longitudMetros;
  }
  inspeccionar() {
    console.log(`Ala '${this.nombre}': ${this.longitudMetros}m de largo. Estado: ${this.estado}`);
  }
}

const alaIzquierda = new Ala("Ala Izquierda Principal", "Operativa", 35);
alaIzquierda.inspeccionar();