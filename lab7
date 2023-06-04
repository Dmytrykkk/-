from flask import Flask, request
import requests


app = Flask(__name__)
auth_cookie = None


login_page = """
<html>
    <head>
        <title>Login</title>
        <style>
            body {
                background-color: #15202d;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            form {
                background-color: white;
                padding: 50px;
                padding-left: 100;
                padding-right: 100;
                border: 1px solid white;
                border-radius: 15px;
            }
            label, input[type="password"], input[type="text"] {
                width: 350px;
                height: 30px;
            }
            input[type="submit"] {
                background-color: #007bff;
                color: white;
                padding: 10px 20px;
                border: none;
                cursor: pointer;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <form action="/" method="post">
            <label for="login"><span style="color: red">*</span> E-mail:</label><br>
            <input type="text" id="login" name="login"><br><br><br><br>
            <label for="password"><span style="color: red">*</span> Пароль:</label><br>
            <input type="password" id="password" name="password"><br><br><br>
            <input type="submit" value="Увійти">
        </form>
    </body>
</html>
"""


def get_value(url: str, auth, key: str) -> str:
    x = requests.get(
        url,
        cookies={
            "JWT": auth
        }
    )

    if x.ok:
        data = x.json()
        results = data.get("results")
        value = results[0].get(key)
        return value
    else:
        print("Ключ не знайдено")
        
        return None


def format_profile(data: dict) -> str:
    page = f"""
<html>
    <head>
        <title>{data['email']}</title>
        <style>
            body {{
                background-color: #15202d;
                margin: 70px;
            }}
            div {{
                background-color: white;
                border-radius: 30px;
                padding: 30px;
                width: 80vw; /* 80% of the viewport width */
                max-width: 850px; /* Maximum width of 850px */
                margin: 0 auto;
            }}
            h1, h2 {{
                margin-left: 20px;
                margin-right: 100px;
            }}
            img {{
                margin-right: 100px;
                max-width: 85%; /* Decreased by 15% */
                height: auto;
            }}
            input[type="submit"] {{
                width: 700px;
                cursor: pointer;
                height: 70px;
                margin-left: calc(50% - 350px);
                background-color: #007bff;
                color: white;
                font-size: 24px;
                border-radius: 10px;
            }}
        </style>
    </head>
    <body>
        <div>
            <table width="100%" style="margin-top: 30px;">
                <tr>
                    <td valign="middle" width="50%">
                        <p><big><h1>{data['surname']} {data['name']}</h1></big></p>
                        <p><h2>{data['birthday']}</h2></p>
                    </td>
                    <td valign="middle" align="right" width="50%">
                        <img src="{data['image']}" width="178" height="229"> <!-- Decreased by 15% -->
                    </td>
                </tr>
            </table>
            <table align="center">
                <tr>
                    <td valign="middle" align="center" style="padding-top: 50px; padding-bottom: 20px;">
                        <form action="/gradebook" method="post">
                            <input type="submit" value="Академічні ресурси">
                        </form>
                    </td>
                </tr>
                <tr>
                    <td valign="middle" align="center" style="padding-top: 20px; padding-bottom: 20px;">
                        <form action="/recordbook" method="post">
                            <input type="submit" value="Залікова книжка">
                        </form>
                    </td>
                </tr>
            </table>
            <table>
                <tr>
                    <td class="image-cell"></td>
                    <td></td>
                </tr>
            </table>
        </div>
    </body>
</html>
"""
    return page


