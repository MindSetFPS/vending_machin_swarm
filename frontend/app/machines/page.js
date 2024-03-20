import Title from "@/components/Title"
import { Button, Link } from "@nextui-org/react"

async function getData() {
    const res = await fetch('http://localhost:7777/api/vendingmachine/all', { cache: "no-store" })

    if (!res.ok) {
        throw new Error('Failed to fetch data')
    }

    return await res.json()
}

export default async function Machines() {

    const data = await getData()

    console.log(data)

    return (
        <>

            {
                data.lenght == 0 ?
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
                    </>
            }

            {data.map((e) => (
                <Link key={e.id} href={`/machines/${e.id}`} >
                    <div className="outline m-2 p-2 rounded-lg outline-2 outline-gray-200  shadow-md hover:shadow-lg transition-all block w-full">
                        Maquina {e.id}
                    </div>
                </Link>
            ))}

        </>
    )
}