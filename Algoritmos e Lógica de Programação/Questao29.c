#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

    int l, c, soma, mat[4][4], somaLinhas[4];
    srand(time(NULL));

    for(l = 0; l < 4; l++){
        for(c = 0; c < 4; c++){
            mat[l][c] = rand() % 100;
        }
    }

    for(l = 0; l < 4; l++){
        soma = 0;
        for(c = 0; c < 4; c++){
            soma += mat[l][c];
        }
        somaLinhas[l] = soma;
    }

    for(l = 0; l < 4; l++){
        for(c = 0; c < 4; c++){
            printf("%2d ", mat[l][c]);
        }
        printf("\n");
    }

    for(l = 0; l < 4; l++){
        printf("Somando a linha %d: %d\n", l, somaLinhas[l]);
    }

    return 0;
}