'use client'

import { Button, Link } from "@nextui-org/react"
import { Sale } from "@/Sale/Sale"

import { useEffect, useState } from "react"

import { getMachineSales } from "@/Sale/SaleController"

export default function Page({ params }){
   
    const [ sales, setSales ] = useState<Sale[]>([])

    useEffect(() => {
        const fetchData = async () => {
            setSales(await getMachineSales(params.id))
        }

        fetchData().catch( (error) => {
            console.error((error) => {
                console.error(error)
            })
        })

    }, [])

    return (
        <>
            <p> Machine: {params.id}</p>
            <Button
                as={Link}
                href={`/assign-products/${params.id}`}
            >
                Asignar Productos
            </Button>

            <div>
                <h1>Ventas</h1>
                {
                    sales && sales.length > 0 ? 
                    <div>{sales.map((sale) => (
                        <div key={sale.id}> 
                            <div>{sale.id}</div>
                            <div>Fecha: {new Date(sale.date).toLocaleString()}</div>
                        </div>
                    ))}</div>
                    :
                    <div>Esta maquina aun no tiene ventas</div>
                }
            </div>
        </>
        
    )
}