import tkinter as tk
from tkinter import messagebox
# International phone code dictionary.
# Structure:
# - If a country has a single prefix, it's assigned directly as a string.
# - If a country shares a prefix with others (like +1 and +7), an internal dictionary with subcodes is used.

phone_codes = {
    "+1": {
        # United States
        "202": "United States", "212": "United States",
        # Canada
        "403": "Canada", "416": "Canada",
        # Caribbean
        "268": "Antigua and Barbuda", "242": "Bahamas",
        "246": "Barbados", "767": "Dominica",
        "809": "Dominican Republic", "829": "Dominican Republic",
        "849": "Dominican Republic", "473": "Grenada",
        "876": "Jamaica", "869": "Saint Kitts and Nevis",
        "758": "Saint Lucia", "784": "Saint Vincent and the Grenadines",
        "868": "Trinidad and Tobago"
    },
    "+7": {
        # Russia
        **{str(code): "Russia" for code in [
            *range(301, 310), *range(381, 390),
            *range(401, 415), 421, 423, 424, 426, 427, 428,
            *range(471, 476), *range(481, 486), *range(491, 500),
            800, *range(901, 910), *range(911, 920),
            *range(920, 930), *range(930, 940), *range(950, 960),
            *range(960, 970), *range(970, 980), *range(980, 990),
            *range(991, 1000)
        ]},
        # Kazakhstan
        **{str(code): "Kazakhstan" for code in range(700, 729)},
        # Shared zones (unclear classification)
        **{str(code): "Shared" for code in [
            *range(100, 110), *range(801, 810), *range(881, 890)
        ]}
    },
    # Unique prefixes (one country per prefix)
    "+93": "Afghanistan",
    "+355": "Albania",
    "+213": "Algeria",
    "+376": "Andorra",
    "+244": "Angola",
    "+54": "Argentina",
    "+374": "Armenia",
    "+61": "Australia",
    "+43": "Austria",
    "+994": "Azerbaijan",
    "+973": "Bahrain",
    "+880": "Bangladesh",
    "+375": "Belarus",
    "+32": "Belgium",
    "+501": "Belize",
    "+229": "Benin",
    "+975": "Bhutan",
    "+591": "Bolivia",
    "+387": "Bosnia and Herzegovina",
    "+267": "Botswana",
    "+55": "Brazil",
    "+673": "Brunei",
    "+359": "Bulgaria",
    "+226": "Burkina Faso",
    "+257": "Burundi",
    "+238": "Cabo Verde",
    "+855": "Cambodia",
    "+237": "Cameroon",
    "+236": "Central African Republic",
    "+235": "Chad",
    "+56": "Chile",
    "+86": "China",
    "+57": "Colombia",
    "+269": "Comoros",
    "+242": "Congo (Congo-Brazzaville)",
    "+506": "Costa Rica",
    "+385": "Croatia",
    "+53": "Cuba",
    "+357": "Cyprus",
    "+420": "Czech Republic",
    "+243": "Democratic Republic of the Congo",
    "+45": "Denmark",
    "+253": "Djibouti",
    "+593": "Ecuador",
    "+20": "Egypt",
    "+503": "El Salvador",
    "+240": "Equatorial Guinea",
    "+291": "Eritrea",
    "+372": "Estonia",
    "+268": "Eswatini",
    "+251": "Ethiopia",
    "+679": "Fiji",
    "+358": "Finland",
    "+33": "France",
    "+241": "Gabon",
    "+220": "Gambia",
    "+995": "Georgia",
    "+49": "Germany",
    "+233": "Ghana",
    "+30": "Greece",
    "+502": "Guatemala",
    "+224": "Guinea",
    "+245": "Guinea-Bissau",
    "+592": "Guyana",
    "+509": "Haiti",
    "+504": "Honduras",
    "+36": "Hungary",
    "+354": "Iceland",
    "+91": "India",
    "+62": "Indonesia",
    "+98": "Iran",
    "+964": "Iraq",
    "+353": "Ireland",
    "+972": "Israel",
    "+39": "Italy",
    "+81": "Japan",
    "+962": "Jordan",
    "+254": "Kenya",
    "+686": "Kiribati",
    "+965": "Kuwait",
    "+996": "Kyrgyzstan",
    "+856": "Laos",
    "+371": "Latvia",
    "+961": "Lebanon",
    "+266": "Lesotho",
    "+231": "Liberia",
    "+218": "Libya",
    "+423": "Liechtenstein",
    "+370": "Lithuania",
    "+352": "Luxembourg",
    "+261": "Madagascar",
    "+265": "Malawi",
    "+60": "Malaysia",
    "+960": "Maldives",
    "+223": "Mali",
    "+356": "Malta",
    "+692": "Marshall Islands",
    "+222": "Mauritania",
    "+230": "Mauritius",
    "+52": "Mexico",
    "+691": "Micronesia",
    "+373": "Moldova",
    "+377": "Monaco",
    "+976": "Mongolia",
    "+382": "Montenegro",
    "+212": "Morocco",
    "+258": "Mozambique",
    "+95": "Myanmar",
    "+264": "Namibia",
    "+674": "Nauru",
    "+977": "Nepal",
    "+31": "Netherlands",
    "+64": "New Zealand",
    "+505": "Nicaragua",
    "+227": "Niger",
    "+234": "Nigeria",
    "+850": "North Korea",
    "+389": "North Macedonia",
    "+47": "Norway",
    "+968": "Oman",
    "+92": "Pakistan",
    "+680": "Palau",
    "+970": "Palestine",
    "+507": "Panama",
    "+675": "Papua New Guinea",
    "+595": "Paraguay",
    "+51": "Peru",
    "+63": "Philippines",
    "+48": "Poland",
    "+351": "Portugal",
    "+974": "Qatar",
    "+40": "Romania",
    "+250": "Rwanda",
    "+685": "Samoa",
    "+378": "San Marino",
    "+239": "Sao Tome and Principe",
    "+966": "Saudi Arabia",
    "+221": "Senegal",
    "+381": "Serbia",
    "+248": "Seychelles",
    "+232": "Sierra Leone",
    "+65": "Singapore",
    "+421": "Slovakia",
    "+386": "Slovenia",
    "+677": "Solomon Islands",
    "+252": "Somalia",
    "+27": "South Africa",
    "+82": "South Korea",
    "+211": "South Sudan",
    "+34": "Spain",
    "+94": "Sri Lanka",
    "+249": "Sudan",
    "+597": "Suriname",
    "+46": "Sweden",
    "+41": "Switzerland",
    "+963": "Syria",
    "+886": "Taiwan",
    "+992": "Tajikistan",
    "+255": "Tanzania",
    "+66": "Thailand",
    "+670": "Timor-Leste",
    "+228": "Togo",
    "+676": "Tonga",
    "+216": "Tunisia",
    "+90": "Turkey",
    "+993": "Turkmenistan",
    "+688": "Tuvalu",
    "+256": "Uganda",
    "+380": "Ukraine",
    "+971": "United Arab Emirates",
    "+44": "United Kingdom",
    "+598": "Uruguay",
    "+998": "Uzbekistan",
    "+678": "Vanuatu",
    "+379": "Vatican City (Holy See)",
    "+58": "Venezuela",
    "+84": "Vietnam",
    "+967": "Yemen",
    "+260": "Zambia",
    "+263": "Zimbabwe"
}


