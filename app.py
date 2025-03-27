from flask import Flask, jsonify
from flask_pydantic_spec import FlaskPydanticSpec
import datetime
from datetime import datetime
from dateutil.relativedelta import relativedelta

app = Flask(__name__)

spec = FlaskPydanticSpec('flask',
                         title='First API - SENAI',
                         version='1.0.0')
spec.register(app)

@app.route('/validadealunos/<dia>-<mes>-<ano>/<validade>')
def validado(prazo, formato):
    if formato == 'dia':
        dias = datetime.today() + relativedelta(days=prazo)
    elif formato == 'semana':
    elif formato == 'mes':
        meses = datetime.today()+relativedelta(months=prazo)
    elif formato == 'ano':
        anos = datetime.today()+relativedelta(years=prazo)
    # years=
    anos = ''
    # weeks=
    semanas = ''
    # days=


    return ({'antes': (datetime.today().strftime("%d-%m-%Y")),
            'dias': (dias),
            'semanas': (semanas),
            'meses': (meses),
            'anos': (anos)})

if __name__ == '__main__':
    app.run(debug=True)