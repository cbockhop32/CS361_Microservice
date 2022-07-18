from http.server import BaseHTTPRequestHandler, HTTPServer
import socketserver
import json
import cgi
from typing import final
import simplejson
from bs4 import BeautifulSoup
import requests


class Server(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        
    def do_HEAD(self):
        self._set_headers()
        
    # GET sends back a Hello world message
    def do_GET(self):
        self._set_headers()
        self.wfile.write(json.dumps({'hello': 'world', 'received': 'ok'}).encode('utf-8'))  
        
    # POST echoes the message adding a JSON field
    def do_POST(self):
        self._set_headers()
        self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        self.send_response(200)
        self.end_headers()

        # This is the url that was received from the POST request
        received_data = simplejson.loads(self.data_string)
   


        # Wikiscraping
        html_text = requests.get(received_data['url']).text

        soup = BeautifulSoup(html_text, 'lxml')

        external_link = soup.find('span', id="External_links").parent.find_next_sibling('ul').find('a', class_='external text')



        # Packaging into an object
        final_data = {'url': external_link['href']}
        # Converting object to JSON string
        json_string = json.dumps(final_data)
        # Writing JSON string
        self.wfile.write(json_string.encode('utf-8'))

        print("Response Sent To Client")

        return


      
        
def run(server_class=HTTPServer, handler_class=Server, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    
    print ('Starting Server On Port: %d...' % port)
    httpd.serve_forever()
    
if __name__ == "__main__":
    from sys import argv
    
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()