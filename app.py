#importamos flask y tambien render template, este segundo nos ayuda a mostrar el index, es lo que le da la capacidad a flask de mostrar un template
from flask import Flask, render_template
from covid import Covid
from bs4 import BeautifulSoup 
import requests

covid = Covid()
covid.get_data() 

paises = covid.list_countries()

locales = cases = covid.get_status_by_country_name("Argentina")

pais = locales['country']
confirmados = locales['confirmed']
activos = locales['active']
muertes = locales['deaths']
recuperados = locales['recovered']
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
  <!-- CSS only -->
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css"
    integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous" />
  <link href="https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;700&display=swap" rel="stylesheet" />
  <title>Covid 19 - Flaskero</title>
  <style>
    body {
      font-family: "Roboto Mono", monospace;
      font-size: 14px;
      color: #ccc;
      background-color: #316191;
    }
    
    h2{
        font-size: 18px;
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
    .under {
        text-decoration: underline;  
    }

    .row {
      padding-top: 100px;
    }
  </style>
</head>

<body>
  <div class="container">
    <div class="row center">
      <div class="col-12 marg-bot">
        <h1 class="center under">Covider flaskero piturro</h1>
      </div>
      <div class="col-6">
        <h2>Confirmados totales en """ + str(pais) + """: <span>""" + str(confirmados) + """</span></h2>
        <h2>Activos: <span>""" + str(activos) + """</span></h2>
        <h2>Muertos: <span>""" + str(muertes) + """</span></h2>
        <h2>Recuperados: <span>""" + str(recuperados) + """</span></h2>
      </div>
      <div class="col-6 center">
        <img src='https://www.muycomputer.com/wp-content/uploads/2020/07/COVID-19.jpg' alt="peso" class="img-fluid" />
        <p>Infectados en el mundo: </p>
        <p>""" + str(covid.get_total_active_cases()) + """</p>
      </div>
    </div>
  </div>
</body>

</html>
    """
    return html
if __name__ == "__main__":
    app.run(debug=True, port=3000)