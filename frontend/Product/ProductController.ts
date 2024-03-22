import { Product } from "./Product"

// Get a single product from the API
// export async function getProduct(id: number) {
//     const response = await fetch(`${process.env.BACKEND_URL}/api/product/${id}`, { cache : 'no-store'})
//     if(!response.ok) {
//         throw new Error('Error fetchging')
//     }

//     const res = await response.json()

//     const product = new Product()

//     product.code = res.code
//     product.id = res.id
//     product.name = res.name
//     product.price = res.price

//     return product
// }

export const getProduct = (id: number): Promise<Product> => {
    const url = `${process.env.BACKEND_URL}/api/product/${id}`;
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
// export async function getProducts() {
//     const response = await fetch(`${process.env.BACKEND_URL}/api/products`, { cache: 'no-store' })
//     if (!response.ok) {
//         throw new Error("Error fetching")

//     }

//     return response.json()
// }

export const getProducts = (): Promise<Product[]> => {
    const url = `${process.env.BACKEND_URL}/api/products`;
    return fetch(url, { cache: 'no-store' })
        .then((response) => response.json())
        .then((data) => data.map((productData) => new Product(productData)));
};
