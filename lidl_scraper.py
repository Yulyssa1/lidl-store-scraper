import requests
import pandas as pd

url = "https://www.lidl.ro/sq/store-finder/api/stores"
params = {
    "latitude": 45.9432,
    "longitude": 24.9668,
    "radius": 500000
}
headers = {
    "User-Agent": "Mozilla/5.0",
    "Accept": "application/json"
}

response = requests.get(url, params=params, headers=headers)
data = response.json()

magazine = []
for magazin in data['stores']:
    magazin_info = {
        "Nume": magazin.get("name"),
        "Adresa": magazin.get("address", {}).get("street"),
        "Oraș": magazin.get("address", {}).get("city"),
        "Cod Poștal": magazin.get("address", {}).get("postalCode"),
        "Latitudine": magazin.get("coordinates", {}).get("latitude"),
        "Longitudine": magazin.get("coordinates", {}).get("longitude")
    }
    magazine.append(magazin_info)

df = pd.DataFrame(magazine)
df.to_excel("magazine_lidl_romania.xlsx", index=False)
print("Salvat în magazine_lidl_romania.xlsx")
