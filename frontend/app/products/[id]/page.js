// 'use client'

async function getProduct(id) {
    const response = await fetch(`${process.env.BACKEND_URL}/api/product/${id}`, { cache : 'no-store'})
    if(!response.ok) {
        throw new Error('Error fetchging')
    }
}

export default async function Page({ params }){
    const product = await getProduct(params.id)

    console.log(product)
    return <p> Product: {params.id}</p>
}