# Email-Metadata-Extractor
This is a Flask-based web application that extracts metadata from `.eml` files or pasted email metadata. The application parses various headers such as `From`, `To`, `Date`, `Subject`, and more, to help users analyse email metadata efficiently.

##Features
- Upload `.eml` File: Users can upload an `.eml` file to extract and display its metadata.
  
-Paste Email Metadata: Users can paste raw email metadata directly into the text area provided on the web page.

-Header Parsing: The application extracts common email headers including but not limited to `From`, `To`, `Date`, `Subject`, `Message-ID`, `Received`, `DKIM-Signature`, and others.

-Metadata Details: Extracts and displays additional details like the SMTP server IP, source, received IP, timestamp, and hashing algorithm used in DKIM signatures.

##Installation

###Clone the repository:
git clone https://github.com/M-612/Email-Metadata-Extractor.git
cd Email-Metadata-Extractor

##Usage

### Running the Application

1. Start the Flask Development Server:
   Ensure you are in the project directory and that your virtual environment is activated:

   bash
   python app.py

   This will start the Flask development server on http://127.0.0.1:5000.

2. Access the Application:

   Open your web browser and navigate to http://127.0.0.1:5000 to view the application.

3. Using the Web Interface

   Upload a .eml File: On the home page, click the "Choose File" button to select a .eml file from your local system.
                    Click the "Upload" button to submit the file.
                    The application will parse the email and display the extracted metadata.

   Paste Email Metadata:Alternatively, you can paste raw email metadata into the provided text area.
                     Click the "Submit" button to process the metadata and view the results.

