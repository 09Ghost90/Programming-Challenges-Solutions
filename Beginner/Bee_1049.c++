#include <iostream>
#include <string>

void verificarAnimal(const std::string& resposta1, const std::string& resposta2, const std::string& resposta3) {
    if (resposta1 == "vertebrado") {
        if (resposta2 == "ave") {
            if (resposta3 == "carnivoro") {
                std::cout << "aguia" << "\n";
            }
            else if (resposta3 == "onivoro") {
                std::cout << "pomba" << "\n";
            }
        }
        else if (resposta2 == "mamifero") {
            if (resposta3 == "onivoro") {
                std::cout << "homem" << "\n";
            }
            else if (resposta3 == "herbivoro") {
                std::cout << "vaca" << "\n";
            }
        }
    }
    else if (resposta1 == "invertebrado") {
        if (resposta2 == "inseto") {
            if (resposta3 == "hematofago") {
                std::cout << "pulga" << "\n";
            }
            else if (resposta3 == "herbivoro") {
                std::cout << "lagarta" << "\n";
            }
        }
        else if (resposta2 == "anelideo") {
            if (resposta3 == "hematofago") {
                std::cout << "sanguessuga" << "\n";
            }
            else if (resposta3 == "onivoro") {
                std::cout << "minhoca" << "\n";
            }
        }
    }
}

int main() {
    std::string resposta1, resposta2, resposta3;
    std::cin >> resposta1;
    std::cin >> resposta2;
    std::cin >> resposta3;

    verificarAnimal(resposta1, resposta2, resposta3);

    return 0;
}
