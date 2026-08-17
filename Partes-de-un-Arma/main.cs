using System;

public abstract class ComponenteArma {
    public string Material { get; set; }
    protected bool Limpio { get; set; } = true;

    public ComponenteArma(string material) { Material = material; }
    public abstract void Mantenimiento();
}

public class Canon : ComponenteArma {
    public string Calibre { get; set; }
    public Canon(string material, string calibre) : base(material) { Calibre = calibre; }

    public override void Mantenimiento() {
        Console.WriteLine($"Cañón calibre {Calibre} ({Material}): Inspeccionado y limpio.");
    }
}

class Program {
    static void Main() {
        ComponenteArma c = new Canon("Titanio", "9mm");
        c.Mantenimiento();
    }
}