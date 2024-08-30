from flask import Flask, jsonify
from twilio.rest import Client

app = Flask(__name__)

# Twilio Account SID and Auth Token
account_sid = 'AC192171e5ee4384039b78ca249effcfd2'
auth_token = 'fb7fd56e6abd964a75a4662865e6dbda'
client = Client(account_sid, auth_token)
recipient_number = '+919887551644'

@app.route('/send_alert', methods=['POST'])
def send_alert():
    try:
        message = client.messages.create(
            from_='+12058596840',
            body='ALERT! Your friend needs help, My location is https://maps.app.goo.gl/Tusquv3e8TNw96By9',
            to=recipient_number
        )

        return jsonify({'message_sid': message.sid}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/make_call', methods=['POST'])
def make_call():
    try:
        # Make a call using Twilio to the specified phone number
        call = client.calls.create(
            url='http://demo.twilio.com/docs/voice.xml',
            to=recipient_number,
            from_='+12058596840'
        )

        # Return the SID of the created call
        return jsonify({'call_sid': call.sid}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)