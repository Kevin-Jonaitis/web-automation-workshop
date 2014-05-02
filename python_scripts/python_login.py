import requests
url = 'http://rocky-brook-8124.herokuapp.com/signUpCheck'
payload = {"username" : "aNewUser",
			"password" : "hunter42"	
		};
		
r = requests.post(url, data=payload)
print r.text
