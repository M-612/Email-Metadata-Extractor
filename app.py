from flask import Flask, request, render_template, redirect, url_for
import email
import re

app = Flask(__name__)

def parse_email_metadata(file_content):
    msg = email.message_from_string(file_content)

    metadata = {
        'From': msg.get('From'),
        'To': msg.get('To'),
        'Date': msg.get('Date'),
        'Subject': msg.get('Subject'),
        'Message-ID': msg.get('Message-ID'),
        'In-Reply-To': msg.get('In-Reply-To'),
        'References': msg.get('References'),
        'Content-Type': msg.get('Content-Type'),
        'Return-Path': msg.get('Return-Path'),
        'Received-SPF': msg.get('Received-SPF'),
        'X-Received': msg.get('X-Received'),
        'ARC-Message-Signature': msg.get('ARC-Message-Signature'),
        'ARC-Authentication-Results': msg.get('ARC-Authentication-Results'),
        'Received': msg.get('Received'),
        'DKIM-Signature': msg.get('DKIM-Signature'),
        'Authentication-Results': msg.get('Authentication-Results'),
        'SPF': msg.get('SPF'),
        'DMARC': msg.get('DMARC'),
        'SMTP-Server-IP': None,
        'SMTP-Source': None,
        'Hashing-Algorithm': None,
        'Received-IP': None,
        'Timestamp': None,
    }

    for received in msg.get_all('Received', []):
        match = re.search(r'\bfrom\b.*?\b(\d{1,3}(?:\.\d{1,3}){3})\b', received)
        if match:
            metadata['SMTP-Server-IP'] = match.group(1)
        match = re.search(r'\bwith\b\s+(\w+)', received)
        if match:
            metadata['SMTP-Source'] = match.group(1)
        match = re.search(r'\bby\b.*?\b(\d{1,3}(?:\.\d{1,3}){3})\b', received)
        if match:
            metadata['Received-IP'] = match.group(1)
        match = re.search(r';\s+(.*)', received)
        if match:
            metadata['Timestamp'] = match.group(1)

    if metadata['DKIM-Signature']:
        match = re.search(r'(\bsha\S+)', metadata['DKIM-Signature'])
        if match:
            metadata['Hashing-Algorithm'] = match.group(1)

    return metadata

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'email_file' in request.files and request.files['email_file'].filename:
            file = request.files['email_file']
            file_content = file.read().decode('utf-8')
            metadata = parse_email_metadata(file_content)
            return render_template('results.html', metadata=metadata)
        elif request.form['email_metadata']:
            file_content = request.form['email_metadata']
            metadata = parse_email_metadata(file_content)
            return render_template('results.html', metadata=metadata)
        else:
            return "Please upload a file or paste metadata!"
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
