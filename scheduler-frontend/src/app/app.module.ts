import { NgModule }           from '@angular/core';
import { BrowserModule }      from '@angular/platform-browser';
import { FormsModule }        from '@angular/forms';
import { HttpClientModule }   from '@angular/common/http';    // ← IMPORT

import { AppRoutingModule }   from './app-routing-module';
import { AppComponent }       from './app.component';
import { TaskFormComponent }  from './components/task-form/task-form.component';
import { TaskListComponent }  from './components/task-list/task-list.component';
import { WeatherScoreComponent } from './components/weather-score/weather-score.component';

@NgModule({
  declarations: [
    AppComponent,
    TaskFormComponent,
    TaskListComponent,
    WeatherScoreComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,        // ← DESCOMENTADO / AÑADIDO
    AppRoutingModule
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
