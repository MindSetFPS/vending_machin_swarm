import { VendingMachine } from "./VendingMachine";

// async function getData() {
//     const res = await fetch('http://localhost:7777/api/vendingmachine/all', { cache: "no-store" })

//     if (!res.ok) {
//         throw new Error('Failed to fetch data')
//     }

//     return await res.json()
// }

export function getVendingMachines(): Promise<VendingMachine[]> {
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/vendingmachine/all`

    return fetch(url, { cache: 'no-store'})
        .then((response) => response.json())
        .then((data) => data.map((vendingMachineData) => {
            let vendingMachine = new VendingMachine()
            vendingMachine.id = vendingMachineData.id
            vendingMachine.is_on = vendingMachineData.is_on
            vendingMachine.products = []

            return vendingMachine
        }))
        
}