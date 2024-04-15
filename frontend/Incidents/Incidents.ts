export interface IIncident {
    id: number,
    description: string,
    fixAtUrl: string,
    active: boolean
}

export default class Incident implements IIncident {
    id: number;
    description: string;
    fixAtUrl: string;
    active: boolean;

    constructor(id: number, description: string, fixAtUrl: string, active: boolean){
        this.id = id
        this.description = description;
        this.fixAtUrl = fixAtUrl;
        this.active = active;
    }
}

export interface IIncidentResponse {
    id: number,
    description: string,
    fix_at_url: string,
    active: boolean
}