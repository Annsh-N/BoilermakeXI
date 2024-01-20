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


def get_dfs(theplace):
    earhart = pd.DataFrame(
        columns=[
            "Station Name",
            "Item Name",
            "Calories",
            "Total Fat",
            "Cholestrol",
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
        ]
    )
    url = (
        "https://api.hfs.purdue.edu/menus/v2/locations/"
        + theplace
        + "/"
        + datetime.date.today().strftime("%Y-%m-%d")
    )

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
            earhart.at[item_val, "Station Name"] = value = station.get("Name")

            items = station.get("Items", [])
            for item in items:
                item_id = item.get("ID", [])
                item_response = requests.get(item_url + item_id)
                item_json_content = item_response.content
                item_json_data_string = item_json_content.decode("utf-8")
                item_json_data = json.loads(item_json_data_string)
                earhart.at[item_val, "Item Name"] = item_json_data.get("Name")

                for nutrition_entry in item_json_data.get("Nutrition", []):
                    if nutrition_entry.get("Name") == "Calories":
                        earhart.at[item_val, "Calories"] = nutrition_entry.get("Value")

                    elif nutrition_entry.get("Name") == "Total fat":
                        earhart.at[item_val, "Total Fat"] = nutrition_entry.get("Value")

                    elif nutrition_entry.get("Name") == "Cholesterol":
                        earhart.at[item_val, "Cholestrol"] = nutrition_entry.get(
                            "Value"
                        )

                    elif nutrition_entry.get("Name") == "Sodium":
                        earhart.at[item_val, "Sodium"] = nutrition_entry.get("Value")

                    elif nutrition_entry.get("Name") == "Total Carbohydrate":
                        earhart.at[item_val, "Total Carbs"] = nutrition_entry.get(
                            "Value"
                        )

                    elif nutrition_entry.get("Name") == "Sugar":
                        earhart.at[item_val, "Sugar"] = nutrition_entry.get("Value")

                    elif nutrition_entry.get("Name") == "Added Sugar":
                        earhart.at[item_val, "Added Sugar"] = nutrition_entry.get(
                            "Value"
                        )

                    elif nutrition_entry.get("Name") == "Dietary Fiber":
                        earhart.at[item_val, "Dietary Fiber"] = nutrition_entry.get(
                            "Value"
                        )

                    elif nutrition_entry.get("Name") == "Protein":
                        earhart.at[item_val, "Protein"] = nutrition_entry.get("Value")

                    elif nutrition_entry.get("Name") == "Calcium":
                        earhart.at[item_val, "Calcium"] = nutrition_entry.get("Value")

                    elif nutrition_entry.get("Name") == "Iron":
                        earhart.at[item_val, "Iron"] = nutrition_entry.get("Value")

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


from IPython.display import display

pd.set_option("display.max_columns", None)

ear = get_dfs("Earhart")
display(ear)

wiley = get_dfs("Wiley")
display(wiley)

ford = get_dfs("Ford")
display(ford)

windsor = get_dfs("Windsor")
display(windsor)

hillenbrand = get_dfs("Hillenbrand")
display(hillenbrand)
