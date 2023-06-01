import requests
import pandas as pd
import pyshorteners
import json
import csv
import matplotlib.pyplot as plt


def authentication(login: str, password: str) -> str:
    response = requests.post("https://ksu24.kspu.edu/api/v2/login/", data={
        'username': login,
        'password': password
    })

    if not response.ok:
        error_message = f"Помилка авторизації. Код: {response.status_code}. Текст: {response.text}"
        print(error_message)
        response.raise_for_status()
    else:
        print(f"Авторизація успішна. Код: {response.status_code}")

    try:
        auth_cookie = response.cookies.get_dict()["JWT"]
        return auth_cookie
    except KeyError as e:
        print(f"Помилка аутентифікації cookie: {e}")
        return None


def try_request(url: str, auth) -> dict:
    print(f"Виконання запиту {url}:")
    x = requests.get(
        url,
        cookies={
            "JWT": auth
        }
    )

    if x.ok:
        data = x.json()
        return data
    else:
        print(f"Помилка запиту. Код: {x.status_code}. Текст: {x.text}")
        return None


def coolprint(data):
    results_list = data.get('results', [data])

    print("\033[35m" + "*-" * 40 + "*" + "\033[0m")
    for dictionary in results_list:
        for key, value in dictionary.items():
            print(f"\033[1m\033[32m{key}\033[0m\t \033[33m==>\033[0m \t{value}")
        print("\033[35m" + "*-" * 40 + "*" + "\033[0m")


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


def shorten_url(url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    print("Скорочене посилання: " + shortened_url)
    return None


def save_to_excel(dataframe, file_name):
    try:
        sorted_dataframe = dataframe.sort_values(by=dataframe.columns.tolist())
        sorted_dataframe.to_excel(file_name, index=False)
        print(f"Результати збережено у файл {file_name}")
    except Exception as e:
        print(f"Помилка збереження в файл Excel: {e}")


def save_to_json(data, file_name):
    try:
        with open(file_name, 'w') as file:
            json.dump(data, file, indent=4)
        print(f"Результати збережено у файл {file_name}")
    except Exception as e:
        print(f"Помилка збереження в файл JSON: {e}")


def save_to_csv(data, file_name):
    try:
        with open(file_name, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Результати збережено у файл {file_name}")
    except Exception as e:
        print(f"Помилка збереження в файл CSV: {e}")


print("\033[1m\033[30m" + 120 * "—" + "\033[0m")

MyLogin = str(input("Логін: "))
MyPassword = str(input("Пароль:  "))

auth_cookie = authentication(MyLogin, MyPassword)

if auth_cookie is not None:
    profile_data = try_request("https://ksu24.kspu.edu/api/v2/my/profile/", auth_cookie)

    if profile_data:
        coolprint(profile_data)
        save_to_excel(pd.DataFrame([profile_data]), "profile.xlsx")
        save_to_json(profile_data, "profile.json")
        save_to_csv(profile_data, "profile.csv")
        shorten_url("https://ksu24.kspu.edu/api/v2/my/profile/")

    print("\033[1m\033[30m" + 120 * "—" + "\033[0m")
    students_data = try_request("https://ksu24.kspu.edu/api/v2/my/students/", auth_cookie)

    if students_data:
        coolprint(students_data)
        save_to_excel(pd.DataFrame(students_data["results"]), "students.xlsx")
        save_to_json(students_data, "students.json")
        save_to_csv(students_data, "students.csv")
        shorten_url("https://ksu24.kspu.edu/api/v2/my/students/")

    student_id = get_value(
        "https://ksu24.kspu.edu/api/v2/my/students/",
        auth_cookie,
        "id"
    )

    print("\033[1m\033[30m" + 120 * "—" + "\033[0m")
    recordbooks_data = try_request(
        "https://ksu24.kspu.edu/api/v2/my/students/"+str(student_id)+"/recordbooks/",
        auth_cookie)

    if recordbooks_data:
        coolprint(recordbooks_data)
        save_to_excel(pd.DataFrame(recordbooks_data["results"]), "recordbooks.xlsx")
        save_to_json(recordbooks_data, "recordbooks.json")
        save_to_csv(recordbooks_data, "recordbooks.csv")
        shorten_url("https://ksu24.kspu.edu/api/v2/my/students/"+str(student_id)+"/recordbooks/")


    recordbook_id = get_value(
        "https://ksu24.kspu.edu/api/v2/my/students/" + str(student_id) + "/recordbooks/",
        auth_cookie,
        "id"
    )

    print("\033[1m\033[30m" + 120 * "—" + "\033[0m")
    records_data = try_request(
        "https://ksu24.kspu.edu/api/v2/my/students/" + str(student_id) + "/recordbooks/" + recordbook_id + "/records",
        auth_cookie
    )

    if records_data:
        coolprint(records_data)
        save_to_excel(pd.DataFrame(records_data["results"]), "records.xlsx")
        save_to_json(records_data, "records.json")
        save_to_csv(records_data, "records.csv")
        shorten_url("https://ksu24.kspu.edu/api/v2/my/students/" + str(student_id) + "/recordbooks/" + recordbook_id + "/records")
    print("\033[1m\033[30m" + 120 * "—" + "\033[0m")

    if records_data:
        df = pd.DataFrame(records_data['results'], columns=['discipline_name', 'result'])
        df.plot(x='discipline_name', y='result', kind='bar', figsize=(10, 6))
        plt.xlabel('Назва предмету')
        plt.ylabel('Результат')
        plt.title('Оцінки за предметами')
        plt.show()


