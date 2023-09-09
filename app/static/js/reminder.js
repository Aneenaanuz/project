// static/js/reminder.js
document.addEventListener("DOMContentLoaded", function () {
    const reminderForm = document.getElementById("reminder-form");
    const reminderList = document.getElementById("reminder-list");

    reminderForm.addEventListener("submit", function (e) {
        e.preventDefault();
        const name = document.getElementById("reminder-name").value;
        const time = document.getElementById("reminder-time").value;

        // Add the reminder to the list
        const reminderItem = document.createElement("li");
        reminderItem.innerHTML = `<strong>${name}</strong> - ${time}`;
        reminderList.querySelector("ul").appendChild(reminderItem);

        // Clear the form
        reminderForm.reset();
    });

    // Additional code here to handle real-time reminders
});
