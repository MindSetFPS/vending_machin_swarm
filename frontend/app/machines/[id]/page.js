'use client'

// import { useSearchParams } from "next/navigation"

import { useRouter } from 'next/router'
import { useEffect } from "react"

export default function Page({ params }){
    // const searchParams = useSearchParams()
    // const router = useRouter()

    // useEffect(() => {
    //     if (router.isReady) {
    //         console.log(router.query)
    //     } else {
    //         console.log("Router is not ready yet")
    //     }
    // }, [router.isReady])


    return <p> Machine: {params.id}</p>
}