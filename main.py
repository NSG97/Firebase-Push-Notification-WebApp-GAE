from flask import Flask, render_template, request
from pyfcm.fcm import FCMNotification

push_service = FCMNotification(api_key="AIzaSyDfv98w0EydT4wvpGQYy2tcGyOPs6EYcTE", env='app_engine')

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def main():
	return render_template('main.html')

@app.route("/sent.php",methods=['POST'])
def sent():
	_notification = request.form['NotificationText']
	result = push_service.notify_topic_subscribers(topic_name="ALL",message_body=_notification)
	return render_template('sent.php',NotificationText=_notification)

if(__name__ == "__main__"):
	app.run()