def profile_info(data: dict) -> str:

    page = f"""
<html>
<html>
    <head>
        <title>Журнал</title>
        <style>
            body {{
                background-color: #15202d;
                display: flex;
                align-items: center;
                justify-content: center;
                height: 100vh;
                margin: 0;
            }}
            table {{
                background-color: white;
                width: 60%;
            }}
            th, td {{
                padding: 10px;
                font-size: 14px;
            }}
        </style>
    </head>
    <body>
        <table>
            <tr>
                <td style= "font-size: 16px"><b>E-mail</b></td>
                <td><p>{data.get('email')}</p></td>
            </tr>
            <tr style="background-color: #ecf2fb">
                <td style= "font-size: 16px"><b>Дата реєстрації</b></td>
                <td>{data.get('date_joined')}</td>
            </tr>
            <tr>
                <td style= "font-size: 16px"><b>Код користувача</b></td>
                <td>{data.get('user_code')}</td>
            </tr>
            <tr style="background-color: #ecf2fb">
                <td style= "font-size: 16px"><b>Спеціальність</b></td>
                <td>{data.get('birthday')}</td>
            </tr>
            <tr>
                <td style= "font-size: 16px"><b>Галузь знань</b></td>
                <td>12 Інформаційні технології</td>
            </tr>
            <tr style="background-color: #ecf2fb">
                <td style= "font-size: 16px"><b>Освітня програма</b></td>
                <td>23696 Інженерія програмного забезпечення</td>
            </tr>
            <tr>
                <td style= "font-size: 16px"><b>Ступінь</b></td>
                <td>Перший (бакалаврський)</td>
            </tr>
            <tr style="background-color: #ecf2fb">
                <td style= "font-size: 16px"><b>Курс</b></td>
                <td>1</td>
            </tr>
            <tr >
                <td style= "font-size: 16px"><b>Форма навчання</b></td>
                <td>Денна</td>
            </tr>
            <tr style="background-color: #ecf2fb">
                <td style= "font-size: 16px"><b>Форма фінансування</b></td>
                <td>За кошти державного бюджету</td>
            </tr>
        </table>
    </body>
</html>
"""
    return page


def profile_recordbook(data: dict) -> str:

    result_list = data.get('results', [])

    page = f"""
<html>
    <head>
        <title>Журнал</title>
        <style>
            body {{
                background-color: #15202d;
                margin: 70px;
                display: flex;
                justify-content: center;
                align-items: center;
            }}
            table {{
                background-color: white;
                width: 90%;
                margin: 0 auto;
            }}
            th, td {{
                padding: 10px;
                font-size: 14px
            }}
        </style>
    </head>
    <body>
        <table>
            <tr style="background-color: #8196b9;">
                <th >Назва навчальної дисципліни</th>
                <th>Годин</th>
                <th>Кредитів</th>
                <th>Викладач</th>
                <th>За національною шкалою</th>
                <th>Кількість балів</th>
                <th>За шкалою ECTS</th>
                <th width="70">Дата</th>
            </tr>
            <tr>
                <td>{result_list[0].get('discipline_name')}</td>
                <td>{result_list[0].get('hours')}</td>
                <td>{result_list[0].get('credits')}</td>
                <td>{result_list[0].get('teacher_name')}</td>
                <td>{result_list[0].get('result_national')}</td>
                <td>{result_list[0].get('result')}</td>
                <td>{result_list[0].get('result_ects')}</td>
                <td>{result_list[0].get('date')}</td>
            </tr>
            <tr style="background-color: #ecf2fb">
                <td>{result_list[1].get('discipline_name')}</td>
                <td>{result_list[1].get('hours')}</td>
                <td>{result_list[1].get('credits')}</td>
                <td>{result_list[1].get('teacher_name')}</td>
                <td>{result_list[1].get('result_national')}</td>
                <td>{result_list[1].get('result')}</td>
                <td>{result_list[1].get('result_ects')}</td>
                <td>{result_list[1].get('date')}</td>
            </tr>
            <tr>
                <td>{result_list[2].get('discipline_name')}</td>
                <td>{result_list[2].get('hours')}</td>
                <td>{result_list[2].get('credits')}</td>
                <td>{result_list[2].get('teacher_name')}</td>
                <td>{result_list[2].get('result_national')}</td>
                <td>{result_list[2].get('result')}</td>
                <td>{result_list[2].get('result_ects')}</td>
                <td>{result_list[2].get('date')}</td>
            </tr>
            <tr style="background-color: #ecf2fb">
                <td>{result_list[3].get('discipline_name')}</td>
                <td>{result_list[3].get('hours')}</td>
                <td>{result_list[3].get('credits')}</td>
                <td>{result_list[3].get('teacher_name')}</td>
                <td>{result_list[3].get('result_national')}</td>
                <td>{result_list[3].get('result')}</td>
                <td>{result_list[3].get('result_ects')}</td>
                <td>{result_list[3].get('date')}</td>
            </tr>
            <tr>
                <td>{result_list[4].get('discipline_name')}</td>
                <td>{result_list[4].get('hours')}</td>
                <td>{result_list[4].get('credits')}</td>
                <td>{result_list[4].get('teacher_name')}</td>
                <td>{result_list[4].get('result_national')}</td>
                <td>{result_list[4].get('result')}</td>
                <td>{result_list[4].get('result_ects')}</td>
                <td>{result_list[4].get('date')}</td>
            </tr>
            <tr style="background-color: #ecf2fb">
                <td>{result_list[5].get('discipline_name')}</td>
                <td>{result_list[5].get('hours')}</td>
                <td>{result_list[5].get('credits')}</td>
                <td>{result_list[5].get('teacher_name')}</td>
                <td>{result_list[5].get('result_national')}</td>
                <td>{result_list[5].get('result')}</td>
                <td>{result_list[5].get('result_ects')}</td>
                <td>{result_list[5].get('date')}</td>
            </tr>
            <tr>
                <td>{result_list[6].get('discipline_name')}</td>
                <td>{result_list[6].get('hours')}</td>
                <td>{result_list[6].get('credits')}</td>
                <td>{result_list[6].get('teacher_name')}</td>
                <td>{result_list[6].get('result_national')}</td>
                <td>{result_list[6].get('result')}</td>
                <td>{result_list[6].get('result_ects')}</td>
                <td>{result_list[6].get('date')}</td>
        </table>
    </body>
</html>
"""
    return page


