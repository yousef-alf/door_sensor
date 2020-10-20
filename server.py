from http import *
from gpio import *
from time import *

#while True:
#count=0

	

	
def onRouteTest(url, response):
	print("Request for /test")
	response.send(count)
	

def onRouteWildcard(url, response):
	print("Request for " + url)
	response.send("wildcard")

def main():
	pinMode(1, IN)
	pinMode(0, OUT)
	count=0
	while True:
		val=digitalRead(1);
		if val == HIGH:
			customWrite(0,"1,0");
			count = count+1
			print(count)
			delay(15000)
		elif val == LOW:
			customWrite(0, "0,0");
			

		def onRouteRoot(url, response):
			print("Request for /");
			response.send(count)
		HTTPServer.route("/",onRouteRoot)
		
	
		HTTPServer.route("/*", onRouteWildcard)
	
		# start server on port 80
		print(HTTPServer.start(80))
		
	
		# don't let it finish
	#	while True:
		#sleep(3600)

if __name__ == "__main__":
	main()
