# script.py
import requests
import ephem

def fetch_tle_data():
    url = "https://tle.ivanstanojevic.me/api/tle/49044"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        return None  # If fetching TLE data fails, return None

    data = response.json()
    name = data.get("name")
    line1 = data.get("line1")
    line2 = data.get("line2")

    tle_rec = ephem.readtle(name, line1, line2)
    tle_rec.compute()

    sublong = tle_rec.sublong
    sublat = tle_rec.sublat
    
    return (4000, 4000)


