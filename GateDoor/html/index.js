webiopi().ready(function() {
	webiopi().refreshGPIO(true);
});

function toggle_gate(button) {
	webiopi().callMacro("toggle_gate");	
}

function restart_pi(button) {
	webiopi().callMacro("restart_pi");
}
