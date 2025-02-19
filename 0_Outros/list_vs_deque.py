import sys
import time
from collections import deque

# Função para medir tempo de execução com listas


def test_list_operations(arr):
    lst = []
    # Adiciona 1 milhão de elementos no final
    for i in arr:
        lst.append(i)
    # Remove 100 mil elementos do início
    for _ in arr:
        lst.pop(0)


# Função para medir tempo de execução com deque


def test_deque_operations(arr):
    dq = deque()
    # Adiciona 1 milhão de elementos no final
    for i in arr:
        dq.append(i)
    # Remove 100 mil elementos do início
    for _ in arr:
        dq.popleft()


def test_list_read(arr):
    lst = arr

    for i in lst:
        pass


def test_deque_read(arr):
    dq = deque(arr)

    for i in dq:
        pass


num = int(input("Int: "))
arr = range(num)

# Medir tempo para lista
start_time = time.time()
test_list_operations(arr)
list_duration = time.time() - start_time
print(f"Tempo de execução para list: {list_duration:.2f}s")

# Medir tempo para deque
start_time = time.time()
test_deque_operations(arr)
deque_duration = time.time() - start_time
print(f"Tempo de execução para deque: {deque_duration:.2f}s")

print()

# Medir o tempo de leitura lista
start_time = time.time()
test_list_read(arr)
list_read_duration = time.time() - start_time
print(f"Tempo de execução para leitura list: {list_read_duration:.2f}s")

# Medir o tempo de leitura deque
start_time = time.time()
test_deque_read(arr)
deque_read_duration = time.time() - start_time
print(f"Tempo de execução para leitura deque: {deque_read_duration:.2f}s")

print()

lst = [i for i in arr]
dq = deque(arr)

print(f"Tamanho da lista: {sys.getsizeof(lst)} bytes")
print(f"Tamanho do deque: {sys.getsizeof(dq)} bytes")
