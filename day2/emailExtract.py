# import datetime
# import json
# import eml_parser
#
#
# def json_serial(obj):
#     if isinstance(obj, datetime.datetime):
#         serial = obj.isoformat()
#         return serial
#
#
# with open('Your Samsung order #SA101990545 shipped today.eml', 'rb') as fhdl:
#     raw_email = fhdl.read()
#
# ep = eml_parser.EmlParser()
# parsed_eml = ep.decode_email_bytes(raw_email)
#
# print(json.dumps(parsed_eml, default=json_serial))

import email
from email import policy
from email.parser import BytesParser
import html2text
import json
import datetime
print("Ajit")

filepath = 'Your Samsung order #SA101990545 shipped today.eml'
def json_serial(obj):
    if isinstance(obj, datetime.datetime):
        serial = obj.isoformat()
        return serial
with open(filepath) as email_file:
    email_message = email.message_from_file(email_file)
#print(email_message.get_payload())
#print(email_message.is_multipart())
print(json.dumps(email_message.get_payload(), default=json_serial))
# if email_message.is_multipart():
#     for part in email_message.walk():
#         #print(part.is_multipart())
#         #print(part.get_content_type())
#         #print()
#         message = str(part.get_payload(decode=True))
#         plain_message = html2text.html2text(message)
#         print(plain_message)
#         print()