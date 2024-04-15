// "use client" 
import Title from "@/components/Title";
import { getProducts } from "@/Product/ProductController";
import ProductList from "@/components/ProductList"
import { Product } from "@/Product/Product";
import { useRouter } from "next/router";
import { useState, useEffect } from "react";
import { Button, Link } from "@nextui-org/react";

export default function Page() {
    const router = useRouter()
    const [products, setProducts] = useState<Product[]>()

    // https://nextjs.org/docs/pages/building-your-application/data-fetching/client-side#client-side-data-fetching-with-useeffect
    // https://medium.com/@harshil25patel/how-to-use-next-js-14-app-router-fetching-data-with-an-async-function-and-utilizing-react-hooks-ac02b71124cb
    // Little hack to make it fetch clientside
    useEffect(() => {
        if (!router.query.id) {
            return
        }

        getProducts().then((res) => {
            setProducts(res)
            console.log(products)
        })

    }, [router.query.id])

    return (
        <>
            <Title>
                Asigna productos a la maquina expendedora
            </Title>
            {products?.length}
            {
                products &&  products?.length > 0 ?
                    <ProductList products={products} vendingMachineId={Number(router.query.id)} />
                    :
                    <div>
                        <div>
                            No hay productos para asignar.
                        </div>
                        <Button as={Link} href="/products"> Ir a productos</Button>
                    </div>
            }
        </>
    )
}