# Weather Data Pipeline

A modern data engineering project that collects, processes, and analyzes weather data from the German Weather Service (DWD) using AWS Free Tier services and modern data engineering practices.

![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)

## 🌟 Features

- Automated weather data collection from DWD API
- Scalable data processing pipeline
- AWS Free Tier cloud integration (S3, Lambda)
- Local development environment with Docker
- Data quality checks and monitoring
- Interactive data visualizations


## 🏗️ Architecture

```plaintext
[Data Sources] → [Collection] → [Processing] → [Storage] → [Analysis]
     DWD API  →   Lambda    →   Python    →    S3     →  Notebooks


🛠️ Tech Stack

Data Collection: Python, AWS Lambda
Processing: Pandas, NumPy
Storage: AWS S3, PostgreSQL
Infrastructure: Docker, Terraform
Development: FastAPI, pytest
Visualization: Streamlit, Plotly


🚀 Quick Start

Clone the repository

git clone https://github.com/yourusername/weather-pipeline.git
cd weather-pipeline


Set up the environment

python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt


Start local services

docker-compose up -d


Run the collector

python src/main.py

📁 Project Structure
weather-pipeline/
├── src/               # Source code
├── infrastructure/    # IaC and Docker files
├── tests/            # Test suite
├── notebooks/        # Jupyter notebooks
└── docs/             # Documentation

📊 Sample Data
The pipeline collects the following weather metrics:

Temperature
Precipitation
Wind speed
Humidity
Air pressure

🔧 Configuration
Create a .env file in the root directory:
DWD_API_URL=https://api.dwd.de/
DB_CONNECTION=postgresql://user:password@localhost:5432/weather_db

🧪 Testing
Run the test suite:
pytest

📈 Monitoring
Access the monitoring dashboard:

Local Grafana: http://localhost:3000
API Documentation: http://localhost:8000/docs


🤝 Contributing

Fork the repository
Create a feature branch
Commit your changes
Push to the branch
Open a Pull Request

German Weather Service (DWD) for providing the data
Open-source community for tools and libraries


📫 Contact

Frederic Meyer
GitHub: @iamfmeyer
LinkedIn: https://www.linkedin.com/in/frederic-meyer-89b154b4/


🗺️ Roadmap

 Add more data sources
 Implement real-time processing
 Enhance visualization dashboard
 Add machine learning predictions
