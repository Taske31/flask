from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def slogan():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="{url_for('static', filename='css/bootstrap.css')}" />
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />

                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img  src="{url_for('static', filename='img/mars.jpg')}"
                    alt="Здесь должен был быть Марс">
                    <p class ="alert alert-dark" role="alert">Человечество вырастает из детства.</p>
                    <p class ="alert alert-success" role="alert">Человечеству мала одна планета.</p>
                    <p class ="alert alert-light" role="alert">Мы сделаем обитаемыми безжизненные пока планеты.</p>
                    <p class ="alert alert-warning" role="alert">И начнем с Марса!</p>
                    <p class ="alert alert-danger" role="alert">Присоединяйся!</p>
                  </body>
                </html>"""


@app.route('/astronaut_selection')
def astronaut_selection():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="{url_for('static', filename='css/bootstrap.css')}" />
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <title>Отбор астронавтов</title>
                  </head>
                  <body>
                    <h1>Анкета претендента</h1>
                    <h3>на участие в миссии</h3>  
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')


