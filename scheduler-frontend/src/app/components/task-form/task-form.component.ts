import { Component }     from '@angular/core';
import { NgForm }        from '@angular/forms';
import { Router }        from '@angular/router';
import { ApiService, Task } from '../../services/api.service';

@Component({
  selector: 'app-task-form',
  templateUrl: './task-form.component.html',
  styleUrls: ['./task-form.component.scss']
})
export class TaskFormComponent {
  task: Task = {
    title: '',
    description: '',
    city: '',
    temp_min: 0,
    temp_max: 0,
    rain: false,
    wind: 0
  };

  constructor(private api: ApiService, private router: Router) {}

  onSubmit(form: NgForm) {
    if (form.valid) {
      this.api.createTask(this.task).subscribe(() => {
        this.router.navigate(['/tasks']);
      });
    }
  }
}
