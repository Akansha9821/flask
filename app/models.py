from flask_mongoengine import MongoEngine

db = MongoEngine()

class Tenant(db.Document):
    name = db.StringField(required=True, unique=True)
    # Add more sensible columns as per your requirements

class ProjectMetadata(db.Document):
    tenant = db.ReferenceField(Tenant, required=True)
    csv_location = db.StringField(required=True)
    evaluation_results = db.StringField()