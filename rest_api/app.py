from flask import Flask, jsonify, request


app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/email', methods=('POST',))
def mock_save_email():
    emails = []
    for email in request.json:
        emails.append(email.get('email'))
    save_emails_to_s3(emails)
    return jsonify({'status': 'success', 'emailsSaved': emails})

# # Example event from SendGrid
# [
#    {
#       "email":"example@test.com",
#       "timestamp":1513299569,
#       "smtp-id":"<14c5d75ce93.dfd.64b469@ismtpd-555>",
#       "event":"open",
#       "category":"cat facts",
#       "sg_event_id":"FOTFFO0ecsBE-zxFXfs6WA==",
#       "sg_message_id":"14c5d75ce93.dfd.64b469.filter0001.16648.5515E0B88.0",
#       "useragent":"Mozilla/4.0 (compatible; MSIE 6.1; Windows XP; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
#       "ip":"255.255.255.255"
#    }
# ]

def save_emails_to_s3(emails):
    pass

## Error route to test out deploy rollback if alarms start firing
## Deploy new version then hit this endpoint to test rollback
@app.route('/error')
def throw_error():
    raise ExpectedError

class ExpectedError(Exception):
    pass
