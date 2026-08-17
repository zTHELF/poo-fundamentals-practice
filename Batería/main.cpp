#include <iostream>
#include <string>

class ComponenteBateria {
protected:
    std::string idSerie;
    double temperatura;
public:
    ComponenteBateria(std::string id) : idSerie(id), temperatura(25.0) {}
    virtual ~ComponenteBateria() {}
    virtual void verificarSalud() const = 0;
};

class BMS : public ComponenteBateria {
    int celdasConectadas;
public:
    BMS(std::string id, int c) : ComponenteBateria(id), celdasConectadas(c) {}
    void verificarSalud() const override {
        std::cout << "Módulo BMS " << idSerie << ": " << celdasConectadas 
                  << " celdas conectadas. Temp: " << temperatura << "°C\n";
    }
};

int main() {
    ComponenteBateria* bms = new BMS("BMS-MASTER", 16);
    bms->verificarSalud();
    delete bms;
    return 0;
}