from flask import render_template,Flask,request,flash
import requests
import json
from Countrydetails import countries


app = Flask(__name__)
app.secret_key = "VK18"
country = countries.all_countries()
namdict = country.currencies()
url = f"http://api.exchangeratesapi.io/v1/latest?access_key=db0c18c12b283976e7e890f63120934a"
response = requests.get(url)
curr = json.loads(response.text)
curr_lst = list(namdict.keys())
@app.route("/",methods=["GET","POST"])
def home():
    ans=0
    first = request.form.get("first")
    second = request.form.get("second")
    amount = request.form.get("amount")
    if first and second and amount:
        try:
            ans = (int(amount)*curr["rates"][namdict[second]])//curr["rates"][namdict[first]]
        except ValueError:
            flash("Please enter valid value")
        except KeyError:
            flash("Country not available")
    return render_template("index.html",curr_lst=curr_lst,ans = ans)
if __name__ == "__main__":
    app.run(debug=True)
