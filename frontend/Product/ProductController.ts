
// Get a single product from the API
export async function getProduct(id) {
    const response = await fetch(`${process.env.BACKEND_URL}/api/product/${id}`, { cache : 'no-store'})
    if(!response.ok) {
        throw new Error('Error fetchging')
    }

    return response.json()
}

// Get all products from API
export async function getProducts() {
    const response = await fetch(`${process.env.BACKEND_URL}/api/products`, { cache : 'no-store'})
    if(!response.ok) {
        throw new Error("Error fetching")

    }

    return response.json()
}