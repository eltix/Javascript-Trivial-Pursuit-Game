#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from random import choice

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

    qas = json.load(open("qa.json"))
    num_questions = len(qas)
    remaining_questions = list(range(num_questions))

    # Handler for the GET requests
    def do_GET(self, *args, **kwargs):

        print(args, flush=True)
        print(kwargs, flush=True)
        print(f"asked_questions: {self.remaining_questions}", flush=True)

        question_id = choice(self.remaining_questions)
        test_response = self.qas[question_id]
        self.remaining_questions.remove(question_id)
        self.send_response(200)
        self.send_header("Content-type", "text/xml")
        self.send_header("Access-Control-Allow-Credentials", "true")
        self.send_header("Access-Control-Allow-Origin", "http://0.0.0.0:8080")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header(
            "Access-Control-Allow-Headers", "X-Requested-With, Content-type"
        )
        self.end_headers()
        self.wfile.write(json.dumps(test_response).encode())
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
