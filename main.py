from flask import Flask, render_template, request
from pyfcm.fcm import FCMNotification

push_service = FCMNotification(api_key="AIzaSyDfv98w0EydT4wvpGQYy2tcGyOPs6EYcTE", env='app_engine')

app = Flask(__name__)

@app.route("/", methods=['GET','POST'])
def main():
	# return the rendered main.html
	return render_template('main.html')

@app.route("/sent.html",methods=['POST'])
def sent():
	# Get Notification from the form
	_notification = request.form['NotificationText']

	# Notification is sent to all devices subscribed to topic "ALL" using pyfcm
	result = push_service.notify_topic_subscribers(topic_name="ALL",message_body=_notification)

	# return the rendered sent.html with the variable _notification
	return render_template('sent.html',NotificationText=_notification)

if(__name__ == "__main__"):
	app.run()