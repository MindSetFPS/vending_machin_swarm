import { Sale } from "./Sale"
import { SaleResponse } from "@/Sale/SaleResponse"

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

const getMachineSales = (machineId: number): Promise<SaleResponse[]> => {
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/sales/machine/${machineId}`

    return fetch(url, { cache: 'no-store' })
        .then((response) => response.json())
        .then((data) => data.map((saleData) => {
            let sale = new SaleResponse()

            let productData = {
                id: saleData.sale.product.id,
                name: saleData.sale.product.name,
                price: saleData.sale.product.price
            }

            sale.date = saleData.sale.date
            sale.id = saleData.sale.id
            sale.machineId = saleData.sale.machine_id
            sale.product = productData;

            return sale
        }))

}

export { getSale, getSales, getMachineSales }