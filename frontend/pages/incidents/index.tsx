import Title from "@/components/Title"
import { getIncidents } from "@/Incidents/IncidentController"
import { IIncident } from "@/Incidents/Incidents"
import { useEffect, useState } from "react"
import { Link, Spinner } from "@nextui-org/react";
import { Card, CardHeader, CardBody, CardFooter } from "@nextui-org/react";
import EditProductStockModal from "@/components/EditProductStockModal";
import { updateIncident } from "@/Incidents/IncidentController";

export default function Incidents() {

    const [incidents, setIncidents] = useState<IIncident[]>()
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
                    incidents.map((incident: IIncident) => (
                        <Card key={incident.id} className="mb-4">
                            <CardHeader>
                            <div>

                            {/* { incident.fixAtUrl ? 
                                <Link href={incident.fixAtUrl}>
                                    Fix
                                </Link>
                                :
                                ''
                            } */}
                            </div>
                            <div>

                            {
                                incident.active ? 
                                
                                <EditProductStockModal 
                                productId={incident.productId} 
                                machineId={incident.machineId} 
                                stock={10}  
                                onProductUpdated={() => updateIncident(incident.id, false)}
                                />
                                :
                                ''
                            }
                            </div>
                            </CardHeader>
                            <CardBody>
                                <p>
                                    <div>
                                    {/* {incident.fixAtUrl} */}
                                    </div>
                                    {incident.description}
                                    <div>
                                        Status: {incident.active ? 'Activo' : 'Resuelto'}
                                    </div>
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