from Server.Repository.Repository import IDatabase, repository

from Server.Incident.domain.Incident import Incident 

from sqlmodel import select

class IncidentRepository:
    def __init__(self, repository: IDatabase) -> None:
        self._repository = repository

    def get_all(self, statement):
        return self._repository.get_all(statement)
    
    def get_by_id(self, id):
        statement = select(Incident).where(Incident.id == id)
        return self._repository.get_by_id(statement)
    
    def delete(self, id):
        warning = self.get_by_id(id=id)
        return self._repository.delete(warning)
    
    def create(self, incident: Incident):
        return self._repository.create(incident)
    
    def update(self, item):
        return self._repository.update(item)
    
incident_repository = IncidentRepository(repository=repository)