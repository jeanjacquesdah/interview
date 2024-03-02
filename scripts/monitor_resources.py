

#Replace 'your_slack_token', '#your_channel', 'your_email@gmail.com', 'recipient_email@example.com', and 'your_email_password' 
#with your actual Slack token, Slack channel, email addresses, and email password.

import psutil
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Server details
cpu_threshold = 80  # Adjust as needed (%)
memory_threshold = 80  # Adjust as needed (%)
disk_threshold = 80  # Adjust as needed (%)

# Slack details
slack_token = 'your_slack_token'
slack_channel = '#your_channel'

# Email details
email_sender = 'your_email@gmail.com'
email_receiver = 'recipient_email@example.com'
email_subject = 'Server Resource Alert'

def monitor_resources():
    # Get CPU, memory, and disk usage
    cpu_usage = psutil.cpu_percent()
    memory_usage = psutil.virtual_memory().percent
    disk_usage = psutil.disk_usage('/').percent

    # Check CPU usage
    if cpu_usage > cpu_threshold:
        send_alert(f'High CPU Usage Alert! Current Usage: {cpu_usage}%')

    # Check memory usage
    if memory_usage > memory_threshold:
        send_alert(f'High Memory Usage Alert! Current Usage: {memory_usage}%')

    # Check disk usage
    if disk_usage > disk_threshold:
        send_alert(f'High Disk Usage Alert! Current Usage: {disk_usage}%')

def send_alert(message):
    try:
        # Send Slack alert
        slack_client = WebClient(token=slack_token)
        slack_client.chat_postMessage(channel=slack_channel, text=message)

    except SlackApiError as e:
        print(f'Slack API Error: {e.response["error"]}')

    try:
        # Send email alert
        email_body = f'Server Resource Alert:\n\n{message}'
        send_email(email_subject, email_body)

    except Exception as e:
        print(f'Email Sending Error: {e}')

def send_email(subject, body):
    # Email server details
    email_server = 'smtp.gmail.com'
    email_port = 587
    email_username = 'your_email@gmail.com'
    email_password = 'your_email_password'

    # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject

    # Attach the body to the email
    msg.attach(MIMEText(body, 'plain'))

    # Setup the email server connection
    server = smtplib.SMTP(email_server, email_port)
    server.starttls()
    server.login(email_username, email_password)

    # Send the email
    server.sendmail(email_sender, email_receiver, msg.as_string())

    # Close the server connection
    server.quit()

if __name__ == "__main__":
    monitor_resources()
