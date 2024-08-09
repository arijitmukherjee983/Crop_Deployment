# Crop Recommendation System

## Overview

The Crop Recommendation System is an advanced web-based platform designed to assist farmers and agricultural stakeholders by providing personalized crop recommendations based on soil and climate data. The system aims to optimize crop yields and promote sustainable farming practices. Users can input soil parameters (e.g., nitrogen, phosphorus, potassium, pH) and climate conditions (e.g., temperature, rainfall) to receive tailored crop suggestions. The platform also features a feedback mechanism for continuous improvement and provides contact information for agricultural experts.

## Features

- **Personalized Crop Recommendations**: Input soil and climate data to receive tailored crop suggestions.
- **Feedback Mechanism**: Users can provide feedback to help improve the system.
- **Expert Contact Information**: Contact details for agricultural experts are available for user support.

## Project Structure

- `index.html`: The main landing page of the application.
- `about.html`: Contains information about the project and its goals.
- `contact.html`: Includes contact details or a form for reaching out to agricultural experts.
- `static/img/`: Directory for static images.
  - `img.jpeg`: An image(farmland) used in the application.
- `requirement.txt`: Lists Python dependencies required for the project.
- `app.py`: Main Python script implementing the web application’s logic.
- `vercel.json`: Configuration file for Vercel deployment.
- `crop_recommendation.csv`: Contains data on crops, soil, and climate conditions used by the recommendation system.


## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/Crop-Deployment.git
   cd Crop-Deployment
2. Install the dependencies:

   ```bash
   pip install -r requirement.txt

3.Run the application locally:

   ```bash
   python app.py

