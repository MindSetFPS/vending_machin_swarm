"use client"
import { Button, Modal, ModalContent, ModalHeader, ModalBody, ModalFooter, useDisclosure, Checkbox, Input, } from "@nextui-org/react"

import { getVendingMachines, createVendingMachine } from "@/VendingMachine/VendingMachineController"
import { createProduct } from "@/Product/ProductController"
import { useEffect, useState } from "react"
import { VendingMachine } from "@/VendingMachine/VendingMachine"

export default function CreateProductsModal({ onProductCreated }) {

    const [name, setName] = useState<string>()
    const [price, setPrice] = useState<number>()
    const [code, setCode] = useState<string>()
    const [vendingMachines, setVendingMachines] = useState<VendingMachine[]>()

    function updateVendingMachineList() {
        getVendingMachines()
            .then((res) => {
                setVendingMachines(res)
            })
    }

    function handleCreateButton(onClose){
        console.log(name, price, code)
        createProduct(name, price, code)
        updateVendingMachineList()
        onProductCreated()
        onClose()
    }

    useEffect(() => {
        updateVendingMachineList()
    }, [])

    const { isOpen, onOpen, onOpenChange } = useDisclosure();
    return (
        <>
            <Button onPress={onOpen} color="primary">Open Modal</Button>
            <Modal
                isOpen={isOpen}
                onOpenChange={onOpenChange}
                placement="top-center"
            >
                <ModalContent>
                    {(onClose) => (
                        <>
                            <ModalHeader>
                                Crea una nuevo producto
                            </ModalHeader>
                            <ModalBody>

                                <Input type="text" label="nombre" labelPlacement="inside" value={name} onChange={ (event) => setName(event.target.value) } />
                                    <Input type="number" label="precio" labelPlacement="inside" value={price} onChange={ (event) => setPrice(event.target.value) }  />
                                    <Input type="text" label="codigo" labelPlacement="inside" value={code} onChange={ (event) => setCode(event.target.value) }  />

                            </ModalBody>
                            <ModalFooter>
                                <Button
                                    onPress={() => handleCreateButton(onClose)}
                                    color="primary"
                                >Crear</Button>
                            </ModalFooter>
                        </>
                    )}
                </ModalContent>
            </Modal>
        </>
    )
}