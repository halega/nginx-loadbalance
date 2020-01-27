import os

from flask import Flask, request

app = Flask(__name__)

app_id = os.environ['APP_ID']

@app.route('/')
def hello():
    client_cert_dn = request.headers.get('X-SSL-Client-DN')
    html = '<!DOCTYPE html>\n'
    html += '<html>\n'
    html += '<head><title>Lab: Nginx with Docker</title></head>\n'
    html += '<body>\n'
    html += '<p>Hello! I Am Backend{}.</p>\n'.format(app_id)
    html += '<p>Client certificate DN: {}</p>\n'.format(client_cert_dn)
    html += '</body></html>'
    return html