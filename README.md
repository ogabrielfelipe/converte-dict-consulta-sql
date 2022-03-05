# converte-dict-consulta-sql
- Módulo destinado a converter um dict passado pelo front-end e converter para ser usado em uma consulta SQL

- Modo de Usar:

    - Como deve passar:
    ```
        {
            "nome": ['AND', 'LIKE', '%_%', 'Gabriel'],
            "data": ['OR', 'BETWEEN', ['2022-03-01', '2022-03-31']],
            "id": ['AND', '=', 1],
            "status": ['OR', '!=', 1]
        }
    ```


    - Resultado esperado:
    
    'nome LIKE '%Gabriel%' OR  data BETWEEN '2022-03-01' AND '2022-03-31' AND id = 1 OR status != 1'
