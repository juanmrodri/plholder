#importamos flask y tambien render template, este segundo nos ayuda a mostrar el index, es lo que le da la capacidad a flask de mostrar un template
from flask import Flask, render_template
from covid import Covid
from bs4 import BeautifulSoup 
import requests
from datetime import date


covid = Covid()
covid.get_data() 

fecha_hoy = date.today()

paises = covid.list_countries()

locales = covid.get_status_by_country_name("Argentina")

pais = locales['country']
confirmados = locales['confirmed']
activos = locales['active']
muertes = locales['deaths']
recuperados = locales['recovered']

## aca tomamos prestada data relacionada con el covid ##
# por ahora la pagina del gob #

url = "https://www.argentina.gob.ar/salud/coronavirus-COVID-19"
page = requests.get(url) 
soup = BeautifulSoup(page.content, "html.parser")
info_prins = soup.find_all('p', "margin-0")

for uno in info_prins:
    prim = uno.find_all('p')

#print(locales.keys())
#print(locales.values())
#arg = locales.get("country")

#for x in locales:
    #print(x, ":", locales[x])

#print("casos totales: " + str(covid.get_total_active_cases()))
#print("Total recuperados: " + str(covid.get_total_recovered()))
#print("Muertes en todo el mundo: " + str(covid.get_total_deaths()))

# generamos instancia de Flask en app
app = Flask(__name__)

@app.route("/")
# esto siempre va a esperar una funcion, asique la definimos asi
# es decir siempre que el usuario entre a esta ruta, se va a ejecutar esta funcion

def index():
    html = """
    <!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Covid 19 - Flaskero</title>
    <!-- CSS only -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
        integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous" />
    <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap" rel="stylesheet" />
</head>
<style>
    body {
        font-family: "Roboto Mono", monospace;
        font-size: 14px;
        color: rgb(0, 0, 0);
        background-color: #fff;
    }

    h2 {
        font-size: 18px;
        line-height: 3rem;
    }

    span {
        font-weight: 700;
    }

    .marg-bot {
        bottom: 1rem;
    }

    .center {
        text-align: center;
    }

    .row {
        padding-top: 100px;
    }

    .badge-warning {
        margin: 1rem 0 2rem 0;
    }

    .row {
        flex-direction: column;
    }

    .col-6 {
        margin: 1rem auto;
        max-width: 100%;
    }

    .red {
        background-color: #dc3545;
    }

    .green {
        background-color: #28a745;
    }

    @media only screen and (min-width: 768px) {
        .row {
            flex-direction: row;
        }

        .col-6 {
            margin: 0 auto;
            max-width: 50%;
        }
        
        .marginer {
        margin-top: 3rem;
      }
    }
</style>

<body>
    <div class="container">
        <div class="row center">
            <div class="col-12 marg-bot">
                <h1 class="center">Covid flaskero</h1>
            </div>
            <div class="col-6">
                <h2>Confirmados totales en """ + str(pais) + """: <span class="alert alert-danger">""" + str(confirmados) + """</span></h2>
                <span class="badge badge-warning">Reporte - """ + str(fecha_hoy) + """</span>
                <ul class="list-group">
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        Activos
                        <span class="badge badge-primary badge-pill">""" + str(activos) + """</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        Muertos
                        <span class="badge badge-primary badge-pill red">""" + str(muertes) + """</span>
                    </li>
                    <li class="list-group-item d-flex justify-content-between align-items-center">
                        Recuperados
                        <span class="badge badge-primary badge-pill green">""" + str(recuperados) + """</span>
                    </li>
                </ul>
            </div>

            <div class="col-6 center">
                <img src='https://www.muycomputer.com/wp-content/uploads/2020/07/COVID-19.jpg' alt="peso"
                    class="img-fluid" />
                <span class="badge badge-warning">Infectados en el mundo: </span>
                <p>""" + str(covid.get_total_active_cases()) + """</p>
            </div>
        </div>
        <div class="col-6">
        <div class="card text-center marginer">
          <div class="card-header">
            Featured
          </div>
          <div class="card-body">
            <h5 class="card-title">Recomendaciones del Gobierno nacional</h5>
            <p class="card-text">
              """ + str(prim[0]) + """
            </p>
            <a href="https://www.argentina.gob.ar/salud/coronavirus-COVID-19" class="btn btn-primary">+ info</a>
          </div>
          <div class="card-footer text-muted">
            """ + str(fecha_hoy) + """
          </div>
        </div>
      </div>
    </div>
    <footer class="center"><span class="badge badge-primary">Proton-team</span>-Julio 2020</footer>
</body>

</html>
    """
    return html
if __name__ == "__main__":
    app.run(debug=True, port=3000)