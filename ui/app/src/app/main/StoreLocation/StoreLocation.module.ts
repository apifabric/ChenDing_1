import {CUSTOM_ELEMENTS_SCHEMA, NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { OntimizeWebModule } from 'ontimize-web-ngx';
import { SharedModule } from '../../shared/shared.module';
import  {STORELOCATION_MODULE_DECLARATIONS, StoreLocationRoutingModule} from  './StoreLocation-routing.module';

@NgModule({

  imports: [
    SharedModule,
    CommonModule,
    OntimizeWebModule,
    StoreLocationRoutingModule
  ],
  declarations: STORELOCATION_MODULE_DECLARATIONS,
  exports: STORELOCATION_MODULE_DECLARATIONS,
  schemas: [CUSTOM_ELEMENTS_SCHEMA]
})
export class StoreLocationModule { }