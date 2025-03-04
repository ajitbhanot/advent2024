import email
import json
import re

# Function to decode the email subject and other headers
def decode_header_value(value):
    decoded_value, encoding = email.header.decode_header(value)[0]
    if isinstance(decoded_value, bytes):
        return decoded_value.decode(encoding if encoding else "utf-8")
    return decoded_value

# Function to extract URLs from a text body
def extract_urls(text):
    # Regular expression to match URLs
    url_pattern = r'https?://[^\s]+'
    urls = re.findall(url_pattern, text)
    return urls

# Function to parse the .eml file and extract relevant information
def parse_eml(file_path):
    with open(file_path, 'r') as f:
        msg = email.message_from_file(f)

    email_data = {}

    # Extract subject
    email_data['subject'] = decode_header_value(msg["Subject"])

    # Extract sender
    email_data['from'] = decode_header_value(msg.get("From"))

    # Extract recipient(s)
    email_data['to'] = decode_header_value(msg.get("To"))

    # Extract date
    email_data['date'] = msg.get("Date")

    # Initialize list for extracted URLs
    email_data['urls'] = []

    # Process the email body
    if msg.is_multipart():
        for part in msg.walk():
            content_type = part.get_content_type()
            content_disposition = str(part.get("Content-Disposition"))

            # Extract the plain text or HTML part of the email
            if content_type == "text/plain" and "attachment" not in content_disposition:
                body = part.get_payload(decode=True).decode()
                email_data['urls'] = extract_urls(body)
            elif content_type == "text/html" and "attachment" not in content_disposition:
                body = part.get_payload(decode=True).decode()
                email_data['urls'] = extract_urls(body)
    else:
        # If the email is not multipart, extract body from the email itself
        body = msg.get_payload(decode=True).decode()
        email_data['urls'] = extract_urls(body)

    return email_data

# File path to the .eml file
file_path = 'Your Samsung order #SA101990545 shipped today.eml'

# Parse the .eml file and extract data
email_json_data = parse_eml(file_path)

# Convert the email data to JSON format
email_json = json.dumps(email_json_data, indent=4)

# Output the email data in JSON format
print(email_json)
