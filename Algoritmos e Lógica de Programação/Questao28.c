#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {

    char *palavras[5][3];
    
    palavras[0][0] = "oi";
    palavras[0][1] = "tudo";
    palavras[0][2] = "estar";
    
    palavras[1][0] = "você";
    palavras[1][1] = "vai";
    palavras[1][2] = "?";

    palavras[2][0] = "com";
    palavras[2][1] = "dia";
    palavras[2][2] = "!";

    palavras[3][0] = ",";
    palavras[3][1] = "bem";
    palavras[3][2] = "sim";

    palavras[4][0] = "casa";
    palavras[4][1] = "hoje";
    palavras[4][2] = "em";
    
    printf("%s ", palavras[0][0]);
    printf("%s ", palavras[0][1]);
    printf("%s \n", palavras[0][2]);
    
    printf("%s ", palavras[1][0]);
    printf("%s ", palavras[1][1]);
    printf("%s \n", palavras[1][2]);

    printf("%s ", palavras[2][0]);
    printf("%s ", palavras[2][1]);
    printf("%s \n", palavras[2][2]);

    printf("%s ", palavras[3][0]);
    printf("%s ", palavras[3][1]);
    printf("%s \n", palavras[3][2]);

    printf("%s ", palavras[4][0]);
    printf("%s ", palavras[4][1]);
    printf("%s \n", palavras[4][2]);
    
    return 0;
}