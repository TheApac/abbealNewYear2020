from flask import Flask, Response, request, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

answer = 'Paomibzi'

subject = "RGFucyB1bmUgcGV0aXRlIHJ1Y2hlIGTigJlhYmVpbGxlcywgdW4gZ3JvdXBlIGRlIHZvbG9udGFpcmVzIHZvdWxhaXQgcHLDqXBhcmVyIGxlIHLDqXZlaWxsb24gZGUgbm/Dq2wKQ2VwZW5kYW50LCBsZSBtYXRpbiBkdSAyNSBkw6ljZW1icmUsIGFsb3JzIHF14oCZZWxsZXMgYWxsYWllbnQgY2hlcmNoZXIgbGVzIGNhZGVhdXgsIGVsbGVzIHNlIHJlbmRpcmVudCBjb21wdGUgcXXigJl1bmUgY29ubmFzc2UgbWFsb3RydSBhdmFpdCBzYWNjYWfDqSB0b3VzIGxlcyBjb2xpcy4gTWFpcywgZWxsZXMgc2UgcmVuZGlyZW50IMOpZ2FsZW1lbnQgY29tcHRlIHF1ZSBs4oCZdW4gZGVzIGNvbGlzIGF2YWl0IGRpc3BhcnUsIHByb2JhYmxlbWVudCBjZWx1aSBkdSByZXNwb25zYWJsZSBkZSBs4oCZb3DDqXJhdGlvbiBzYWJvdGFnZS4KSGV1cmV1c2VtZW50LCBjaGFxdWUgY29saXMgw6l0YWl0IG51bcOpcm90w6kgZXQgaWwgw6l0YWl0IGRvbmMgcG9zc2libGUgZGUgc2F2b2lyIHF1aSDDqXRhaXQgw6AgbOKAmW9yaWdpbmUgZGUgdG91dCBjZWNpLgpMYSBsaXN0ZSBxdeKAmWVsbGVzIGTDqXRpZW5uZW50IGZvbmN0aW9ubmUgY29tbWUgc3VpdCA6IGxlIG51bcOpcm8gZHUgY29saXMsIHN1aXZpIGR1IG5vbSBkdSBkZXN0aW5hdGFpcmUsIHPDqXBhcsOpcyBwYXIg4oCYOuKAmQoKUGFyIGV4ZW1wbGUgOgo3Mzg0MDIwNDI5NDk6TWF5YQozODM5ODA5MDIwMDQ6TcOpbGluYQo5NTk3Mzc0Mzk5MzE6TWluZHkKClZvdXMgYXZleiDDqWdhbGVtZW50IMOgIHZvdHJlIGRpc3Bvc2l0aW9uIGxhIGxpc3RlIGR1IHNjYW4gZWZmZWN0dcOpIGVuIHbDqXJpZmlhbnQgbGVzIGNvbGlzIGxlIG1hdGluIG3Dqm1lCgpQYXIgZXhlbXBsZSA6CjM4Mzk4MDkwMjAwNAo5NTk3Mzc0Mzk5MzEKCkFwcsOocyBhdm9pciB0b3V0IHNjYW5uw6ksIGVsbGVzIHNlIHJlbmRpcmVudCBjb21wdGUgcXXigJlpbCBtYW5xdWFpdCB1biBudW3DqXJvLCBj4oCZZXN0IMOgIGNlIG1vbWVudCBxdeKAmWVsbGVzIHNlIHNvbnQgYXBlcsOndWVzIHF14oCZZWxsZXMgcG91cnJhaWVudCByZXRyb3V2ZXIgbGUgY291cGFibGUgZXQgbGUgZmFpcmUgYWNoZXRlciBkZSBub3V2ZWF1eCBjYWRlYXV4IHBvdXIgdG91dCBsZSBtb25kZS4gUG91cnJlei12b3VzIGxlcyBhaWRlciDDoCByZXRyb3V2ZXIgc29uIG5vbSwgZW4gdm91cyBhcHB1eWFudCBzdXIgbGVzIGZpY2hpZXJzIGZvdXJuaXMgPw=="


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/exercise')
def get_exercise():
    return Response('{"subject":"'+subject+'"}', status=200, mimetype='application/json')


@app.route('/file1')
def get_file1():
    return send_file('fileFull.txt', attachment_filename='fullList.txt')


@app.route('/file2')
def get_file2():
    return send_file('fileNumbers.txt', attachment_filename='listWithNumbers.txt')


@app.route('/answer', methods=['POST'])
def submit_answer():
    data = request.get_json()
    if data['answer'] == answer:
        return Response('{"valid":true}', status=200, mimetype='application/json')
    else:
        return Response('{"valid":false}', status=418, mimetype='application/json')


if __name__ == '__main__':
    app.run()
