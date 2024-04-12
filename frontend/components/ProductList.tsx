"use client"

import { Product } from "@/Product/Product"
import { Button } from "@nextui-org/react"
import { ReactNode, useState, useEffect } from "react"
import { assigntProductsToVendingMachine } from "@/VendingMachine/VendingMachineController"

interface ProductProp {
    product: Product,
    children?: ReactNode,
    onTap: (productId: number) => void;
}
export function ProductItem({ product, children, onTap }: ProductProp) {
    const [selected, setSelected] = useState<boolean>(false)
    
    function clickHandler(event){
        onTap(event)
        setSelected(!selected)
    }
    
    return (
        <>
            <div className={`${selected ? "outline-blue-600 bg-blue-200" : "" } flex justify-between content-center align-middle items-center outline m-2 p-2 rounded-lg outline-2 outline-gray-200  shadow-md hover:shadow-lg transition-all w-full`}>

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
                <Button size="md" variant="faded" onPress={() => clickHandler(product.id)}> Agregar {product.id}  </Button>
                {children}
            </div>
        </>
    )
}

// https://stackoverflow.com/questions/69885310/typescript-error-type-type-is-not-assignable-to-type-intrinsicattributes

interface ProducListProps {
    products: Product[],
    vendingMachineId: number
}

export default function ProductList({ products, vendingMachineId }: ProducListProps) {

    const [ productsToAdd, setProductsToAdd ] = useState<number[]>([])
    
    function handleTap(productId){
        if(!productsToAdd.includes(productId)){
            setProductsToAdd([...productsToAdd, productId])
        } else {
            let newArr = [...productsToAdd]
            let index = newArr.indexOf(productId)
            newArr.splice(index, 1)
            setProductsToAdd(newArr)
        }
        console.log(productsToAdd)

    }

    function assignButton(){
        assigntProductsToVendingMachine(productsToAdd, vendingMachineId)
    }
    
    return (
        <>
            <div className="flex">
                <Button onPress={assignButton} > Asignar </Button>

                {productsToAdd.map((product: number) => (
                    <div key={product}>
                        {product}
                    </div>
                ))}
            </div>


            {products.map((product: Product) => (

                <ProductItem key={product.id} product={product} onTap={handleTap} >
                </ProductItem>

            ))}
        </>
    )
}