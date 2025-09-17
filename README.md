# Speedtest App

This project is a simple web application that performs an internet speed test using the Speedtest library. It provides a user-friendly interface to display download speed, upload speed, and ping.

## Project Structure

```
speedtest-app
├── app.py               # Main application file
├── requirements.txt     # Project dependencies
├── static
│   └── style.css        # CSS styles for the frontend
├── templates
│   └── index.html       # HTML template for the frontend
└── README.md            # Project documentation
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone <repository-url>
   cd speedtest-app
   ```

2. **Install dependencies**:
   It is recommended to use a virtual environment. You can create one using:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
   Then install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```
   python app.py
   ```

4. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000` to view the speed test results.

## Usage

Once the application is running, you can click the button on the webpage to initiate the speed test. The results will be displayed on the same page, showing the download speed, upload speed, and ping.

## License

This project is licensed under the MIT License.