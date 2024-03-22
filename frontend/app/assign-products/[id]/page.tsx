import Title from "@/components/Title";
import { getProducts } from "@/Product/ProductController";
import ProductList from "@/components/ProductList"

export default async function Page({ params }){
    
    const products = await getProducts()
    
    console.log(products)
    console.log(products.products)

    return(
        <>
            <Title>
                Asigna productos a la maquina expendedora
            </Title>

            {
                products.products != 'undefined' ? 
                <ProductList products={products.products} />
                :
                'No'
            }
            
            Hello {params.id}
        </>
    )
}