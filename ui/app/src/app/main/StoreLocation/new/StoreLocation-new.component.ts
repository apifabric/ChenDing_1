import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'StoreLocation-new',
  templateUrl: './StoreLocation-new.component.html',
  styleUrls: ['./StoreLocation-new.component.scss']
})
export class StoreLocationNewComponent {
  @ViewChild("StoreLocationForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}