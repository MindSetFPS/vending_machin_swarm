
import { Table, TableHeader, TableColumn, TableBody, TableRow, TableCell, getKeyValue } from "@nextui-org/react";

export default function SalesTable({ salesList }) {
    console.log(salesList)
    const columns = [
        {
            key: "id",
            label: "id"
        },
        {
            key: "productId",
            label: "Product"
        },
        {
            key: "date",
            label: "Fecha"
        }, {
            key: "machineId",
            label: "Machine Id"
        }
    ]
    return (
        <Table aria-label="Example static collection table">
            <TableHeader columns={columns}>
                {(column) => <TableColumn key={column.key}>{column.label}</TableColumn>}
            </TableHeader>
            <TableBody items={salesList}>
                {(item) => (
                    <TableRow key={item.key}>
                        {(columnKey) => <TableCell>{getKeyValue(item, columnKey)}</TableCell>}
                    </TableRow>
                )}
            </TableBody>
        </Table>
    )
}