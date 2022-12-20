def rows_registro(lista_registros, registro_procurado):
    indices = []
    for idx, value in enumerate(lista_registros):
        if value == registro_procurado:
            indices.append(idx+1)
    return indices
    

if __name__ == '__main__':
    a_list = [1,2,3,4,1,2,1,2,3,4]
    print(rows_registro(a_list, 1))