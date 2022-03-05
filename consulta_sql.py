def convert_pesquisa_consulta(dict):
    cons_sql = []
    for chave, valor in dict.items():
        atributo = chave
        operador = ''
        for i in range(len(valor)):
            if valor[i] == 'OR':
                operador_sql_or = valor[i]
                if valor[i+1] == 'LIKE':
                    operador = valor[i+1]
                    cons_sql.append("{}  {} {} '{}'".format(operador_sql_or, atributo, operador, valor[i+2].replace('_', valor[i+3])))
                if valor[i+1] == '=':                
                    operador = valor[i+1]
                    cons_sql.append('{}  {} {} {}'.format(operador_sql_or, atributo, operador, valor[i+2]))
                if valor[i+1] == '!=':                
                    operador = valor[i+1]
                    cons_sql.append('{} {} {} {}'.format(operador_sql_or, atributo, operador, valor[i+2]))
                if valor[i+1] == 'BETWEEN':            
                    operador = valor[i+1]
                    cons_sql.append("{}  {} {} '{}' AND '{}'".format(operador_sql_or, atributo, operador, valor[i+2][0], valor[i+2][1]))

            elif valor[i] == 'AND':
                operador_sql_and = valor[i]
                if valor[i+1] == 'LIKE':
                    operador = valor[i+1]
                    cons_sql.append("{} {} {} '{}'".format(operador_sql_and, atributo, operador, valor[i+2].replace('_', valor[i+3])))
                if valor[i+1] == '=':                
                    operador = valor[i+1]
                    cons_sql.append('{} {} {} {}'.format(operador_sql_and, atributo, operador, valor[i+2]))
                if valor[i+1] == '!=':                
                    operador = valor[i+1]
                    cons_sql.append('{} {} {} {}'.format(operador_sql_and, atributo, operador, valor[i+2]))
                if valor[i+1] == 'BETWEEN':            
                    operador = valor[i+1]
                    cons_sql.append("{} {} {} '{}' AND '{}'".format(operador_sql_and, atributo, operador, valor[i+2][0], valor[i+2][1]))
    
    return " ".join(cons_sql)[4:]
    


entry2 = {
    "nome": ['AND', 'LIKE', '%_%', 'Gabriel'],
    "data": ['OR', 'BETWEEN', ['2022-03-01', '2022-03-31']],
    "id": ['AND', '=', 1],
    "status": ['OR', '!=', 1],
}    

resultado2 = convert_pesquisa_consulta(entry2)
print(resultado2)

