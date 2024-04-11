import Title from "@/components/Title"
import { Button, Link } from "@nextui-org/react"

import { getVendingMachines } from "@/VendingMachine/VendingMachineController"

export default async function Machines() {

    const data = await getVendingMachines()

    console.log("data: ", data.length)

    return (
        <>

            {
                data && data.length == 0 ?

                    <>
                        <Title>
                            No hay maquinas
                        </Title>
                        <Button
                            href="/machines/create"
                            as={Link}
                            color="primary"
                        >
                            Crear una maquina
                        </Button>
                    </>
                    :
                    <>
                        <Title>
                            Lista de maquinas
                        </Title>
                        {data.map((e) => (
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