def profile_gradebook(data: dict) -> str:
    result_list = data.get('results', [])
    page = f"""
<html>
    <head>
        <title>Журнал</title>
        <style>
            body {{
                background-color: #15202d;
                margin: 70px;
            }}
            table {{
                background-color: white;
                width: 90%;
                margin: 0 auto;
            }}
            th, td {{
                padding: 10px;
                font-size: 14px
            }}
        </style>
    </head>
    <body>
        <table>
            <tr style="background-color: #8196b9;">
                <th >Назва журналу</th>
                <th>Назва предмету</th>
                <th>Тип журналу</th>
                <th>Семестр</th>
                <th>Академічних годин</th>
                <th>Викладач</th>
            </tr>
            <tr>
                <td>{result_list[0].get('legal_name')}</td>
                <td>{result_list[0].get('discipline_name')}</td>
                <td>{result_list[0].get('gradebook_type')}</td>
                <td>{result_list[0].get('semester_students', [])}</td>
                <td>{result_list[0].get('hours', [])}</td>
                <td>{result_list[0].get('teacher_info', [])}</td>
            </tr>
            <tr style="background-color: #ecf2fb">
                <td>{result_list[1].get('legal_name')}</td>
                <td>{result_list[1].get('discipline_name')}</td>
                <td>{result_list[1].get('gradebook_type')}</td>
                <td>{result_list[1].get('semester_students', [])}</td>
                <td>{result_list[1].get('hours', [])}</td>
                <td>{result_list[1].get('teacher_info', [])}</td>
            </tr>
            <tr>
                <td>{result_list[2].get('legal_name')}</td>
                <td>{result_list[2].get('discipline_name')}</td>
                <td>{result_list[2].get('gradebook_type')}</td>
                <td>{result_list[2].get('semester_students', [])}</td>
                <td>{result_list[2].get('hours', [])}</td>
                <td>{result_list[2].get('teacher_info', [])}</td>
            </tr>
            <tr style="background-color: #ecf2fb">
                <td>{result_list[3].get('legal_name')}</td>
                <td>{result_list[3].get('discipline_name')}</td>
                <td>{result_list[3].get('gradebook_type')}</td>
                <td>{result_list[3].get('semester_students', [])}</td>
                <td>{result_list[3].get('hours', [])}</td>
                <td>{result_list[3].get('teacher_info', [])}</td>
            </tr>
            <tr>
                <td>{result_list[4].get('legal_name')}</td>
                <td>{result_list[4].get('discipline_name')}</td>
                <td>{result_list[4].get('gradebook_type')}</td>
                <td>{result_list[4].get('semester_students', [])}</td>
                <td>{result_list[4].get('hours', [])}</td>
                <td>{result_list[4].get('teacher_info', [])}</td>
            </tr>
            <tr style="background-color: #ecf2fb">
                <td>{result_list[5].get('legal_name')}</td>
                <td>{result_list[5].get('discipline_name')}</td>
                <td>{result_list[5].get('gradebook_type')}</td>
                <td>{result_list[5].get('semester_students', [])}</td>
                <td>{result_list[5].get('hours', [])}</td>
                <td>{result_list[5].get('teacher_info', [])}</td>
            </tr>
            <tr>
                <td>{result_list[6].get('legal_name')}</td>
                <td>{result_list[6].get('discipline_name')}</td>
                <td>{result_list[6].get('gradebook_type')}</td>
                <td>{result_list[6].get('semester_students', [])}</td>
                <td>{result_list[6].get('hours', [])}</td>
                <td>{result_list[6].get('teacher_info', [])}</td>
            </tr>
            <tr style="background-color: #ecf2fb">
                <td>{result_list[7].get('legal_name')}</td>
                <td>{result_list[7].get('discipline_name')}</td>
                <td>{result_list[7].get('gradebook_type')}</td>
                <td>{result_list[7].get('semester_students', [])}</td>
                <td>{result_list[7].get('hours', [])}</td>
                <td>{result_list[7].get('teacher_info', [])}</td>
            </tr>
            <tr>
                <td>{result_list[8].get('legal_name')}</td>
                <td>{result_list[8].get('discipline_name')}</td>
                <td>{result_list[8].get('gradebook_type')}</td>
                <td>{result_list[8].get('semester_students', [])}</td>
                <td>{result_list[8].get('hours', [])}</td>
                <td>{result_list[8].get('teacher_info', [])}</td>
            </tr>
        </table>
    </body>
</html>
"""
    return page


