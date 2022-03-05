def convert_pesquisa_consulta(dict):
    cons_sql = []
    for chave, valor in dict.items():
        atributo = chave
        operador = ''
        
        for i in range(len(valor)):

            if valor[i] == 'LIKE':
                operador = valor[i-1]
                if valor[i-1] == 'OR':
                    operador_sql_or = valor[i]
                    cons_sql.append("{}  {} {} '{}'".format(operador_sql_or, atributo, operador, valor[i+1].replace('_', valor[i+2])))
                if valor[i-1] == 'AND':
                    operador_sql_and = valor[i]
                    cons_sql.append("{} {} {} '{}'".format(operador_sql_and, atributo, operador, valor[i+1].replace('_', valor[i+2])))
            
            elif valor[i] == 'BETWEEN':
                operador = valor[i]
                if valor[i-1] == 'OR':
                    operador_sql_or = valor[i-1]                    
                    cons_sql.append("{}  {} {} '{}' AND '{}'".format(operador_sql_or, atributo, operador, valor[i+1][0], valor[i+1][1]))
                if valor[i-1] == 'AND':
                    operador_sql_and = valor[i-1]  
                    cons_sql.append("{} {} {} '{}' AND '{}'".format(operador_sql_and, atributo, operador, valor[i+1][0], valor[i+1][1]))

            elif valor[i] == '=':
                operador = valor[i]
                if valor[i-1] == 'OR':
                    operador_sql_and = valor[i-1]
                    if isinstance(valor[i+1], float) or isinstance(valor[i+1], int):
                        cons_sql.append("{}  {} {} {}".format(operador_sql_and, atributo, operador, valor[i+1]))
                    else:
                        cons_sql.append("{}  {} {} '{}'".format(operador_sql_and, atributo, operador, valor[i+1])) 
                        
                operador_sql_and = valor[i-1] 
                if valor[i-1] == 'AND':
                    if isinstance(valor[i+1], float) or isinstance(valor[i+1], int):
                        cons_sql.append("{} {} {} {}".format(operador_sql_and, atributo, operador, valor[i+1]))
                    else:
                        cons_sql.append("{} {} {} '{}'".format(operador_sql_and, atributo, operador, valor[i+1]))

            elif valor[i] == '!=':
                operador = valor[i]
                if valor[i-1] == 'OR':
                    operador_sql_and = valor[i-1]
                    if isinstance(valor[i+1], float) or isinstance(valor[i+1], int):
                        cons_sql.append("{}  {} {} {}".format(operador_sql_and, atributo, operador, valor[i+1]))
                    else:
                        cons_sql.append("{}  {} {} '{}'".format(operador_sql_and, atributo, operador, valor[i+1]))

                operador_sql_and = valor[i-1]
                if valor[i-1] == 'AND':
                    if isinstance(valor[i+1], float) or isinstance(valor[i+1], int):
                        cons_sql.append("{} {} {} {}".format(operador_sql_and, atributo, operador, valor[i+1]))
                    else:
                        cons_sql.append("{}  {} {} '{}'".format(operador_sql_and, atributo, operador, valor[i+1]))
    
    return " ".join(cons_sql)[4:]
    


entry2 = {
    "nome": ['AND', 'LIKE', '%_%', 'Gabriel'],
    "data": ['OR', 'BETWEEN', ['2022-03-01', '2022-03-31']],
    "id": ['OR', '=', 1],
    "status": ['OR', '!=', 1],
}    

resultado2 = convert_pesquisa_consulta(entry2)
print(resultado2)

