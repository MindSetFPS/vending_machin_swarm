import { Product } from "./Product"

// Get a single product from the API
export const getProductById = (id: number): Promise<Product> => {
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/product/${id}`;
    return fetch(url, { cache: 'no-store' })
        .then((response) => response.json())
        .then((data) => {
            let product = new Product()
            product.code = data.code
            product.id = data.id
            product.name = data.name
            product.price = data.price

            return product
        });
};

// Get all products from API
export const getProducts = (): Promise<Product[]> => {
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/products`;

    return fetch(url, { cache: 'no-store' })
        .then((response) => response.json())
        .then((data) => {    
            return data.products.map((productData) => {
                let product = new Product()
                product.code = productData.code
                product.id = productData.id
                product.name = productData.name
                product.price = productData.price

                return product
            })}
        )
        .catch((error) => {
            console.error(error)
            return []
        })
};

// create product 
export const createProduct = (name: string, price: number, code: string) => {
    const url = `${process.env.NEXT_PUBLIC_BACKEND_URL}/api/products/create`;
    return fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            name: name,
            price: price,
            code: code
        })
    })
}