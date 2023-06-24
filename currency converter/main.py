from flask import render_template,Flask,request
import requests
import json

app = Flask(__name__)

url = f"http://api.exchangeratesapi.io/v1/latest?access_key=db0c18c12b283976e7e890f63120934a"
response = requests.get(url)
curr = json.loads(response.text)
curr_lst = list(curr["rates"].keys())
@app.route("/",methods=["GET","POST"])
def home():
    ans=0
    first = request.form.get("first")
    print(first)
    second = request.form.get("second")
    print(second)
    amount = request.form.get("amount")
    print(amount)
    if first and second and amount:
        ans =  (int(amount)*curr["rates"][second])//curr["rates"][first]
    return render_template("index.html",curr_lst=curr_lst,ans = ans)
if __name__ == "__main__":
    app.run(debug=True)