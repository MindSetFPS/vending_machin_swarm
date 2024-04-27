from Server.Repository.Repository import IDatabase
from Server.Incident.domain.Incident import Incident
from Server.Incident.infrastructure.IncidentRepository import incident_repository
from sqlmodel import select

class IncidentController:
    def __init__(self, incident_repository: IDatabase) -> None:
        self.repository = incident_repository
        

    def create_incident(self, incident: Incident):
        self.repository.create(incident)
    
    def get_all(self):
        query = select(Incident)
        return self.repository.get_all(query)
        
incident_controller = IncidentController(incident_repository=incident_repository)