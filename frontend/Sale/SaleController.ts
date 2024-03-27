import { Sale } from "./Sale"

const getSale = (): Sale => {
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/`
    return
}

const getSales = (): Promise<Sale[]> => {
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/sales`

    return fetch(url, { cache: 'no-store' })
        .then((response) => response.json())
        .then((data) => data.map((saleData) => {
            let sale = new Sale()

            sale.date = saleData.date
            sale.id = saleData.id
            sale.machineId = saleData.machine_id
            sale.productId = saleData.product_id

            return sale
        }))
}

const getMachineSales = (machineId: number): Promise<Sale[]> => {
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/sales/machine/${machineId}`

    return fetch(url, { cache: 'no-store' })
    .then((response) => response.json())
    .then((data) => data.map((saleData) => {
        let sale = new Sale()

        sale.date = saleData.date
        sale.id = saleData.id
        sale.machineId = saleData.machine_id
        sale.productId = saleData.product_id

        return sale
    }))

}

export { getSale, getSales, getMachineSales}