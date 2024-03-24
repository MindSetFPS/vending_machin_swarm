import { Product } from "@/Product/Product"
import { Button } from "@nextui-org/react"

interface ProductProp {
    product: Product
}
export function ProductItem(product: ProductProp) {
    return (
        <>
            <div className="flex justify-between content-center align-middle items-center outline m-2 p-2 rounded-lg outline-2 outline-gray-200  shadow-md hover:shadow-lg transition-all w-full">

                <div>
                    <div>
                        Nombre: {product.product.name}
                    </div>
                    <div>
                        Id: {product.product.id}
                    </div>
                    <div>
                        ${product.product.price}
                    </div>
                    <div>
                        Code: {product.product.code}
                    </div>
                </div>
                <Button size="md" variant="faded"> Agregar {product.product.id} </Button>
            </div>
        </>
    )
}

interface ProducListProps {
    products: Product[]
}

// https://stackoverflow.com/questions/69885310/typescript-error-type-type-is-not-assignable-to-type-intrinsicattributes
export default function ProductList(products: ProducListProps) {
    return (
        <>
            {products.products.map((product: Product) => (

                <ProductItem key={product.id} product={product} ></ProductItem>

            ))}
        </>
    )
}