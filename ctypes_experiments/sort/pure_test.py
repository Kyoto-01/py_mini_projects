#!/usr/bin/env python3

numbers = []


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        trocou = False  # Verificar se houve troca nesta iteração

        # Comparar elementos adjacentes
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                # Troca de elementos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                trocou = True  # Marcar que houve troca

        # Se não houve troca, o vetor já está ordenado
        if not trocou:
            break


def load_numbers():

    with open("input.txt", "r") as file:

        while n := file.readline():

             numbers.append(int(n))


load_numbers()

bubble_sort(numbers)
