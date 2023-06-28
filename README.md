
- The `app/` directory contains the application models and other related files.
- `main.py` is the main script that coordinates the ML component, Flask API, and MongoDB integration.
- `.env.example` is an example file for setting up environment variables.
- `requirements.txt` lists the required packages for the project.
- `README.md` is the project documentation file.

## Requirements

- Python 3.7 or higher
- Flask
- Flask-RESTful
- pymongo
- scikit-learn
- python-dotenv

## Installation

1. Clone the repository:git clone flask
2. Change to the project directory: cd flask-api-project
3. Create and activate a virtual environment:
     python3 -m venv venv
     source venv/bin/activate
4. Install the required dependencies: pip install -r requirements.txt
5. Set up the environment variables:

- Rename the `.env.example` file to `.env`.
- Update the values in the `.env` file according to your environment.

6. Start the Flask development server: flask run
7. The API will be accessible at `http://localhost:5000`.

## Endpoints

### `POST /tenants`

Create a new tenant.

**Request Body:**

```json
{
"name": "Tenant Name"
}

Response: {
  "id": 1,
  "name": "Tenant Name"
}

POST /project-metadata
Create a new project metadata record.

Request Body: {
  "tenant_id": 1,
  "csv_location": "C:\flask\Salary_Data.csv",
  "model_evaluation": {
  "Mean Absolute Error": 5500,
  "Root Mean Squared Error": 7000,
  "R-squared": 0.85
}
}
GET /tenants
Retrieve all tenants.

Response:  [
  {
    "id": 1,
    "name": "Tenant Name"
  },
  {
    "id": 2,
    "name": "Another Tenant"
  }
]

