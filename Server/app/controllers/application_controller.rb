class ApplicationController < ActionController::Base
	# Prevent CSRF attacks by raising an exception.
	# For APIs, you may want to use :null_session instead.
	
	#http_basic_authenticate_with name: "tiger", password: "1337", :except => []

	USERS = { 
		'tiger' => '1337', 
		'emma' => '3895' ,
		'amy' => 'liu'
	}

 before_filter :authenticate

  protected

  def authenticate
    authenticate_or_request_with_http_basic do |username, password|
      return true if username == "tiger" && password == "1337"
      return true if username == "emma" && password == "3895"
    end
  end
end
