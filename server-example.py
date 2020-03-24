from http.server import BaseHTTPRequestHandler
import logging
import random

logger = logging.getLogger("Server")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('Server.log')
formatter = logging.Formatter(
    '%(asctime)s : %(levelname)s : %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        message = 'Hello! You are visiting a web server built in Python!'

        if self.path == '/random-number':
            random_number = random.SystemRandom().randint(1, 10)
            message += '\n\n\nRandom Number:\n    ' + str(random_number)
            logger.info('random number: ' + str(random_number))

        self.send_response(200)
        self.send_header('Content-Type',
                         'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(message.encode('utf-8'))


if __name__ == '__main__':
    from http.server import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    logger.info("Started Server")
    server.serve_forever()
