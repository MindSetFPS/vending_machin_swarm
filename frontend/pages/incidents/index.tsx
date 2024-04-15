import Title from "@/components/Title"
import { getIncidents } from "@/Incidents/IncidentController"
import Incident from "@/Incidents/Incidents"
import { useEffect, useState } from "react"
import { Spinner } from "@nextui-org/react";
import { Card, CardHeader, CardBody, CardFooter } from "@nextui-org/react";

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
                Hola tonotos
            </Title>
            {
                incidents && incidents.length > 0 ?
                    incidents.map((incident: Incident) => (
                        <Card key={incident.id} className="mb-4">
                            <CardHeader>
                                {incident.fixAtUrl}
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
                    'no'
            }
        </>
    )
}