import { Product } from "./Product"

// Get a single product from the API
export const getProduct = (id: number): Promise<Product> => {
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
        .then((data) => data.products.map((productData) => { 
            let product = new Product()
            product.code = productData.code
            product.id = productData.id
            product.name = productData.name
            product.price = productData.price

            return product
        }));
};
