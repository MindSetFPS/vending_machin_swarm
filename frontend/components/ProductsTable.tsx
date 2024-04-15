
import { Table, TableHeader, Link, Button, TableColumn, TableBody, TableRow, TableCell, getKeyValue, Tooltip } from "@nextui-org/react";

import EditProductStockModal from "./EditProductStockModal";
import { useCallback } from "react";
import { EyeIcon } from "./EyeIcon";
import { EditIcon } from "./EditIcon";
import { DeleteIcon } from "./DeleteIcon";

export default function ProductsTable({ machineProductsList, machineId }) {
    console.log(machineProductsList)
    const columns = [
        {
            key: "machineId",
            label: "machineId"
        },
        {
            key: "productId",
            label: "productId"
        },
        {
            key: "stock",
            label: "stock"
        },
        {
            key: "actions",
            label: "Actions"
        }
    ]

    const renderCell = useCallback((item, columnKey) => {
        const cellValue = item[columnKey];
        console.log(item)
        console.log(cellValue)
        switch (columnKey) {

            case "machineId":
                return (
                    <p className="text-bold text-sm capitalize">{item.machineId}</p>
                );
            case "productId":
                return (
                    <div>
                        {item.productId}
                    </div>
                );

            case "stock":
                return (
                    <div>
                        {item.stock}
                    </div>
                );
            case "actions":
                return (
                    <div className="relative flex items-center gap-2">
                        <Button isIconOnly as={Link} href={`/products/${item.productId}`}>

                            <span className="text-lg text-default-400 cursor-pointer active:opacity-50">
                                <EyeIcon />
                            </span>

                        </Button>
                        <span className="text-lg text-default-400 cursor-pointer active:opacity-50">

                            <EditProductStockModal onProductUpdated={() => console.log("product modal")} productId={item.productId} machineId={item.machineId} stock={item.stock}/>
                            {/* <EditIcon /> */}
                        </span>
                        <span className="text-lg text-danger cursor-pointer active:opacity-50">
                            <DeleteIcon />
                        </span>
                    </div>
                );
            default:
                return cellValue;
        }
    }, []);


    return (
        <>
            <Table aria-label="Example static collection table">
                <TableHeader columns={columns}>
                    {(column) => <TableColumn key={column.key}>{column.label}</TableColumn>}
                </TableHeader>
                <TableBody items={machineProductsList} emptyContent={<Button as={Link} href={`/assign-products/${machineId}`} >Asignar products a esta maquina</Button>}>
                    {(item) => (
                        <TableRow key={item.productId}>
                            {(columnKey) => <TableCell>{renderCell(item, columnKey)}</TableCell>}
                        </TableRow>
                    )}
                </TableBody>
            </Table>
        </>
    )
}