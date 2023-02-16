from flask import Flask

app = Flask(__name__)


@app.route('/choice/Mars')
def bootstrap():
    return f'''<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Выбор планеты</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
        <link rel="stylesheet" href="static/css/style1.css">
    </head>
    <body>
        <h1>Я выбираю: Марс</h1>
        <h3>Эта планета близка по строению к Земле</h3>
        <div class="p-3 mb-2 bg-danger text-white bg-opacity-75">Здесь большое количество полезных ресурсов</div>
        <div class="p-3 mb-2 bg-danger text-white bg-opacity-75">Присутствует неустойчивое магнитное поле</div>
        <div class="p-3 mb-2 bg-danger text-white bg-opacity-75">Газовая атмосфера</div>
        <div class="p-3 mb-2 bg-danger text-white bg-opacity-75">Присутствуют следы воды и органических веществ</div>
    </body>
</html>'''


@app.route('/choice/Venus')
def bootstrap():
    return f'''<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Выбор планеты</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
        <link rel="stylesheet" href="static/css/style2.css">
    </head>
    <body>
        <h1>Я выбираю: Венера</h1>
        <h3>Эта планета близка по строению к Земле</h3>
        <div class="p-3 mb-2 bg-warning text-dark bg-opacity-75">Имеет слабое магнитное поле</div>
        <div class="p-3 mb-2 bg-warning text-dark bg-opacity-75">Плотная газовая атмосфера</div>
        <div class="p-3 mb-2 bg-warning text-dark bg-opacity-75">Токсичная среда</div>
        <div class="p-3 mb-2 bg-warning text-dark bg-opacity-75">Большой ресурсный потенциал</div>
    </body>
</html>'''


@app.route('/choice/Enceladus')
def bootstrap():
    return f'''<!DOCTYPE html>
<html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Выбор планеты</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
        <link rel="stylesheet" href="static/css/style3.css">
    </head>
    <body>
        <h1>Я выбираю: Энцелад</h1>
        <h3>Эта планета не похожа на Землю</h3>
        <div class="p-3 mb-2 bg-info text-white bg-opacity-75">Имеет ледяную поверхность</div>
        <div class="p-3 mb-2 bg-info text-white bg-opacity-75">Не имеет атмосферы</div>
        <div class="p-3 mb-2 bg-info text-white bg-opacity-75">Замерзшая планета</div>
        <div class="p-3 mb-2 bg-info text-white bg-opacity-75">Имеет большие объемы жидкой воды под слоем льда</div>
    </body>
</html>'''


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
