#include <stdio.h>
#include <string.h>

/*
   ---------------------------------------------
   PROJETO: Sistema de Academia
   OBJETIVO: Cadastrar alunos, calcular IMC e mostrar resultados.
   FEITO POR: Marcos Vitor Olivera De Luna
   PROFESSOR: Eros Leon Kohler
   DISCIPLINA: Algoritmos e Lógica de Programação
   ---------------------------------------------
*/

struct Aluno {
    char nome[50];
    int idade;
    float peso, altura, imc;
};
// Função 01
float calcularIMC(float peso, float altura) {
    return peso / (altura * altura);
}
// Função 02
void mostrarStatus(float imc) {
    if (imc < 18.5)
        printf(" - Abaixo do peso\n");
    else if (imc < 25)
        printf(" - Peso normal\n");
    else if (imc < 30)
        printf(" - Sobrepeso\n");
    else
        printf(" - Obesidade\n");
}

int main() {
    struct Aluno alunos[100];
    int qtd = 0;
    int opcao;

    do {
        printf("\n===== MENU PRINCIPAL =====\n");
        printf("1 - Cadastrar Aluno\n");
        printf("2 - Listar Alunos\n");
        printf("3 - Apagar Aluno\n"); // <-- NOVA OPÇÃO
        printf("4 - Sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);
        getchar(); // <-- limpa ENTER do menu

        switch (opcao) {
            case 1:
                if (qtd < 100) {
                    printf("\n=== Cadastro de Aluno ===\n");

                    printf("Nome: ");
                    scanf(" %[^\n]", alunos[qtd].nome); 

                    printf("Idade: ");
                    scanf("%d", &alunos[qtd].idade);

                    printf("Peso (kg): ");
                    scanf("%f", &alunos[qtd].peso);

                    printf("Altura (m): ");
                    scanf("%f", &alunos[qtd].altura);

                    if (alunos[qtd].peso > 0 && alunos[qtd].altura > 0) {
                        alunos[qtd].imc = calcularIMC(alunos[qtd].peso, alunos[qtd].altura);
                        printf("\nAluno cadastrado com sucesso!\n");
                        qtd++;
                    } else {
                        printf("\nValores inválidos! Cadastro cancelado.\n");
                    }
                } else {
                    printf("\nLimite de alunos atingido!\n");
                }
                break;

            case 2:
                if (qtd == 0)
                    printf("\nNenhum aluno cadastrado ainda.\n");
                else {
                    printf("\n=== Lista de Alunos ===\n");
                    for (int i = 0; i < qtd; i++) {
                        printf("%d. %s - Idade: %d - IMC: %.2f",
                               i + 1, alunos[i].nome, alunos[i].idade, alunos[i].imc);
                        mostrarStatus(alunos[i].imc);
                    }
                }
                break;

            case 3:
                if (qtd == 0) {
                    printf("\nNenhum aluno cadastrado para apagar.\n");
                } else {
                    int num;
                    printf("\nDigite o número do aluno que deseja apagar (1 a %d): ", qtd);
                    scanf("%d", &num);

                    if (num < 1 || num > qtd) {
                        printf("\nNúmero inválido!\n");
                    } else {
                        // Move todos os alunos seguintes uma posição para trás
                        for (int i = num - 1; i < qtd - 1; i++) {
                            alunos[i] = alunos[i + 1];
                        }
                        qtd--; // reduz a contagem total
                        printf("\nAluno apagado com sucesso!\n");
                    }
                }
                break;

            case 4:
                printf("\nEncerrando o programa...\n");
                break;

            default:
                printf("\nOpcao invalida! Tente novamente.\n");
        }

    } while (opcao != 4); // Encerra o loop
    

    return 0;
}
