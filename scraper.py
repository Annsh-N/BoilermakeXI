"""from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("trial_index.html")
"""
import datetime
import requests
import json
import pandas as pd
from IPython.display import display

pd.set_option("display.max_columns", None)


def get_dfs(theplace, curr_date):
    earhart = pd.DataFrame(
        columns=[
            "Station Name",
            "Item Name",
            "Calories",
            "Total Fat",
            "Cholesterol",
            "Sodium",
            "Total Carbs",
            "Sugar",
            "Added Sugar",
            "Dietary Fiber",
            "Protein",
            "Calcium",
            "Iron",
            "Ingredients",
            "Allergens",
            "Serving Size",
            "Saturated Fat",
        ]
    )
    url = "https://api.hfs.purdue.edu/menus/v2/locations/" + theplace + "/" + curr_date

    response = requests.get(url)
    json_content = response.content
    json_data_string = json_content.decode("utf-8")
    json_data = json.loads(json_data_string)
    # Extract 'Meals' and 'Stations' information
    meals = json_data.get("Meals", [])

    item_url = "https://api.hfs.purdue.edu/menus/v2/items/"
    item_val = 0
    # Iterate through meals to find 'Stations'
    for meal in meals:
        stations = meal.get("Stations", [])
        for station in stations:
            # Now 'station' contains information about each station

            items = station.get("Items", [])
            for item in items:
                earhart.at[item_val, "Station Name"] = station.get("Name")
                item_id = item.get("ID", [])
                item_response = requests.get(item_url + item_id)
                item_json_content = item_response.content
                item_json_data_string = item_json_content.decode("utf-8")
                item_json_data = json.loads(item_json_data_string)
                earhart.at[item_val, "Item Name"] = item_json_data.get("Name")
                for nutrition_entry in item_json_data.get("Nutrition", []):
                    if nutrition_entry.get("Name") == "Calories":
                        earhart.at[item_val, "Calories"] = nutrition_entry.get(
                            "LabelValue"
                        )

                    elif nutrition_entry.get("Name") == "Total fat":
                        earhart.at[item_val, "Total Fat"] = nutrition_entry.get(
                            "LabelValue"
                        )

                    elif nutrition_entry.get("Name") == "Cholesterol":
                        earhart.at[item_val, "Cholesterol"] = nutrition_entry.get(
                            "LabelValue"
                        )
                    elif nutrition_entry.get("Name") == "Serving Size":
                        earhart.at[item_val, "Serving Size"] = nutrition_entry.get(
                            "LabelValue"
                        )
                    elif nutrition_entry.get("Name") == "Sodium":
                        earhart.at[item_val, "Sodium"] = nutrition_entry.get(
                            "LabelValue"
                        )

                    elif nutrition_entry.get("Name") == "Total Carbohydrate":
                        earhart.at[item_val, "Total Carbs"] = nutrition_entry.get(
                            "LabelValue"
                        )

                    elif nutrition_entry.get("Name") == "Sugar":
                        earhart.at[item_val, "Sugar"] = nutrition_entry.get(
                            "LabelValue"
                        )

                    elif nutrition_entry.get("Name") == "Added Sugar":
                        earhart.at[item_val, "Added Sugar"] = nutrition_entry.get(
                            "LabelValue"
                        )

                    elif nutrition_entry.get("Name") == "Dietary Fiber":
                        earhart.at[item_val, "Dietary Fiber"] = nutrition_entry.get(
                            "LabelValue"
                        )

                    elif nutrition_entry.get("Name") == "Protein":
                        earhart.at[item_val, "Protein"] = nutrition_entry.get(
                            "LabelValue"
                        )
                    elif nutrition_entry.get("Name") == "Saturated Fat":
                        earhart.at[item_val, "Saturated Fat"] = nutrition_entry.get(
                            "LabelValue"
                        )

                    elif nutrition_entry.get("Name") == "Calcium":
                        earhart.at[item_val, "Calcium"] = nutrition_entry.get(
                            "DailyValue"
                        )

                    elif nutrition_entry.get("Name") == "Iron":
                        earhart.at[item_val, "Iron"] = nutrition_entry.get("DailyValue")

                earhart.at[item_val, "Ingredients"] = item_json_data.get(
                    "Ingredients", ""
                )
                allergens = ""
                for allergen in item_json_data.get("Allergens", []):
                    if allergen.get("Value") == True:
                        allergens += allergen.get("Name") + ","
                earhart.at[item_val, "Allergens"] = allergens[:-1]
                item_val += 1
    return earhart


starting = "SS = Serving Size. C = Calories. TF = Total Fat. SF = Saturated Fat. Ch = Cholesterol. Na = Sodium. Carb = Carbohydrates. Su = Sugar. P = Protein\n"


def print_in_correct_format(place, curr_date):
    ans = '{"place": "' + place + '", "items": ['
    ear = get_dfs(place, curr_date)

    for i in range(len(ear)):
        x = str(ear.at[i, "Ingredients"]).replace('"', " inch ")
        ingreds = x.replace("\n", " ")
        ingreds = ingreds.replace("\r", " ")
        ingreds = ingreds.replace("\r\n", " ")
        ans += (
            '{ "name": "'
            + str(ear.at[i, "Item Name"]).replace('"', " inch ")
            + '", "SS": "'
            + str(ear.at[i, "Serving Size"])
            + '", "C": "'
            + str(ear.at[i, "Calories"])
            + '", "TF": "'
            + str(ear.at[i, "Total Fat"])
            + '", "SF": "'
            + str(ear.at[i, "Saturated Fat"])
            + '", "Ch": "'
            + str(ear.at[i, "Cholesterol"])
            + '", "Na": "'
            + str(ear.at[i, "Sodium"])
            + '", "Carb": "'
            + str(ear.at[i, "Total Carbs"])
            + '", "Su": "'
            + str(ear.at[i, "Sugar"])
            + '", "P": "'
            + str(ear.at[i, "Protein"])
            + '", "Allergens": "'
            + str(ear.at[i, "Allergens"])
            + '", "Ingredients": "'
            + ingreds
            + '"}, '
        )

    # Remove the trailing comma and close the items array
    ans = ans.rstrip(", ") + "]}"
    return ans


for i in range(4):
    curr_date = "2024-01-" + str(26 + i)
    answer = "["
    answer += (
        print_in_correct_format("Earhart", curr_date)
        + ","
        + print_in_correct_format("Ford", curr_date)
        + ","
        + print_in_correct_format("Wiley", curr_date)
        + ","
        + print_in_correct_format("Windsor", curr_date)
        + ","
        + print_in_correct_format("Hillenbrand", curr_date)
        + ","
        + print_in_correct_format("1bowl", curr_date)
        + ","
        + print_in_correct_format("Pete's Za", curr_date)
        + ","
        + print_in_correct_format("The Burrow", curr_date)
        + "]"
    )
    f = open(curr_date + ".json", "w")
    f.write(answer)
    f.close()
