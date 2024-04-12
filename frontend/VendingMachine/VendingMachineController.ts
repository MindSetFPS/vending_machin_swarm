import { Product } from "@/Product/Product";
import { VendingMachine } from "./VendingMachine";
import VendingmachineProductStock from "./VendingMachineProductStock"

// async function getData() {
//     const res = await fetch('http://localhost:7777/api/vendingmachine/all', { cache: "no-store" })

//     if (!res.ok) {
//         throw new Error('Failed to fetch data')
//     }

//     return await res.json()
// }

export function getVendingMachines(): Promise<VendingMachine[]> {
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/vendingmachine/all`

    return fetch(url, { cache: 'no-store' })
        .then((response) => response.json())
        .then((data) => {
            let vms: VendingMachine[] = []

            if (Array.isArray(data) && data.length > 0) {

                vms = data.map((vendingMachineData) => {
                    console.log(vendingMachineData)
                    let vendingMachine = new VendingMachine()
                    vendingMachine.id = vendingMachineData.id
                    vendingMachine.is_on = vendingMachineData.is_on
                    vendingMachine.products = []

                    return vendingMachine
                })
            }
            return vms
        })
        .catch((e) => {
            console.error(e)
            return []
        })
}

export function createVendingMachine(is_on: boolean) {
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/vendingmachine/create`
    return fetch(url, {
        cache: 'no-store',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            is_on: is_on
        })
    })
}

export function assigntProductsToVendingMachine(productIdList: number[], machineId: number) {
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/vendingmachine/assign/${machineId}`

    return fetch(url, {
        cache: 'no-store',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(productIdList)
    })
}

export function getProductsByMachineId(machineId: number): Promise<VendingmachineProductStock[]> {
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/vendingmachine/${machineId}/products`

    return fetch(url, { cache: 'no-store' })
        .then((res) => res.json())
        .then((data) => {
            let products: VendingmachineProductStock[] = []
            if (Array.isArray(data) && data.length > 0) {
                products = data.map((productData) => {
                    // console.log(productData)
                    let product: VendingmachineProductStock = {
                        machineId: productData.machine_id,
                        productId: productData.product_id,
                        stock: productData.stock
                    }

                    return product
                })
            }
            // console.log(products)
            return products
        })
        .catch((e) => {
            console.error(e)
            return []
        })
}

export function refillVendingMachineStock(machineId: number, productId: number, stock: number) {
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/vendingmachine/refill`

    return fetch(url, {
        cache: 'no-store',
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            product_id: productId,
            machine_id: machineId,
            stock: stock
        })
    })
}