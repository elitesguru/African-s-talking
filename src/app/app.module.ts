import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import { KYCFormComponent } from './components/kyc-form/kyc-form.component';

@NgModule({
  declarations: [
    AppComponent,
    KYCFormComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
