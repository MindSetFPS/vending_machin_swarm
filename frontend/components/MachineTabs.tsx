import { Tabs, Tab, Card, CardBody } from "@nextui-org/react";
import SalesTable from "./SalesTable";
import ProductsTable from "./ProductsTable";

export function MachineTabs({ sales, products }) {
    return (
        <div className="flex w-full flex-col">
            <Tabs aria-label="Options">
                <Tab key="sales" title="Sales">
                    <SalesTable salesList={sales} />
                </Tab>
                <Tab key="products" title="Products">
                    <ProductsTable machineProductsList={products} />
                </Tab>
            </Tabs>
        </div>
    );
}