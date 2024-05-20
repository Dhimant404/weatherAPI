# Real-time Weather Forecast API

This project provides a RESTful API that offers real-time weather forecasts based on geographical locations. The API allows users to manage locations and retrieve current and historical weather data. Built using FastAPI, the application leverages MongoDB for data storage and Redis for caching, all containerized using Docker.

## Features

- **Location Management**: Add, retrieve, update, and delete locations.
- **Weather Forecast**: Fetch real-time weather data for specified locations.
- **Weather History**: Retrieve historical weather data summaries.
- **Caching**: Reduce external API calls using Redis.
- **Rate Limiting**: Prevent abuse of the API.
- **Logging**: Track API requests and interactions with external services.

## Tech Stack

- **Backend Framework**: FastAPI
- **Database**: MongoDB
- **Cache**: Redis
- **Containerization**: Docker

## Setup Instructions

### Prerequisites

- **Conda**: Ensure you have Conda installed. You can download and install it from [here](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html).
- **Docker**: Ensure you have Docker installed. You can download and install it from [here](https://docs.docker.com/get-docker/).

### Step-by-Step Guide

1. **Clone the Repository**

    ```sh
    git clone https://github.com/your-username/weather-api.git
    cd weather-api
    ```

2. **Create and Activate Conda Environment**

    ```sh
    conda create --name weather-api-env --file requirements.txt
    conda activate weather-api-env
    ```

3. **Set Up Environment Variables**

    Create a `.env` file in the root directory of the project and add the following environment variables:

    ```env
    MONGODB_URL=mongodb://mongodb:27017/
    REDIS_HOST=redis
    REDIS_PORT=6379
    WEATHER_API_KEY=your_weather_api_key
    ```

4. **Run the Application Using Docker Compose**

    ```sh
    docker-compose up --build
    ```

5. **Access the API**

    The API will be accessible at `http://localhost:8000`.

## API Endpoints

- **Location Management**
  - `GET /locations`: Retrieve all locations.
  - `POST /locations`: Add a new location.
  - `GET /locations/{location_id}`: Retrieve a specific location by ID.
  - `PUT /locations/{location_id}`: Update a specific location by ID.
  - `DELETE /locations/{location_id}`: Delete a specific location by ID.

- **Weather Forecast**
  - `GET /weather/{location_id}`: Retrieve real-time weather forecast for a specific location.

- **Weather History**
  - `GET /history/{location_id}?days={7|15|30}`: Retrieve historical weather data summary for the past specified days.


## Contact

For any queries, please contact [dhimat16@gmail.com].