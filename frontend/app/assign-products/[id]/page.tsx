import Title from "@/components/Title";
import { getProducts } from "@/Product/ProductController";
import ProductList from "@/components/ProductList"

export default async function Page({ params }) {
    const products = await getProducts()
    console.log(products)

    return (
        <>
            <Title>
                Asigna productos a la maquina expendedora
            </Title>

            {
                products.length > 0 ?
                    <ProductList products={products} />
                    :
                    'No hay productos.'
            }

            Hello {params.id}
        </>
    )
}