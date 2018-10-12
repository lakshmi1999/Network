#uploading a webpage
from http.server import HTTPServer,BaseHTTPRequestHandler
class Serv(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path==(r'/'):
			self.path=(r'C:/webser\upload.html')
		try:
			file_to_open=open(self.path[2:]).read()
			self.send_response(200)
		except:
			file_to_open="FILE NOT FOUND,TRY AGAIN"	
			self.send_response(404)
		self.end_headers()
		self.wfile.write(bytes(file_to_open,'utf-8'))
		
		
httpd=HTTPServer(('127.0.0.1',8000),Serv)
httpd.serve_forever()
