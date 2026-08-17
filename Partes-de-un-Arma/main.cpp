#include <iostream>
#include <string>

class ComponenteArma {
protected:
    std::string material;
    bool limpio;
public:
    ComponenteArma(std::string m) : material(m), limpio(true) {}
    virtual ~ComponenteArma() {}
    virtual void mantenimiento() = 0;
};

class Cargador : public ComponenteArma {
    int capacidad;
public:
    Cargador(std::string m, int c) : ComponenteArma(m), capacidad(c) {}
    void mantenimiento() override {
        std::cout << "Cargador " << material << " (Capacidad: " << capacidad 
                  << " municiones): Lubricacion completa.\n";
    }
};

int main() {
    ComponenteArma* cargador = new Cargador("Polimero STANAG", 30);
    cargador->mantenimiento();
    delete cargador;
    return 0;
}