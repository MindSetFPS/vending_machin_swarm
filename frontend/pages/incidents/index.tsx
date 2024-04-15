import Title from "@/components/Title"
import { getIncidents } from "@/Incidents/IncidentController"
import Incident from "@/Incidents/Incidents"
import { useEffect, useState } from "react"
import { Link, Spinner } from "@nextui-org/react";
import { Card, CardHeader, CardBody, CardFooter } from "@nextui-org/react";
import EditProductStockModal from "@/components/EditProductStockModal";

export default function Incidents() {

    const [incidents, setIncidents] = useState<Incident[]>()
    const [loading, setLoading] = useState<boolean>(true)


    useEffect(() => {
        setLoading(true)
        getIncidents().then((res) => {
            setIncidents(res)
            setLoading(false)
        })
        console.log(incidents)

    }, [])

    if (loading) return (<Spinner />)
    return (
        <>
            <Title>
               Incidentes 
            </Title>
            {
                incidents && incidents.length > 0 ?
                    incidents.map((incident: Incident) => (
                        <Card key={incident.id} className="mb-4">
                            <CardHeader>
                            { incident.fixAtUrl ? 
                                <Link href={incident.fixAtUrl}>
                                    Fix
                                </Link>
                                :
                                ''
                            }
                                {/* <EditProductStockModal productId={1} machineId={1} stock={10}  onProductUpdated={() => console.log("yess")}/> */}
                            </CardHeader>
                            <CardBody>
                                <p>
                                    {incident.fixAtUrl}
                                    {incident.description}
                                </p>
                                
                            </CardBody>
                        </Card>

                    ))
                    :
                    'Sin incidentes.'
            }
        </>
    )
}