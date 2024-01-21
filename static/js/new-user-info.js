document.addEventListener("DOMContentLoaded", function () {
    const sexButtons = document.querySelectorAll(".sex-option");
    const activityButtons = document.querySelectorAll(".activity-buttons button");
    const ageSlider = document.getElementById("age");
    const ageValue = document.getElementById("age-value");

    sexButtons.forEach(button => {
        button.addEventListener("click", function () {
            // Reset all buttons to default style
            sexButtons.forEach(btn => {
                btn.classList.remove("male", "female", "rather_not_say");
            });

            // Apply selected style to the clicked button
            button.classList.add(button.dataset.value);
        });
    });

    activityButtons.forEach(button => {
        button.addEventListener("click", function() {
            // Reset all buttons to default style
            activityButtons.forEach(btn => {
                btn.style.backgroundColor = "#ffffff";
                btn.style.color = "#00aa00";
            });

            // Apply selected style to the clicked button
            button.style.backgroundColor = "#00aa00";
            button.style.color = "#ffffff";
        });
    });

    // Update age value display on slider change
    ageSlider.addEventListener("input", function () {
        ageValue.textContent = this.value;
    });
});

function resetPreferences() {
    // Reload the page to reset preferences
    location.reload();
}

function submitPreferences() {
    // Add your logic for submitting preferences here
    // For now, you can leave it empty or add a link to the href attribute
    document.getElementById("submitButton").setAttribute("href", "your_submission_link_here");
}
function validateAgeInput(input) {
    // Allow only numeric values
    input.value = input.value.replace(/[^0-9]/g, '');

    // Limit to a minimum value of 0
    if (parseInt(input.value) < 0) {
        input.value = '0';
    }

    // Limit to a maximum value of 150
    if (parseInt(input.value) > 150) {
        input.value = '150';
    }
}
function validateHeightInput(input) {
    // Allow only numeric values
    input.value = input.value.replace(/[^0-9.]/g, '');

    // Ensure there is at most one decimal point
    let decimalCount = (input.value.match(/\./g) || []).length;
    if (decimalCount > 1) {
        // More than one decimal point, remove the extra ones
        input.value = input.value.slice(0, input.value.lastIndexOf('.'));
    }

    // Limit to a minimum value of 0
    if (parseInt(input.value) < 0) {
        input.value = '0';
    }

    // Limit to a maximum value of 300
    if (parseInt(input.value) > 300) {
        input.value = '300';
    }
}
function validateWeightInput(input) {
    // Allow only numeric values
    input.value = input.value.replace(/[^0-9.]/g, '');

    // Ensure there is at most one decimal point
    let decimalCount = (input.value.match(/\./g) || []).length;
    if (decimalCount > 1) {
        // More than one decimal point, remove the extra ones
        input.value = input.value.slice(0, input.value.lastIndexOf('.'));
    }

    // Limit to a minimum value of 0
    if (parseInt(input.value) < 0) {
        input.value = '0';
    }

    // Limit to a maximum value of 600
    if (parseInt(input.value) > 600) {
        input.value = '600';
    }
}

function selectGoal(goal) {
    // Reset all buttons
    document.getElementById('bulkButton').classList.remove('selected');
    document.getElementById('cutButton').classList.remove('selected');
    document.getElementById('maintainButton').classList.remove('selected');

    // Set the selected button
    document.getElementById(goal + 'Button').classList.add('selected');
}