import { Button, Modal, ModalContent, ModalHeader, ModalBody, ModalFooter, useDisclosure, Checkbox, Input, } from "@nextui-org/react"

import { getVendingMachines, createVendingMachine, refillVendingMachineStock } from "@/VendingMachine/VendingMachineController"
import { useEffect, useState } from "react"
import { VendingMachine } from "@/VendingMachine/VendingMachine"

export default function EditProductStockModal({ onProductUpdated, productId, machineId, stock }) {

    const [name, setName] = useState<string>()
    const [vendingMachines, setVendingMachines] = useState<VendingMachine[]>()
    const [newStock, setNewStock] = useState<number>(stock)

    function updateVendingMachineList() {
        getVendingMachines()
            .then((res) => {
                setVendingMachines(res)
            })
    }

    function handleCreateButton(onClose) {
        refillVendingMachineStock(machineId, productId, newStock)
        onProductUpdated()
        onClose()
    }

    useEffect(() => {
        updateVendingMachineList()
    }, [])

    const { isOpen, onOpen, onOpenChange } = useDisclosure();
    return (
        <>
            <Button onPress={onOpen} color="primary">Cambiar stock</Button>
            <Modal
                isOpen={isOpen}
                onOpenChange={onOpenChange}
                placement="top-center"
            >
                <ModalContent>
                    {(onClose) => (
                        <>
                            <ModalHeader>
                                Editar Producto {productId} en maquina {machineId}
                            </ModalHeader>
                            <ModalBody>
                                <div className="flex justify-between">
                                    <Input className="px-2" type="number" label="stock" labelPlacement="inside" value={String(newStock)} onChange={(e) => setNewStock(Number(e.target.value))} />
                                </div>

                            </ModalBody>
                            <ModalFooter>
                                <Button
                                    onPress={() => handleCreateButton(onClose)}
                                    color="primary"
                                >Actualizar</Button>
                            </ModalFooter>
                        </>
                    )}
                </ModalContent>
            </Modal>
        </>
    )
}