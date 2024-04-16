import { machine } from "os";
import { IIncident, IIncidentResponse } from "./Incidents";

const getIncidents = (): Promise<IIncident[]> => {
    
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/incidents`
    return fetch(url, { cache: 'no-store'})
        .then((res) => res.json())
        .then((data) => data.map((incidentData: IIncidentResponse) => {
            const { id, description, fix_at_url, active, machine_id, product_id } = incidentData;
            let incident: IIncident = { id: id, description: description, fixAtUrl: fix_at_url, active: active, machineId: machine_id, productId: product_id }
            return incident
        }))
}

const updateIncident = (id: number, isActive: boolean) => {
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/incidents/update`

    fetch (url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            id: id,
            is_active: isActive
        })
    })
}

const createIncident = () => {
    console.log("todo" )

}

export { createIncident, getIncidents, updateIncident }