import { MenuRootItem } from 'ontimize-web-ngx';

import { AddressCardComponent } from './Address-card/Address-card.component';

import { CustomerCardComponent } from './Customer-card/Customer-card.component';

import { EmployeeCardComponent } from './Employee-card/Employee-card.component';

import { FeedbackCardComponent } from './Feedback-card/Feedback-card.component';

import { InventoryCardComponent } from './Inventory-card/Inventory-card.component';

import { OrderCardComponent } from './Order-card/Order-card.component';

import { OrderDetailCardComponent } from './OrderDetail-card/OrderDetail-card.component';

import { PaymentCardComponent } from './Payment-card/Payment-card.component';

import { ProductCardComponent } from './Product-card/Product-card.component';

import { ShipmentCardComponent } from './Shipment-card/Shipment-card.component';

import { StoreLocationCardComponent } from './StoreLocation-card/StoreLocation-card.component';

import { SupplierCardComponent } from './Supplier-card/Supplier-card.component';


export const MENU_CONFIG: MenuRootItem[] = [
    { id: 'home', name: 'HOME', icon: 'home', route: '/main/home' },
    
    {
    id: 'data', name: ' data', icon: 'remove_red_eye', opened: true,
    items: [
    
        { id: 'Address', name: 'ADDRESS', icon: 'view_list', route: '/main/Address' }
    
        ,{ id: 'Customer', name: 'CUSTOMER', icon: 'view_list', route: '/main/Customer' }
    
        ,{ id: 'Employee', name: 'EMPLOYEE', icon: 'view_list', route: '/main/Employee' }
    
        ,{ id: 'Feedback', name: 'FEEDBACK', icon: 'view_list', route: '/main/Feedback' }
    
        ,{ id: 'Inventory', name: 'INVENTORY', icon: 'view_list', route: '/main/Inventory' }
    
        ,{ id: 'Order', name: 'ORDER', icon: 'view_list', route: '/main/Order' }
    
        ,{ id: 'OrderDetail', name: 'ORDERDETAIL', icon: 'view_list', route: '/main/OrderDetail' }
    
        ,{ id: 'Payment', name: 'PAYMENT', icon: 'view_list', route: '/main/Payment' }
    
        ,{ id: 'Product', name: 'PRODUCT', icon: 'view_list', route: '/main/Product' }
    
        ,{ id: 'Shipment', name: 'SHIPMENT', icon: 'view_list', route: '/main/Shipment' }
    
        ,{ id: 'StoreLocation', name: 'STORELOCATION', icon: 'view_list', route: '/main/StoreLocation' }
    
        ,{ id: 'Supplier', name: 'SUPPLIER', icon: 'view_list', route: '/main/Supplier' }
    
    ] 
},
    
    { id: 'settings', name: 'Settings', icon: 'settings', route: '/main/settings'}
    ,{ id: 'about', name: 'About', icon: 'info', route: '/main/about'}
    ,{ id: 'logout', name: 'LOGOUT', route: '/login', icon: 'power_settings_new', confirm: 'yes' }
];

export const MENU_COMPONENTS = [

    AddressCardComponent

    ,CustomerCardComponent

    ,EmployeeCardComponent

    ,FeedbackCardComponent

    ,InventoryCardComponent

    ,OrderCardComponent

    ,OrderDetailCardComponent

    ,PaymentCardComponent

    ,ProductCardComponent

    ,ShipmentCardComponent

    ,StoreLocationCardComponent

    ,SupplierCardComponent

];