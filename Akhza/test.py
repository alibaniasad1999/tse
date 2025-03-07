from kavenegar import *
api = KavenegarAPI('6B3372454C4146334137554C47467332626C79397268474A71367144705171424C697A5A41707976506C593D')
params = { 'sender' : '2000500666', 'receptor': '09912147276', 'message' :'.وب سرویس پیام کوتاه کاوه نگار' }
response = api.sms_send( params)