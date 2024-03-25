'use client'

import { Button, Link } from "@nextui-org/react"

export default function Page({ params }){
   
    return (
        <>
            <p> Machine: {params.id}</p>
            <Button
                as={Link}
                href={`/assign-products/${params.id}`}
            >
                Asignar Productos
            </Button>
        </>
        
    )
}