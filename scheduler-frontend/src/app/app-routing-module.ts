import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { TaskListComponent }      from './components/task-list/task-list.component';
import { TaskFormComponent }      from './components/task-form/task-form.component';
import { WeatherScoreComponent }  from './components/weather-score/weather-score.component';

const routes: Routes = [
  { path: 'tasks',           component: TaskListComponent },
  { path: 'tasks/new',       component: TaskFormComponent },
  { path: 'tasks/:id/score', component: WeatherScoreComponent },
  { path: '', redirectTo: 'tasks', pathMatch: 'full' },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule {}