# Function to identify the country (or region) based on the phone number
def identify_country(number):
    # Remove spaces and hyphens from the input number
    num = number.replace(" ", "").replace("-", "")

    # Loop through all known prefixes, sorted from longest to shortest
    for pref in sorted(phone_codes.keys(), key=lambda x: -len(x)):
        # Check if the number starts with this prefix
        if num.startswith(pref):
            remainder = num[len(pref):]  # Get the remaining part of the number after the prefix
            val = phone_codes[pref]     # Get the value associated with this prefix

            if isinstance(val, str):
                # If the value is a string, it's a direct country name
                return val
            elif isinstance(val, dict):
                # If it's a dict, check subcodes
                for sub in sorted(val.keys(), key=lambda x: -len(x)):
                    if remainder.startswith(sub):
                        return val[sub]
                return f"Prefix {pref} recognized, but subcode not identified."
    
    # If no prefix matches
    return "Prefix not recognized."


# Function called when the user clicks the "Identify Country" button
def search():
    number = entry.get()  # Get the phone number entered by the user
    if not number.startswith("+"):
        # Show a warning if the number doesn't start with "+"
        messagebox.showwarning("Input Error", "Number must start with '+'.")
        return
    result = identify_country(number)  # Call the identification function
    result_label.config(text=f"Result: {result}")  # Display the result in the label


# Graphical User Interface (GUI) using tkinter
root = tk.Tk()
root.title("International Phone Prefix Identifier")  # Title of the window
root.geometry("400x200")  # Set fixed window size
root.resizable(False, False)  # Disable resizing

# Label asking for user input
tk.Label(root, text="Enter phone number:").pack(pady=10)

# Entry field for the user to input the phone number
entry = tk.Entry(root, width=30)
entry.pack()

# Button to trigger the identification function
tk.Button(root, text="Identify Country", command=search).pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="Result: ", font=("Helvetica", 12))
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()

