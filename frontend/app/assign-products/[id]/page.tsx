"use client" 

import Title from "@/components/Title";
import { getProducts } from "@/Product/ProductController";
import ProductList from "@/components/ProductList"
import { Product } from "@/Product/Product";

import { useState, useEffect } from "react";

export default function Page({ params }) {

    const [ products, setProducts ] = useState<Product[]>()

    // https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side#client-side-data-fetching-with-useeffect
    // https://medium.com/@harshil25patel/how-to-use-next-js-14-app-router-fetching-data-with-an-async-function-and-utilizing-react-hooks-ac02b71124cb
    // Little hack to make it fetch clientside
    useEffect(() => {
        const fetchData = async () => {
            setProducts(await getProducts())
        }

        fetchData().catch( (error) => {
            console.error((error) => {
                console.error(error)
            })
        })

    }, [])

    return (
        <>
            <Title>
                Asigna productos a la maquina expendedora
            </Title>

            {
                products != undefined && products.length > 0 ?
                    <ProductList products={products} />
                    :
                    'No hay productos.'
            }
        </>
    )
}