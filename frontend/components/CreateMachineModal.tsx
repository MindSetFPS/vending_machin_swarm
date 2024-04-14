"use client"
import { Button, Modal, ModalContent, ModalHeader, ModalBody, ModalFooter, useDisclosure, Checkbox, Input, } from "@nextui-org/react"

import { getVendingMachines, createVendingMachine } from "@/VendingMachine/VendingMachineController"
import { useEffect, useState } from "react"
import { VendingMachine } from "@/VendingMachine/VendingMachine"

export default function CreateMachineModal({ onProductCreated }) {

    const [isOn, setIsOn] = useState(false)
    const [name, setName] = useState<string>()
    const [x, setX] = useState(false)
    const [y, setY] = useState(false)
    const [vendingMachines, setVendingMachines] = useState<VendingMachine[]>()

    function updateVendingMachineList() {
        getVendingMachines()
            .then((res) => {
                setVendingMachines(res)
            })
    }

    function handleCreateButton(onClose){
        createVendingMachine(isOn)
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
            <Button onPress={onOpen} color="primary">Crear maquina expendedora</Button>
            <Modal
                isOpen={isOpen}
                onOpenChange={onOpenChange}
                placement="top-center"
            >
                <ModalContent>
                    {(onClose) => (
                        <>
                            <ModalHeader>
                                Crea una nueva maquina
                            </ModalHeader>
                            <ModalBody>

                                <Input type="text" label="name" labelPlacement="inside" value={name} />
                                <Checkbox> La maquina está encendida </Checkbox>
                                Coordenadas
                                <div className="flex justify-between">
                                    <Input className="px-2" type="text" label="x" labelPlacement="inside" />
                                    <Input className="px-2" type="text" label="y" labelPlacement="inside" />
                                </div>

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