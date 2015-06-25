from datadog import statsd as dogstats
from flask import Flask, request

app = Flask(__name__)
datadog.initialize(statsd_host='localhost', statsd_port=8126)


@app.route('/message', methods=['POST'])
def message():
    channel = request.form.get('channel_name')
    if channel:
        dogstats.increment('slack.channels.%s' % channel)

if __name__ == '__main__':
    app.run()
