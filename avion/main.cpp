#include <iostream>
#include <string>

class ParteAvion {
protected:
    std::string nombre;
    std::string estado;
public:
    ParteAvion(std::string n, std::string e) : nombre(n), estado(e) {}
    virtual ~ParteAvion() {}
    virtual void inspeccionar() const = 0;
};

class TrenDeAterrizaje : public ParteAvion {
    bool desplegado;
public:
    TrenDeAterrizaje(std::string n, std::string e, bool d) : ParteAvion(n, e), desplegado(d) {}
    void inspeccionar() const override {
        std::cout << "Tren '" << nombre << "': " << (desplegado ? "Desplegado" : "Retraido") 
                  << ". Estado: " << estado << "\n";
    }
};

int main() {
    ParteAvion* tren = new TrenDeAterrizaje("Tren Principal", "Normal", true);
    tren->inspeccionar();
    delete tren;
    return 0;
}