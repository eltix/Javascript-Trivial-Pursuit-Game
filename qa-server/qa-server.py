#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json

PORT_NUMBER = 8081

# This class will handles any incoming request from
# the browser
class MyHandler(BaseHTTPRequestHandler):
    # def end_headers(self):
    #     self.send_header("Access-Control-Allow-Origin", "*")
    #     SimpleHTTPRequestHandler.end_headers(self)

    def do_OPTIONS(self):
        self.send_response(200, "ok")
        self.send_header("Access-Control-Allow-Credentials", "true")
        self.send_header("Access-Control-Allow-Origin", "http://localhost:8888")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header(
            "Access-Control-Allow-Headers", "X-Requested-With, Content-type"
        )

    # Handler for the GET requests
    def do_GET(self, *args, **kwargs):
        # test_response = {
        #     "response_code": 0,
        #     "results": [
        #         {
        #             "category": "History",
        #             "type": "multiple",
        #             "difficulty": "medium",
        #             "question": "In what year did Kentucky become the 15th state to join the union?",
        #             "correct_answer": "1792",
        #             "incorrect_answers": ["1782", "1798", "1788"],
        #         }
        #     ],
        # }
        print(args, flush=True)
        print(kwargs, flush=True)
        qas = json.load(open("qa.json"))
        test_response = qas[0]
        self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.send_header("Access-Control-Allow-Credentials", "true")
        self.send_header("Access-Control-Allow-Origin", "http://0.0.0.0:8080")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header(
            "Access-Control-Allow-Headers", "X-Requested-With, Content-type"
        )
        self.end_headers()
        # self._set_headers()
        self.wfile.write(json.dumps(test_response).encode())
        # self.wfile.close()
        # self.send_response(200)
        # self.send_header("Content-type", "text/html")
        # self.end_headers()
        # # Send the html message
        # self.wfile.write("Hello World !")
        return


try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(("", PORT_NUMBER), MyHandler)
    print("Started httpserver on port ", PORT_NUMBER)

    # Wait forever for incoming htto requests
    server.serve_forever()

except KeyboardInterrupt:
    print("^C received, shutting down the web server")
    server.socket.close()
