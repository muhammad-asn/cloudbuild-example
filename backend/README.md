# Flask Hello World

This is a simple Flask "Hello, World!" application with a unit test.

## Prerequisites

- Python 3.10.x
- `pip` package installer

## Installation

1. Clone the repository or download the source code.

2. Navigate to the project directory.

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Application
To run the Flask application, execute the following command:
```bash
python app.py
```

OR with docker
```bash
docker compose up -d --build
```

## Running Unit Tests with Coverage
This will run the unit tests defined in `tests/` folder and display the results in the terminal.
```bash
coverage run -m unittest test_app.py
coverage report
```