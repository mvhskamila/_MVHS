var now = new Date();
var dateTimeString = now.toISOString();
var formattedDateTimeString = now.toLocaleString();
var timeElement = document.getElementById("current-time");
timeElement.textContent = formattedDateTimeString;
timeElement.setAttribute("datetime", dateTimeString);