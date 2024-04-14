// 'use client'

import { getProductById } from "@/Product/ProductController"

import Subtitle from "@/components/Subtitle"
import { useRouter } from "next/router"
import { useEffect, useState } from "react"
import { Product } from "@/Product/Product"

export default function Page({ params }) {
    const router = useRouter()
    const [product, setProducts] = useState<Product>()

    useEffect(() => {
        if (!router.query.id) {
            return
        }
        getProductById(Number(router.query.id)).then((res) => {
            setProducts(res)
        })
    }, [router.query.id])

    return (
        <>
            {
                product != undefined ?
                    <div>
                        <Subtitle>
                            Price: ${product.price}
                        </Subtitle>
                        <Subtitle>
                            Product name: {product.name} -
                        </Subtitle>
                        <Subtitle>
                            Code: {product.code} -
                        </Subtitle>
                        <Subtitle>
                            ID: {product.id}
                        </Subtitle>
                    </div>
                    :
                    'Product does not exist.'
            }

        </>
    )

}