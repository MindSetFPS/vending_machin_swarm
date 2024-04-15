import Incident, { IIncident, IIncidentResponse } from "./Incidents";

const getIncidents = (): Promise<Incident[]> => {
    
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/incidents`
    return fetch(url, { cache: 'no-store'})
        .then((res) => res.json())
        .then((data) => data.map((incidentData: IIncidentResponse) => {
            const { id, description, fix_at_url, active } = incidentData;
            let incident: IIncident = { id: id, description: description, fixAtUrl: fix_at_url, active: active}
            return incident
        }))
}

const createIncident = () => {
    console.log("todo" )

}

export { createIncident, getIncidents }