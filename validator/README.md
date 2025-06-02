# Flask Card Validator

This project is a simple Flask application that validates credit card numbers and identifies their types (e.g., Visa, MasterCard, Amex) using regular expressions. It demonstrates good practices in object-oriented programming and provides a user-friendly interface for inputting credit card numbers.

## Project Structure

```
flask-card-validator
├── app
│   ├── __init__.py
│   ├── card_validator.py
│   ├── routes.py
│   └── templates
│       └── index.html
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd flask-card-validator
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```
   flask run
   ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

3. Enter a credit card number in the input field and submit the form to see the identified card type.

## Features

- Validates credit card numbers using regular expressions.
- Identifies card types such as Visa, MasterCard, and American Express.
- User-friendly interface for easy input and result display.

## Contributing

Feel free to submit issues or pull requests if you have suggestions for improvements or new features. 

## License

This project is licensed under the MIT License. See the LICENSE file for details.