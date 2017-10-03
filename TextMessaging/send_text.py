from twilio.rest import Client

account_sid = "AC7bcaa216e439b9090a429a99c1ec4c2d"
auth_token = "985aa04fbc8158be7a08e87cdb53a389"

client = Client(account_sid, auth_token)

#message = client.api.account.messages.create(body = "This SMS is through my python code",
#                                     to = "+917977504651",
#                                     from_ = "+16303945970")

message = client.messages.create(body = "This SMS is through my python code",
                                             to = "+917977504651",
                                             from_ = "+16303945970")
print(message.sid)
