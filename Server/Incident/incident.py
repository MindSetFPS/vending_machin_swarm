from fastapi import APIRouter
from Server.Incident.application.IncidentController import incident_controller
from Server.Incident.domain.Incident import Incident
router = APIRouter(
    prefix="/incident",
    tags=["incidents"]
)

@router.get("/incident")
async def incident(): 
    return {
        "ok" : True
    }
    


@router.get('/')
async def get_incidents():
    incidents = incident_controller.get_all()
    print(incidents)
    
    return incidents


@router.post("/api/warnings/create")
async def create_warning(incident: Incident):
    new_warning = incident_controller.create_warning(incident=incident)
    