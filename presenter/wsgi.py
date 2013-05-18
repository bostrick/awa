
#import sys
#sys.path.append("..")

import presenter
application = presenter.main(0)

def application2(environ, start_response):

    status = '200 OK'
    output = 'Hello World!'

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]

