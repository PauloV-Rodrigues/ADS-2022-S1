#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

    int l, c, soma, mat[4][4], somaColunas[4];
    srand(time(NULL));

    for(l = 0; l < 4; l++){
        for(c = 0; c < 4; c++){
            mat[l][c] = rand() % 100;
        }
    }

    for(c = 0; c < 4; c++){
        soma = 0;
        for(l = 0; l < 4; l++){
            soma += mat[l][c];
        }
        somaColunas[c] = soma;
    }

    for(l = 0; l < 4; l++){
        for(c = 0; c < 4; c++){
            printf("%2d ", mat[l][c]);
        }
        printf("\n");
    }

    for(c = 0; c < 4; c++){
        printf("Somando a coluna %d: %d\n", c, somaColunas[c]);
    }

    return 0;
}