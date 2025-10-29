# Weather App

A minimalist weather application built with Flask that shows current weather conditions for any city.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setup

1. Clone the repository
```bash
git clone <your-repository-url>
cd weather-app-flask
```

2. Create a virtual environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Set up OpenWeather API
- Sign up at [OpenWeather](https://openweathermap.org/api)
- Get your API key
- Create a `.env` file in the project root:
```bash
OPENWEATHER_API_KEY=your_api_key_here
```

## Running the App

1. Make sure your virtual environment is activated
2. Run the Flask application:
```bash
python app.py
```
3. Open your browser and go to: `http://localhost:5001`

## Features

- Current temperature
- Weather conditions
- Humidity levels
- Sunrise and sunset times
- "Feels like" temperature
- Support for any city worldwide

## Project Structure
```
weather-app-flask/
├── static/
│   └── style.css
├── templates/
│   └── index.html
├── .env
├── .gitignore
├── app.py
├── Procfile
└── requirements.txt
```

## Troubleshooting

- If you get a port error, modify the port number in `app.py`
- If weather data isn't loading, verify your API key in the `.env` file
- Make sure all required packages are installed using `pip install -r requirements.txt`

## License

This project is licensed under the MIT License.
