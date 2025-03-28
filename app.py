from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='Validade Aluno API - SENAI',
                         version='1.0.0')
spec.register(app)


@app.route('/calcular-validade/<prazo>/<formato>')
def validado(prazo, formato):
    """
    API para calcular o prazo de validade de um produto conforme o número informado pelo usuário

    ## Endpoint:
    `GET /calcular-prazo/<prazo>/<formato>`

    ## Parâmetros:
    - `prazo` (int): **Valor no formato de inteiro** (exemplo: 1).
        - **Qualquer outro valor sem ser um número inteiro irá resultar em erro.**
    - `formato` (str): **Valor no formato de ‘string’** (exemplo: ano).
        - **Qualquer outro valor sem ser uma 'string' irá resultar em erro.**
    ## Resposta (JSON)
    ```json
    {
      "antes": "28/03/2025",
      "semanas": "20/06/2025"
    }
    ```

    ## Erros possíveis:
    - Se `prazo` não estiver no formato correto, retorna erro **400 Bad Request.**
    - Se `formato` não estiver no formato correto, retorna erro **400 Bad Request.**

    ## Resposta (JSON)
    `prazo`
    ```json
    {
          "Error": "formato invalido, tente usar números inteiros ao invés de quebrados."
    }
    ```
    `formato`
    ```json
    {
          'Error': 'formato invalido, tente (dia, semana, mes ou ano)'
    }
    ```
    """
    try:

        prazo = int(prazo)
        if formato == 'dia' or formato == 'dias':
            dias = datetime.today() + relativedelta(days=prazo)
            dias = dias.strftime('%d/%m/%Y')
            data = dias
            tipo_data = "dias"
        elif formato == 'semana' or formato == 'semanas':
            semanas = datetime.today() + relativedelta(weeks=prazo)
            semanas = semanas.strftime('%d/%m/%Y')
            data = semanas
            tipo_data = "semanas"
        elif formato == 'mes' or formato == 'meses':
            mes = datetime.today() + relativedelta(months=prazo)
            mes = mes.strftime('%d/%m/%Y')
            data = mes
            tipo_data = "meses"
        elif formato == 'ano' or formato == 'anos':
            anos = datetime.today() + relativedelta(years=prazo)
            anos = anos.strftime('%d/%m/%Y')
            data = anos
            tipo_data = "anos"
        else:
            return jsonify({
                'Error': 'formato invalido, tente (dia, semana, mes ou ano)'
            })

        return jsonify({'antes': (datetime.today().strftime("%d/%m/%Y")),
                        f'{tipo_data}': data
                        })
    except ValueError:
        return jsonify({
            'Error': 'formato invalido, tente usar números inteiros ao invés de quebrados.'
        })


if __name__ == '__main__':
    app.run(debug=True)
