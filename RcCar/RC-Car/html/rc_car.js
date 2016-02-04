webiopi().ready(function() {
	webiopi().refreshGPIO(true);
});

function top_left(button) {
	webiopi().callMacro("top_left");
}

function top_middle(button) {
	webiopi().callMacro("top_middle");
}

function top_right(button) {
	webiopi().callMacro("top_right");
}

function middle_left(button) {
	webiopi().callMacro("middle_left");
}

function middle_middle(button) {
	webiopi().callMacro("middle_middle");
}

function middle_right(button) {
	webiopi().callMacro("middle_right");
}

function bottom_left(button) {
	webiopi().callMacro("bottom_left");
}

function bottom_middle(button) {
	webiopi().callMacro("bottom_middle");
}

function bottom_right(button) {
	webiopi().callMacro("bottom_right");
}

function microphone(microphone) {
	
}

function lights(lights) {
	if (lights.checked) {
		webiopi().callMacro("lightsOn");
	} else {
		webiopi().callMacro("lightsOff");
	}
}

function restart_pi(button) {
	webiopi().callMacro("restart_pi");
}
