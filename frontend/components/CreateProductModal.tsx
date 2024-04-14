import { Button, Modal, ModalContent, ModalHeader, ModalBody, ModalFooter, useDisclosure, Checkbox, Input, } from "@nextui-org/react"
import { useEffect, useState } from "react"
import { createProduct } from "../Product/ProductController"

export default function CreateProductModal() {

    const [name, setName] = useState<string>("")
    const [price, setPrice] = useState<number>(0)
    const [code, setCode] = useState<string>("")
    const { isOpen, onOpen, onOpenChange } = useDisclosure();
    
    function cleanFields(){
        setName("")
        setPrice(0)
        setCode("")
    }

    function handleClick(close){
        console.log("clicked")
        
        createProduct(name, price, code)
        cleanFields()
        close()
    }

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
                                Crear nuevo produto
                            </ModalHeader>
                            <ModalBody>

                                <Input type="text" label="name" labelPlacement="inside" value={name} onChange={(event) => setName(event.target.value)}/>
                                <Input type="number" label="precio" labelPlacement="inside" value={String(price)} onChange={(event) => setPrice(Number(event.target.value))} />
                                <Input type="text" label="codigo" labelPlacement="inside" value={code} onChange={(event) => setCode(event.target.value)}/>

                            </ModalBody>
                            <ModalFooter>
                                <Button
                                    onPress={() => handleClick(onClose)}
                                    color="primary"
                                >
                                    Crear
                                </Button>
                            </ModalFooter>
                        </>
                    )}
                </ModalContent>
            </Modal>
        </>
    )
}