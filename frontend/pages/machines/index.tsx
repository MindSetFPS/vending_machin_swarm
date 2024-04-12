// "use client"

import Title from "@/components/Title"
import { Link } from "@nextui-org/react"

import React, { useState, useEffect } from "react";

import { getVendingMachines } from "@/VendingMachine/VendingMachineController"
import CreateMachineModal from "@/components/CreateMachineModal";
import { VendingMachine } from "@/VendingMachine/VendingMachine";


export default function Machines() {
    const [vendingMachines, setVendingMachines] = useState<VendingMachine[]>()

    useEffect(() => {
        getVendingMachines().then((res) => {
            setVendingMachines(res)
            console.log(res)
        })
    }, [])

    const handleProdctCreated = async () => {
        setVendingMachines(await getVendingMachines())
    }

    if (!vendingMachines) return ("no items ")
    if (vendingMachines.length == 0) return ("no items for real ")

    return (
        <>
            {
                vendingMachines && vendingMachines.length == 0 ?

                    <>
                        <Title>
                            No hay maquinas
                        </Title>
                        <CreateMachineModal onProductCreated={handleProdctCreated} />
                    </>
                    :
                    <>
                        {
                            vendingMachines.length
                        }
                        <Title>
                            Lista de maquinas
                        </Title>

                        <CreateMachineModal onProductCreated={() => handleProdctCreated()} />
                        {vendingMachines.map((e) => (
                            <Link key={e.id} href={`/machines/${e.id}`} >
                                <div className="outline m-2 p-2 rounded-lg outline-2 outline-gray-200  shadow-md hover:shadow-lg transition-all block w-full">
                                    Maquina {e.id}
                                </div>
                            </Link>
                        ))}
                    </>
            }
        </>
    )
}