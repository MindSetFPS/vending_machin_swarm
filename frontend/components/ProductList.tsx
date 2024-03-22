import { Product } from "@/Product/Product"
import { Link } from "@nextui-org/react"


export default function ProductList(products: Array<Product>) {

    // console.log("p: ", products.products)
    return (
        <>
            {products.products.map((e) => (
                    <div key={e.id}  className="outline m-2 p-2 rounded-lg outline-2 outline-gray-200  shadow-md hover:shadow-lg transition-all block w-full">
                        Product {e.id}
                    </div>
            ))}
        </>
    )
}