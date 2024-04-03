import { Button, Link } from "@nextui-org/react"
import { getProducts } from "@/Product/ProductController"

export default async function Product(){
    const data = await getProducts()
    console.log(data)
    return(
        <>
            <div className="container">
                <h1 className="text-5xl font-bold">Products Page</h1>

            </div>

            {
                data.products == 0 ? 
                'No products' 
                : 
                <div>
                    {data.map((e) => (
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