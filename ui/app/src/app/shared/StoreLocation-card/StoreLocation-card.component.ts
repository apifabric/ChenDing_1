import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './StoreLocation-card.component.html',
  styleUrls: ['./StoreLocation-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.StoreLocation-card]': 'true'
  }
})

export class StoreLocationCardComponent {


}