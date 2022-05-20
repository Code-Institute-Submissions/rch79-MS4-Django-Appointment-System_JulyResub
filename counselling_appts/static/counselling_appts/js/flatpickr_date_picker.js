// Retrieves tomorrow's date to be used as the minimum
// date on the date picker
const TODAY = new Date()
const TOMORROW = new Date()
TOMORROW.setDate(TOMORROW.getDate() + 1)

// id of the date picker element in the template view
const ELEMENT_ID = "#flatpickr"

// how far in advance, in days (counting from current date + 1)
// users will be able to book their appointments
const INCREMENT = 365


const blocked_dates = JSON.parse(document.getElementById('blocked_dates').textContent);


// datepicker 
flatpickr(ELEMENT_ID, {
    "disable": [
        function(date) {
            // disables weekends
            return (date.getDay() === 0 || date.getDay() === 6);

        }, 
        "2022-07-15",
        blocked_dates
    ],
    "locale": {
        "firstDayOfWeek": 1 // start week on Monday
    },
    minDate: TOMORROW,
    maxDate: new Date().fp_incr(INCREMENT) // 365 days from now 
});
