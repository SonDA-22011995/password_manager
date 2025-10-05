🔐 Password Manager Application
📋 Overview

This Password Manager is a simple desktop application built with Python and Tkinter that allows users to securely store, update, and manage their login credentials (website, username, and password). All data is stored locally in a data.csv file.

⚙️ Features
1. ➕ Add New Credentials

Enter the following information in the input fields:

Website

Username

Password

Click the Add button to save the data into the data.csv file.

If a record with the same website and username already exists, the app will prevent adding a duplicate entry and will only allow updating the password instead.

2. 🔁 Update Existing Password

To change an existing password:

Enter the Website, Username, and the New Password.

Click Update to modify the password for that specific user in data.csv.

3. 🔍 Search User Information

Enter a Website name and click Find.

A child window will appear displaying all usernames associated with that website.

Select the desired user and click Submit to confirm your selection.

4. ⚡ Generate Strong Password

Click Generate Password to automatically create a secure, random password.

The generated password will appear in the password input field and can be used immediately.

5. 📋 Copy to Clipboard

Click Copy user name/Password to instantly copy the respective field to the system clipboard.

This makes it easy to paste credentials into login forms without displaying them in plain text.

💾 Data Storage

All credentials are stored in a CSV file named data.csv located in the application directory.

The file structure:

Website,Username,Password
example.com,john_doe,Abc123!@#

🧩 Technologies Used

Python 3.12

Tkinter (for GUI)

Pandas 2.3.2 (for CSV data handling)

pyperclip 1.11.0 (for clipboard operations)

random & string (for password generation)

🚀 `How to Run

Clone or download the project.

Set Up Virtual Environment and Install Dependencies

Create a virtual environment (recommended):

python -m venv venv


Activate the virtual environment

On Windows:

venv\Scripts\activate


On macOS / Linux:

source venv/bin/activate


Install required libraries from requirements.txt:

pip install -r requirements.txt

Run the main file:

python main.py


Start managing your passwords easily and securely!

🧑‍💻 Author

Developed by Sonda-daoansonhvtc@gmail.com — a simple yet effective password management solution built with Python ❤️`