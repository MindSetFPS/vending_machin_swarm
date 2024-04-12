// 'use client'

import { getProduct } from "@/Product/ProductController"
import Subtitle from "@/components/Subtitle"

export default async function Page({ params }){
    const product = await getProduct(params.id)

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