import requests

# www.metropolitano.com.pe/webmetro/new/prueba/consulta_prueba.php
# www.metropolitano.com.pe/webmetro/new/prueba/validaciones_recargas.php
# www.metropolitano.com.pe/webmetro/new/prueba/busca_itinerario.php


def query_card(request, card):
    url = "http://metropolitano.com.pe/webmetro/new/prueba/consulta_prueba.php"
    web_response = request.get(url)
    web = web_response.text
    start = web.find('id="txtcondicion">')
    KEY = web[start + 18:start + 22]
    print KEY

    # do POST
    url_2 = "http://metropolitano.com.pe/webmetro/new/prueba/validaciones_recargas.php"
    param = {
        'tarjeta': card,
        'txt': KEY,
    }
    print '\ncargando...'
    card_response = request.post(url_2, data=param)
    return card_response.text


with requests.session() as req:
    card = raw_input("Input your card number: ")
    print query_card(req, card)
