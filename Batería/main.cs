using System;

public abstract class ComponenteBateria {
    public string IdSerie { get; set; }
    protected double Temperatura { get; set; } = 25.0;

    public ComponenteBateria(string idSerie) { IdSerie = idSerie; }
    public abstract void VerificarSalud();
}

public class CeldaLitio : ComponenteBateria {
    public double CapacidadAh { get; set; }
    public CeldaLitio(string id, double cap) : base(id) { CapacidadAh = cap; }

    public override void VerificarSalud() {
        Console.WriteLine($"Celda {IdSerie} ({CapacidadAh} Ah): Temp {Temperatura}°C");
    }
}

class Program {
    static void Main() {
        ComponenteBateria c = new CeldaLitio("CEL-99", 2.5);
        c.VerificarSalud();
    }
}