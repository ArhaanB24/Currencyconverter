from flask import render_template,Flask,request,flash
import requests
import json
# from Countrydetails import countries


app = Flask(__name__)
app.secret_key = "VK18"

# country = countries.all_countries()
namdict = {'Afghanistan': 'AFN', 'Aland Islands': 'EUR', 'Albania': 'ALL', 'Algeria': 'DZD', 'American Samoa': 'USD', 'Andorra': 'EUR', 'Angola': 'AOA', 'Anguilla': 'XCD', 'Antarctica': '', 'Antigua And Barbuda': 'XCD', 'Argentina': 'ARS', 'Armenia': 'AMD', 'Aruba': 'AWG', 'Australia': 'AUD', 'Austria': 'EUR', 'Azerbaijan': 'AZN', 'Bahamas The': 'BSD', 'Bahrain': 'BHD', 'Bangladesh': 'BDT', 'Barbados': 'BBD', 'Belarus': 'BYR', 'Belgium': 'EUR', 'Belize': 'BZD', 'Benin': 'XOF', 'Bermuda': 'BMD', 'Bhutan': 'BTN', 'Bolivia': 'BOB', 'Bosnia and Herzegovina': 'BAM', 'Botswana': 'BWP', 'Bouvet Island': 'NOK', 'Brazil': 'BRL', 'British Indian Ocean Territory': 'USD', 'Brunei': 'BND', 'Bulgaria': 'BGN', 'Burkina Faso': 'XOF', 'Burundi': 'BIF', 'Cambodia': 'KHR', 'Cameroon': 'XAF', 'Canada': 'CAD', 'Cape Verde': 'CVE', 'Cayman Islands': 'KYD', 'Central African Republic': 'XAF', 'Chad': 'XAF', 'Chile': 'CLP', 'China': 'CNY', 'Christmas Island': 'AUD', 'Cocos (Keeling) Islands': 'AUD', 'Colombia': 'COP', 'Comoros': 'KMF', 'Congo': 'XAF', 'Congo The Democratic Republic Of The': 'CDF', 'Cook Islands': 'NZD', 'Costa Rica': 'CRC', "Cote D'Ivoire (Ivory Coast)": 'XOF', 'Croatia (Hrvatska)': 'HRK', 'Cuba': 'CUP', 'Cyprus': 'EUR', 'Czech Republic': 'CZK', 'Denmark': 'DKK', 'Djibouti': 'DJF', 'Dominica': 'XCD', 'Dominican Republic': 'DOP', 'East Timor': 'USD', 'Ecuador': 'USD', 'Egypt': 'EGP', 'El Salvador': 'USD', 'Equatorial Guinea': 'XAF', 'Eritrea': 'ERN', 'Estonia': 'EUR', 'Ethiopia': 'ETB', 'Falkland Islands': 'FKP', 'Faroe Islands': 'DKK', 'Fiji Islands': 'FJD', 'Finland': 'EUR', 'France': 'EUR', 'French Guiana': 'EUR', 'French Polynesia': 'XPF', 'French Southern Territories': 'EUR', 'Gabon': 'XAF', 'Gambia The': 'GMD', 'Georgia': 'GEL', 'Germany': 'EUR', 'Ghana': 'GHS', 'Gibraltar': 'GIP', 'Greece': 'EUR', 'Greenland': 'DKK', 'Grenada': 'XCD', 'Guadeloupe': 'EUR', 'Guam': 'USD', 'Guatemala': 'GTQ', 'Guernsey and Alderney': 'GBP', 'Guinea': 'GNF', 'Guinea-Bissau': 'XOF', 'Guyana': 'GYD', 'Haiti': 'HTG', 'Heard and McDonald Islands': 'AUD', 'Honduras': 'HNL', 'Hong Kong S.A.R.': 'HKD', 'Hungary': 'HUF', 'Iceland': 'ISK', 'India': 'INR', 'Indonesia': 'IDR', 'Iran': 'IRR', 'Iraq': 'IQD', 'Ireland': 'EUR', 'Israel': 'ILS', 'Italy': 'EUR', 'Jamaica': 'JMD', 'Japan': 'JPY', 'Jersey': 'GBP', 'Jordan': 'JOD', 'Kazakhstan': 'KZT', 'Kenya': 'KES', 'Kiribati': 'AUD', 'Korea North': 'KPW', 'Korea South': 'KRW', 'Kuwait': 'KWD', 'Kyrgyzstan': 'KGS', 'Laos': 'LAK', 'Latvia': 'EUR', 'Lebanon': 'LBP', 'Lesotho': 'LSL', 'Liberia': 'LRD', 'Libya': 'LYD', 'Liechtenstein': 'CHF', 'Lithuania': 'LTL', 'Luxembourg': 'EUR', 'Macau S.A.R.': 'MOP', 'Macedonia': 'MKD', 'Madagascar': 'MGA', 'Malawi': 'MWK', 'Malaysia': 'MYR', 'Maldives': 'MVR', 'Mali': 'XOF', 'Malta': 'EUR', 'Man (Isle of)': 'GBP', 'Marshall Islands': 'USD', 'Martinique': 'EUR', 'Mauritania': 'MRO', 'Mauritius': 'MUR', 'Mayotte': 'EUR', 'Mexico': 'MXN', 'Micronesia': 'USD', 'Moldova': 'MDL', 'Monaco': 'EUR', 'Mongolia': 'MNT', 'Montenegro': 'EUR', 'Montserrat': 'XCD', 'Morocco': 'MAD', 'Mozambique': 'MZN', 'Myanmar': 'MMK', 'Namibia': 'NAD', 'Nauru': 'AUD', 'Nepal': 'NPR', 'Netherlands Antilles': '', 'Netherlands The': 'EUR', 'New Caledonia': 'XPF', 'New Zealand': 'NZD', 'Nicaragua': 'NIO', 'Niger': 'XOF', 'Nigeria': 'NGN', 'Niue': 'NZD', 'Norfolk Island': 'AUD', 'Northern Mariana Islands': 'USD', 'Norway': 'NOK', 'Oman': 'OMR', 'Pakistan': 'PKR', 'Palau': 'USD', 'Palestinian Territory Occupied': 'ILS', 'Panama': 'PAB', 'Papua new Guinea': 'PGK', 'Paraguay': 'PYG', 'Peru': 'PEN', 'Philippines': 'PHP', 'Pitcairn Island': 'NZD', 'Poland': 'PLN', 'Portugal': 'EUR', 'Puerto Rico': 'USD', 'Qatar': 'QAR', 'Reunion': 'EUR', 'Romania': 'RON', 'Russia': 'RUB', 'Rwanda': 'RWF', 'Saint Helena': 'SHP', 'Saint Kitts And Nevis': 'XCD', 'Saint Lucia': 'XCD', 'Saint Pierre and Miquelon': 'EUR', 'Saint Vincent And The Grenadines': 'XCD', 'Saint-Barthelemy': 'EUR', 'Saint-Martin (French part)': 'EUR', 'Samoa': 'WST', 'San Marino': 'EUR', 'Sao Tome and Principe': 'STD', 'Saudi Arabia': 'SAR', 'Senegal': 'XOF', 'Serbia': 'RSD', 'Seychelles': 'SCR', 'Sierra Leone': 'SLL', 'Singapore': 'SGD', 'Slovakia': 'EUR', 'Slovenia': 'EUR', 'Solomon Islands': 'SBD', 'Somalia': 'SOS', 'South Africa': 'ZAR', 'South Georgia': 'GBP', 'South Sudan': 'SSP', 'Spain': 'EUR', 'Sri Lanka': 'LKR', 'Sudan': 'SDG', 'Suriname': 'SRD', 'Svalbard And Jan Mayen Islands': 'NOK', 'Swaziland': 'SZL', 'Sweden': 'SEK', 'Switzerland': 'CHF', 'Syria': 'SYP', 'Taiwan': 'TWD', 'Tajikistan': 'TJS', 'Tanzania': 'TZS', 'Thailand': 'THB', 'Togo': 'XOF', 'Tokelau': 'NZD', 'Tonga': 'TOP', 'Trinidad And Tobago': 'TTD', 'Tunisia': 'TND', 'Turkey': 'TRY', 'Turkmenistan': 'TMT', 'Turks And Caicos Islands': 'USD', 'Tuvalu': 'AUD', 'Uganda': 'UGX', 'Ukraine': 'UAH', 'United Arab Emirates': 'AED', 'United Kingdom': 'GBP', 'United States of America': 'USD', 'United States Minor Outlying Islands': 'USD', 'Uruguay': 'UYU', 'Uzbekistan': 'UZS', 'Vanuatu': 'VUV', 'Vatican City State (Holy See)': 'EUR', 'Venezuela': 'VEF', 'Vietnam': 'VND', 'Virgin Islands (British)': 'USD', 'Virgin Islands (US)': 'USD', 'Wallis And Futuna Islands': 'XPF', 'Western Sahara': 'MAD', 'Yemen': 'YER', 'Zambia': 'ZMK', 'Zimbabwe': 'ZWL'}
url = f"http://api.exchangeratesapi.io/v1/latest?access_key=db0c18c12b283976e7e890f63120934a"
response = requests.get(url)
new = {}
for i,j in list(namdict.items()):
    new[f"{i}:{j}"] = j

curr = json.loads(response.text)
curr_lst = list(new.keys())
@app.route("/",methods=["GET","POST"])
def home():
    ans = 0
    first = ""
    second = ""
    first = request.form.get("first")
    second = request.form.get("second")
    amount = request.form.get("amount")
    if first and second and amount:
        try:
            ans = (int(amount)*curr["rates"][new[second]])//curr["rates"][new[first]]
        except ValueError:
            flash("Please enter valid value")
        except KeyError:
            flash("Country not available")
    return render_template("index.html",curr_lst=curr_lst,ans = ans)
if __name__ == "__main__":
    app.run(debug=True)
