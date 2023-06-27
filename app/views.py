from flask import Blueprint, jsonify, request
from .models import Tenant, ProjectMetadata

api_blueprint = Blueprint('app', __name__)

@api_blueprint.route('/tenants', methods=['POST'])
def create_tenant():
    name = request.json.get('name')
    tenant = Tenant(name=name)
    tenant.save()
    return jsonify(tenant), 201

@api_blueprint.route('/project_metadata', methods=['POST'])
def create_project_metadata():
    tenant_id = request.json.get('tenant_id')
    csv_location = request.json.get('csv_location')
    evaluation_results = request.json.get('evaluation_results')
    
    tenant = Tenant.objects.get(id=tenant_id)
    
    project_metadata = ProjectMetadata(tenant=tenant, csv_location=csv_location, evaluation_results=evaluation_results)
    project_metadata.save()
    
    return jsonify(project_metadata), 201
