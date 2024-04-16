export interface IIncident {
    id: number,
    description: string,
    fixAtUrl?: string,
    active: boolean,
    machineId?: number,
    productId?: number,
}

/* export default class Incident implements IIncident {
    id: number;
    description: string;
    active: boolean;
    fixAtUrl: string;
    machine_id: <number>;
    product_id: number;

    constructor(id: number, description: string, active: boolean, fixAtUrl?: string, machine_id?: number, product_id?: number ){
        this.id = id
        this.description = description;
        this.fixAtUrl = fixAtUrl ?? '';
        this.active = active;
        this.machine_id = machine_id ?? undefined;
    }
} */

export interface IIncidentResponse {
    id: number,
    description: string,
    fix_at_url?: string,
    active: boolean,
    machine_id?: number,
    product_id?: number
}