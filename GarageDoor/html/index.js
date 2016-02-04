webiopi().ready(function() {
	webiopi().refreshGPIO(true);
});

function toggle_garage(button) {
	webiopi().callMacro("toggle_garage");	
}

function restart_pi(button) {
	webiopi().callMacro("restart_pi");
}
