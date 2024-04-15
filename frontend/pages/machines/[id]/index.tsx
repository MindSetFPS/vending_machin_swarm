// 'use client'

import { Button, Link } from "@nextui-org/react"

import { useEffect, useState } from "react"
import { useRouter } from 'next/router'
import { getMachineSales } from "@/Sale/SaleController"
import { getProductsByMachineId } from "@/VendingMachine/VendingMachineController"
import { Sale } from "@/Sale/Sale"
import { SaleResponse } from "@/Sale/SaleResponse"
import { MachineTabs } from "@/components/MachineTabs"
import { Product } from "@/Product/Product"
import VendingMachineProductStock from "@/VendingMachine/VendingMachineProductStock" 

export default function Page() {
    const router = useRouter()
    const [sales, setSales] = useState<SaleResponse[]>([])
    const [products, setProducts] = useState<VendingMachineProductStock[]>([])


    useEffect(() => {
        if (!router.query.id) {
            return
        }

        getMachineSales(Number(router.query.id)).then((res) => {
            setSales(res)
        })
        
        getProductsByMachineId(Number(router.query.id)).then((res) => {
            setProducts(res)
            console.log(products)
        })
    }, [router.query.id])

    return (
        <>
            <Button
                as={Link}
                href={`/assign-products/${router.query.id}`}
            >
                Asignar Productos
            </Button>

            <div>
                <MachineTabs sales={sales} products={products} machineId={router.query.id} />
                {
                    sales && sales.length > 0 ?
                        <div>{sales.map((sale) => (
                            <div key={sale.id} className="outline outline-2 outline-slate-300 rounded-lg p-2 mt-4 bg-slate-50 hover:shadow-xl transition" >
                                <div>{sale.product.name}</div>
                                <div>Fecha: {new Date(sale.date).toLocaleString()}</div>
                                <div>${sale.product.price}</div>
                            </div>
                        ))}</div>
                        :
                        <div>Esta maquina aun no tiene ventas</div>
                }
            </div>
        </>

    )
}