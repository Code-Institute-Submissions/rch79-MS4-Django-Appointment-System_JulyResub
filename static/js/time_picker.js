
var currentDateTime = new Date()

new AppointmentPicker(document.getElementById('time-ev'), {
	interval: 60,
	minTime: 09,
	maxTime: 18,
	disabled: ['12:00', '11:00']
});
// Add event listener on input field
document.getElementById('time-ev').addEventListener('change.appo.picker', function (e) {
	document.getElementById('time-ev-out').innerHTML = JSON.stringify(e.time) + ', ' + JSON.stringify(e.displayTime);
}, false);
document.getElementById('time-ev').addEventListener('close.appo.picker', function (e) {
	document.getElementById('action-ev-out').innerHTML = 'closed';
}, false);
document.getElementById('time-ev').addEventListener('open.appo.picker', function (e) {
	document.getElementById('action-ev-out').innerHTML = 'open';
}, false);

console.log("hello");