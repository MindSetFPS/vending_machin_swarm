export class SaleResponse {
    date: string;
    id: number;
    machineId: number;
    product: {
        id: number;
        name: string;
        price: number;
        code?: string
    }
}