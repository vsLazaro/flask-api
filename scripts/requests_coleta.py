import requests

base_url = "http://127.0.0.1:5000"

def get_all_crashes():
    response = requests.get(f"{base_url}/crash")
    if response.status_code == 200:
        crashes = response.json()
        for crash in crashes:
            print(f"Crash ID: {crash['id']}, Operator: {crash['operator']}")
        return crashes
    else:
        print("An unexpected error occured while attemtping to fetch all crashes")
    

def get_crash(id):
    response = requests.get(f"{base_url}/crash/{id}")
    if response.status_code == 200:
        crash = response.json()
        print(f"Crash ID: {crash['id']}, Operator: {crash['operator']}")
        return crash
    else:
        print("An unexpected error occured while attemtping to fetch crash")

def add_crash(input):
    data = input
    response = requests.post(f"{base_url}/crash", json=data)
    if response.status_code == 201:
        print("Crash added successfully")
    else:
        print("An unexpected error occured while attemtping to add new crash")

def update_crash(crashe_id, input):
    url = f"{base_url}/crash/{crashe_id}"
    data = input
    response = requests.put(url, json=data)
    if response.status_code == 200:
        print("Crash updated successfully")
    else:
        print("An unexpected error occured while attemtping to update crash")

def delete_crash(id):
    response = requests.delete(f"{base_url}/crash/{id}")
    if response.status_code == 200:
        print("Crash deleted successfully")
    else:
        print("An unexpected error occured while attemtping to delete crash")

all_crashes = get_all_crashes()
crash = get_crash(all_crashes[0]['id'])
crash_with_updated_date = crash
crash_with_updated_date['description'] = 'January 21, 2014'
update_crash(crashe_id=crash_with_updated_date['id'], input=crash_with_updated_date)

delete_crash(id=crash_with_updated_date['id'])

add_crash(input={
    "date": "2023-10-01",
    "time": "1200",
    "location": "Porto Alegre",
    "operator": "Operador da aeronave",
    "flight_number": "Número do voo",
    "route": "Rota do voo",
    "ac_type": "Tipo de aeronave",
    "registration": "Número de registro",
    "cn_ln": "Número de série / Linha de construção",
    "aboard": "Número de pessoas a bordo",
    "fatalities": "Número de fatalidades",
    "ground": "Número de vítimas em solo",
    "summary": "Resumo do acidente"
})