import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { StoreLocationHomeComponent } from './home/StoreLocation-home.component';
import { StoreLocationNewComponent } from './new/StoreLocation-new.component';
import { StoreLocationDetailComponent } from './detail/StoreLocation-detail.component';

const routes: Routes = [
  {path: '', component: StoreLocationHomeComponent},
  { path: 'new', component: StoreLocationNewComponent },
  { path: ':id', component: StoreLocationDetailComponent,
    data: {
      oPermission: {
        permissionId: 'StoreLocation-detail-permissions'
      }
    }
  }
];

export const STORELOCATION_MODULE_DECLARATIONS = [
    StoreLocationHomeComponent,
    StoreLocationNewComponent,
    StoreLocationDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class StoreLocationRoutingModule { }