@app.route('/', methods=["POST", "GET"])
def hello_world():

    global auth_cookie

    if request.method == "POST":
        ksu_login = request.form['login']
        ksu_password = request.form['password']

        auth = requests.post("https://ksu24.kspu.edu/api/v2/login/", data={
            'username': ksu_login,
            'password': ksu_password
        })

        if not auth.ok:
            print(f"Помилка аутентифікації. Код:{auth.status_code} {auth.text}")
            auth.raise_for_status()
        else:
            print(f"Аутентифікація успішна. Статус код:{auth.status_code}")

        auth_cookie = auth.cookies.get_dict()["JWT"]
        response = requests.get(url="https://ksu24.kspu.edu/api/v2/my/profile/", cookies={'JWT': auth_cookie})
        data = response.json()

        return format_profile(data)

    return login_page


@app.route('/recordbook', methods=["POST", "GET"])
def recordbook():

    global auth_cookie

    if request.method == "POST":
        profile_id = get_value(
            "https://ksu24.kspu.edu/api/v2/my/students/",
            auth_cookie, 'id'
        )

        recordbook_id = get_value(
            "https://ksu24.kspu.edu/api/v2/my/students/"+str(profile_id)+"/recordbooks/",
            auth_cookie, 'id'
        )
        response = requests.get(
            "https://ksu24.kspu.edu/api/v2/my/students/"+str(profile_id)+"/recordbooks/"+str(recordbook_id)+"/records/",
            cookies={
                "JWT": auth_cookie
            }
        )

        data = response.json()

        return profile_recordbook(data)

    return login_page


@app.route('/gradebook', methods=["POST", "GET"])
def gradebook():

    global auth_cookie

    if request.method == "POST":

        response = requests.get(
            "https://ksu24.kspu.edu/api/gradebook/personal_student_gradebook/",
            cookies={
                "JWT": auth_cookie
            }
        )
        data = response.json()

        return profile_gradebook(data)

    return login_page


if __name__ == '__main__':
    app.run()
