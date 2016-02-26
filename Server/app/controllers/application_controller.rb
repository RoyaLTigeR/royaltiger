class ApplicationController < ActionController::Base
	$global_ip = '173.58.125.83'

	# Prevent CSRF attacks by raising an exception.
	# For APIs, you may want to use :null_session instead.
	USERS = { 
		'tiger' => '1337', 
		'emma' => '3895' ,
		'amy' => 'liu' ,
	}

 	before_filter :authenticate

	protected
	def authenticate
		authenticate_or_request_with_http_basic do |username, password|
			return true if USERS.has_key?(username) && USERS[username] == password
		end
	end
end
