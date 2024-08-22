# Email-Metadata-Extractor
This is a Flask-based web application that extracts metadata from `.eml` files or pasted email metadata. The application parses various headers such as `From`, `To`, `Date`, `Subject`, and more, to help users analyse email metadata efficiently.

Features
- Upload `.eml` File: Users can upload an `.eml` file to extract and display its metadata.
-Paste Email Metadata: Users can paste raw email metadata directly into the text area provided on the web page.
-Header Parsing: The application extracts common email headers including but not limited to `From`, `To`, `Date`, `Subject`, `Message-ID`, `Received`, `DKIM-Signature`, and others.
-Metadata Details: Extracts and displays additional details like the SMTP server IP, source, received IP, timestamp, and hashing algorithm used in DKIM signatures.

Installation
Clone the repository:
git clone https://github.com/M-612/Email-Metadata-Extractor.git
cd Email-Metadata-Extractor

