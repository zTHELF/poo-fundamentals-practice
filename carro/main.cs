using System;

public abstract class ComponenteCarro {
    public string Marca { get; set; }
    protected int DesgastePorcentaje { get; set; } = 0;

    public ComponenteCarro(string marca) { Marca = marca; }
    public abstract void Diagnosticar();
}

public class Motor : ComponenteCarro {
    public int CaballosFuerza { get; set; }
    public Motor(string marca, int hp) : base(marca) { CaballosFuerza = hp; }

    public override void Diagnosticar() {
        Console.WriteLine($"Motor {Marca} [{CaballosFuerza} HP]: Desgaste al {DesgastePorcentaje}%");
    }
}

class Program {
    static void Main() {
        ComponenteCarro v8 = new Motor("V8 Turbo", 500);
        v8.Diagnosticar();
    }
}