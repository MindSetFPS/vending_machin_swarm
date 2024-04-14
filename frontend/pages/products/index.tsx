import { Button, Link } from "@nextui-org/react"
import { getProducts } from "@/Product/ProductController"
import { useEffect, useState } from "react"
import { Product } from "@/Product/Product"

export default function Product(){

    const [ products, setProducts ] = useState<Product[]>([])
   
    useEffect(() => {
        getProducts().then((res) => {
            setProducts(res)
            console.log(res)
        })
    }, []) 

    if(products.length == 0) return("No products ")

    return(
        <>
            <div className="container">
                <h1 className="text-5xl font-bold">Products Page</h1>

            </div>

            {
                products && products.length == 0 ? 
                <>
                <Button
                    href="/products/create"
                    as={Link}
                    color="primary"
                >Crear un producto</Button>
                </>

                : 
                <div>
                    {products.map((e) => (
                        <Link key={e.id} href={`/products/${e.id}`} >
                            <div className="outline m-2 p-2 rounded-lg outline-2 outline-gray-200  shadow-md hover:shadow-lg transition-all block w-full">
                                Product {e.id}
                            </div>
                        </Link>
                    ))}
                </div>
            }

        </>
    )
}