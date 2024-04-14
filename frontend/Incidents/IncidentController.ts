import Incident from "./Incidents";

const getIncidents = () => {
    console.log("todo")
    
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/incidents`
    return fetch(url, { cache: 'no-store'})
        .then((res) => res.json())
        .then((data) => data.map((incidentData: Incident) => {
            const { id, description, fixAtUrl, active } = incidentData;
            let incident = new Incident(id, description, fixAtUrl, active)
            return incident
        }))
}

const createIncident = () => {
    console.log("todo" )

}