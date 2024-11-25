#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NUM_COUNT 100000

int numbers[NUM_COUNT];

// Função para realizar o Bubble Sort
void bubbleSort(int arr[], int n) {
    int i, j, temp;
    int trocou;

    for (i = 0; i < n - 1; i++) {
        trocou = 0; // Verificar se houve troca nesta iteração

        // Comparar elementos adjacentes
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Troca de elementos
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                trocou = 1; // Marcar que houve troca
            }
        }

        // Se não houve troca, o vetor já está ordenado
        if (trocou == 0) {
            break;
        }
    }
}

void load_input() {
    FILE *file = fopen("input.txt", "r");

    char number[10];

    int i, j, ch;

    i = j = 0;

    while((i < NUM_COUNT) && ((ch = fgetc(file)) != EOF)) {
    	if (ch != '\n') {
		number[j] = ch;		
		++j;
	} else {
		number[j] = 0;
		numbers[i] = atoi(number);
		++i;
		j = 0;
	}
    }
}

int main() {
	load_input();

	bubbleSort(numbers, NUM_COUNT);

	return 0;
}
