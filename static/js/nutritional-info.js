document.addEventListener("DOMContentLoaded", function () {
    // Fetch the JSON data
    fetch("/static/json/2024-01-21.json")
        .then(response => response.json())
        .then(data => {
            // Replace "YourItemName" with the actual name of the item you want to display
            const itemName = "BBQ Pork Ribette";
            const item = data.find(item => item.items.some(i => i.name === itemName));

            if (item) {
                displayNutritionFacts(item.items.find(i => i.name === itemName));
                displayAllergens(item.items.find(i => i.name === itemName));
                displayIngredients(item.items.find(i => i.name === itemName));
            } else {
                alert("Item not found in the JSON data.");
            }
        })
        .catch(error => console.error("Error fetching JSON data:", error));
});

function displayNutritionFacts(item) {
    // Helper function to handle NaN values
    function replaceNaN(value) {
        if (value == "nan") {
            return 0;
        } else {
            return value;
        }
    }

    document.getElementById("ss").textContent = replaceNaN(item.SS);
    document.getElementById("c").textContent = replaceNaN(item.C);
    document.getElementById("tf").textContent = replaceNaN(item.TF);
    document.getElementById("sf").textContent = replaceNaN(item.SF);
    document.getElementById("ch").textContent = replaceNaN(item.Ch);
    document.getElementById("na").textContent = replaceNaN(item.Na);
    document.getElementById("carb").textContent = replaceNaN(item.Carb);
    document.getElementById("su").textContent = replaceNaN(item.Su);
    document.getElementById("p").textContent = replaceNaN(item.P);
}

function displayAllergens(item) {
    const allergensContainer = document.getElementById("allergen-icons");
    item.Allergens.split(", ").forEach(allergen => {
        const iconLink = `https://api.hfs.purdue.edu/Menus/Content/dietaryTagIcons/PurdueMenusIcons_${allergen}.svg`;
        const iconContainer = document.createElement("div");
        iconContainer.classList.add("allergen-icon");
        iconContainer.innerHTML = `<img src="${iconLink}" alt="${allergen}">`;
        const nameContainer = document.createElement("div");
        nameContainer.classList.add("allergen-name");
        nameContainer.textContent = allergen;
        const allergenDiv = document.createElement("div");
        allergenDiv.appendChild(iconContainer);
        allergenDiv.appendChild(nameContainer);
        allergensContainer.appendChild(allergenDiv);
    });
}

function displayIngredients(item) {
    const ingredientsContainer = document.getElementById("ingredient-list");
    const ingredientsList = item.Ingredients.split(", ");
    ingredientsList.forEach(ingredient => {
        const ingredientDiv = document.createElement("div");
        ingredientDiv.textContent = ingredient;
        ingredientsContainer.appendChild(ingredientDiv);
    });
}
