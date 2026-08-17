using System;

public abstract class ParteAvion {
    public string Nombre { get; set; }
    protected string Estado { get; set; }

    public ParteAvion(string nombre, string estado) {
        Nombre = nombre;
        Estado = estado;
    }
    public abstract void Inspeccionar();
}

public class Turbina : ParteAvion {
    public int EmpujeLbs { get; set; }
    public Turbina(string nombre, string estado, int empuje) : base(nombre, estado) {
        EmpujeLbs = empuje;
    }
    public override void Inspeccionar() {
        Console.WriteLine($"Turbina '{Nombre}': Estado {Estado}, Empuje: {EmpujeLbs} lbs.");
    }
}

class Program {
    static void Main() {
        ParteAvion t = new Turbina("CFM LEAP", "Excelente", 32000);
        t.Inspeccionar();
    }
}