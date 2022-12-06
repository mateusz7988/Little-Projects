def solution(N):
    n = bin(N)
    n = str(n)
    gap = 0
    gap_list = []
    lista = [char for char in n]
    lista.pop(0)
    lista.pop(0)
    lista = [int(char) for char in lista]
    print(lista)
    for i in range(0, len(lista)):
        try:
            while lista[i] == 0:
                gap = gap + 1
                lista.pop(i)
                print(lista)
            if gap == 0 and 0 in gap_list:
                None
            else:
                gap_list.append(gap)
            gap = 0
        except IndexError:
            if gap != 0 and -1 not in gap_list:
                gap_list.append(-1)
    print(gap_list)
    print(max(gap_list))
    return max(gap_list)
solution(1025)