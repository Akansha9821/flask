import os
import requests
from app.models import Tenant, ProjectMetadata
from app import create_app
import pandas as pd
from sklearn.linear_model import LinearRegression
from dotenv import load_dotenv


app = create_app()
load_dotenv()

def train_model(csv_file):
    # Load CSV data into a pandas DataFrame

    data = pd.read_csv(csv_file)
    
    # Select the features (columns) and target (salary)
    features = os.environ.get('COLUMNS')
    target = os.environ.get('TARGET')
    X = data[features]
    y = data[target]
    
    # Convert categorical variables to dummy variables
    X = pd.get_dummies(X)
    
    # Train a linear regression model
    model = LinearRegression()
    model.fit(X, y)
    
    return model

def main():
    with app.app_context():
        # Create a tenant
        tenant_name = 'My Tenant'
        tenant = Tenant(name=tenant_name)
        tenant.save()

        # Read environment variables
        csv_file = os.environ.get('CSV_FILE_PATH')

        # Train the model
        model = train_model(csv_file)

        # Save project metadata
        project_metadata = ProjectMetadata(tenant=tenant, csv_location=csv_file)
        project_metadata.save()

        # Fetch and print the generated tenant and project metadata records
        tenants = Tenant.objects.all()
        print('Tenants:')
        print(tenants)

        metadata = ProjectMetadata.objects.all()
        print('Project Metadata:')
        print(metadata)

if __name__ == '__main__':
    main()
