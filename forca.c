#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define LETRAS 21

void imprimir_palavras(char *m, int tamanho){
    int i;
    int j;
    int k;
    for(i = 0, j = 0; i < tamanho; i++, j += LETRAS){
        for(k = j; m[k] != '\0'; k++){
            printf("%c", m[k]);
        }
        printf("\n");
    }
    printf("\n");
}

void adicionar_palavra(char *m, char *palavra_nova, int tamanho){
    int pont;
    int i;
    for(i = 0, pont = LETRAS*tamanho; i <= strlen(palavra_nova); i++, pont++){
        m[pont] = palavra_nova[i];
    }
}

int forca(char *palavra){
    char esconder[LETRAS];
    int i;
    int acertou = 0;
    int tentativas = 0;
    char chute;
    for(i = 0; i < strlen(palavra); i++){
        esconder[i] = '_';
    }
    esconder[i] = '\0';
    while(strcmp(palavra, esconder) != 0){
        acertou = 0;
        printf("A palavra tem %i letras\t voce ja fez %i tentativas\n\n", strlen(palavra), tentativas);
        puts(esconder);
        printf("\nChute uma letra: ");

        chute = getchar();
        
        for(i = 0; i < strlen(palavra); i++){
            if(chute == palavra[i] && esconder[i] == '_'){
                esconder[i] = chute;
                acertou = 1;
            }
        }
        if(acertou){
            printf("parabens!! voce acertou a letra %c\n\n", chute);
        }
        tentativas++;
        
    }
    
    return tentativas;
}

int main()
{   
    int escolha;
    int sorteio;
    int resultado;
    char palavras[5][LETRAS] = {"ricardo", "pedro", "alessandra", "polyanna", "daniel"};
    int quantidade_de_palavras = 5;
    char palavra_nova[LETRAS];
    
    puts("Bem-vindo ao jogo da forca");
    do{
        puts("Escolha uma das opcoes abaixo:\n");
        puts("[1] Jogar");
        puts("[2] Ver as palavras do jogo");
        puts("[3] Adicionar uma palavra no jogo");
        puts("[4] Sair do jogo");
        
        scanf("%d", &escolha);
        setbuf(stdin,NULL);
        switch(escolha){
            case 1:
                sorteio = rand()%quantidade_de_palavras;
                resultado = forca(palavras[sorteio]);
                printf("voce ganhou com apenas %i tentativas\n", resultado);
                break;
                
            case 2:
                imprimir_palavras(palavras, quantidade_de_palavras);
                break;
                
            case 3:
                do{
                    printf("Digite a palavra que voce gostaria de adicionar:\nObs: a palavra dever ter no maximo %d letras\n", LETRAS-1);
                    setbuf(stdin, NULL);
                    gets(palavra_nova);
                    if(strlen(palavra_nova) >= LETRAS)
                        fflush(stdin);
                }while(strlen(palavra_nova) >= LETRAS);
                
                adicionar_palavra(palavras,palavra_nova,quantidade_de_palavras);
                quantidade_de_palavras++;
                break;
                
            default:
                if(escolha != 4){
                    puts("Opcao invalida\n");
                    break;
                }
                
        }
    }while(escolha != 4);
    puts("Volte sempre! :)");

    return 0;
}
