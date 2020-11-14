## Server 200 status checker
for os: all

Script cheks your server status once a minute. In a case status != 200 you will get panic sms message to your phone


### Installing

```
git clone https://github.com/iamdianahello/py101_request
pip3 install twilio
pip3 install python-dotenv
```


### Usage
create .env file with your twillio params and numbers:
TWILIO_ACCOUNT_SID=
TWILIO_AUTH_TOKEN=
NUMBER_FROM=
NUMBER_TO=

then run spam.py
