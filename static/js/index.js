function openDatePicker() {
    document.getElementById('date-picker').classList.toggle('hidden');
}

function updateSelectedDate() {
    const selectedDate = document.getElementById('datepicker').value;
    document.getElementById('selected-date').innerText = selectedDate;
    document.getElementById('date-picker').classList.add('hidden');
}
