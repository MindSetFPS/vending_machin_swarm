"use client"

import { Product } from "@/Product/Product"
import { Button } from "@nextui-org/react"
import { ReactNode } from "react"

interface ProductProp {
    product: Product,
    children?: ReactNode
}
export function ProductItem({ product, children }: ProductProp) {
    // const [productsToUpload, setProductsToUpload] = useState([])
    // function clickHandler(){
    //     setProductsToUpload([...productsToUpload, 1])
    //     console.log(productsToUpload)
    // }
    return (
        <>
            <div className="flex justify-between content-center align-middle items-center outline m-2 p-2 rounded-lg outline-2 outline-gray-200  shadow-md hover:shadow-lg transition-all w-full">

                <div>
                    <div>
                        Nombre: {product.name}
                    </div>
                    <div>
                        Id: {product.id}
                    </div>
                    <div>
                        ${product.price}
                    </div>
                    <div>
                        Code: {product.code}
                    </div>
                </div>
                <Button size="md" variant="faded" onPress={() => console.log("holaaa")}> Agregar {product.id}  </Button>
                {children}
            </div>
        </>
    )
}

// https://stackoverflow.com/questions/69885310/typescript-error-type-type-is-not-assignable-to-type-intrinsicattributes

interface ProducListProps {
    products: Product[],
}

export default function ProductList({ products }: ProducListProps) {
    return (
        <>
            {products.map((product: Product) => (

                <ProductItem key={product.id} product={product} >
                </ProductItem>

            ))}
        </>
    )
}