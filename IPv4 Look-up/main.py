import requests, json, ipaddress
from flask import Flask, jsonify, request

app = Flask(__name__)

class Lookup:
    @app.route("/GitHub/xHookah/IPv4LookUp/", methods=["GET", "POST"])
    def ip():
        ip = request.args.get('ip')
        if ip == None: return jsonify({"Error": "You did not specify IPv4."})

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv102.0) Gecko/20100101 Firefox/102.0"}

        if len(ip) > 16:
            return jsonify({"Error": f"Sorry but length of IPv4: {int(ip)} is to long."})
        try:
            ip = requests.get(f"http://ip-api.com/json/{ip}", headers=headers)
            ip = json.loads(ip.text)
        except:
            return jsonify({"Error": "Could not make a GET request to the IPv4 Look-up API."})
        try:
            country = ip['country']
            isp = ip['isp']
            org = ip['org']
            city = ip['city']
            region_name = ip['regionName']
            zip_code = ip['zip']
            country_code = ip['countryCode']
            query = ip['query']

            json_format = {
                "Country": country,
                "ISP": isp,
                "Organization": org,
                "City": city,
                "Region": region_name,
                "ZIP/Postal": zip_code,
                "Country Code": country_code,
                "Query": query
            }

            return jsonify(json_format)
        except Exception as error:
            print(error)
            return jsonify({"Error": f"IPv4: {int(ip)} is invalid."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)