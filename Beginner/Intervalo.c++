// Programação Procedimental A1
// 11/06/2024
// Bruno Sousa Pereira
// 12321ECP001


#include <stdio.h>
#include <stdlib.h>
#include <math.h>

float raio_user = 0;
float perimetro = 0;
float area = 0;
float pi = M_PI;

int main() {
    system("cls");

    printf("Seja bem vindo ao simples calculador de Area e Perimetro de um circulo!\n\n");

    printf("Digite o raio do circulo: ");
    scanf("%f", &raio_user);

    // Calculando o perímetro e área do circulo:
    perimetro = 2 * pi * raio_user;
    area = pi * (pow(raio_user, 2));

    printf("O circulo de raio %.3f cm possui perimetro = %.3f cm", raio_user, perimetro);
    printf("\n");
    printf("O circulo de raio %.3f cm possui area = %.3f cm", raio_user, area);

    return 0;
}