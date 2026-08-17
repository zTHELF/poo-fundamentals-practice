#include <iostream>
#include <string>

class ComponenteCarro {
protected:
    std::string marca;
    int desgastePorcentaje;
public:
    ComponenteCarro(std::string m) : marca(m), desgastePorcentaje(0) {}
    virtual ~ComponenteCarro() {}
    virtual void diagnosticar() const = 0;
};

class SistemaFrenos : public ComponenteCarro {
    bool esAbs;
public:
    SistemaFrenos(std::string m, bool abs) : ComponenteCarro(m), esAbs(abs) {}
    void diagnosticar() const override {
        std::cout << "Frenos " << marca << " (" << (esAbs ? "ABS" : "Estandar") 
                  << "): Desgaste al " << desgastePorcentaje << "%\n";
    }
};

int main() {
    ComponenteCarro* f = new SistemaFrenos("Bosch", true);
    f->diagnosticar();
    delete f;
    return 0;
}