from Server.Repository.Repository import IDatabase
from Server.Models.Incident import Incident
from Server.Repository.IncidentRepository import incident_repository

class IncidentController:
    def __init__(self, incident_repository: IDatabase) -> None:
        self.repository = incident_repository
        

    def create_warning(self, incident: Incident):
        self.repository.create(incident)
        
incident_controller = IncidentController(incident_repository=incident_repository)