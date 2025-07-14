import { Component, OnInit } from '@angular/core';
import { Router }            from '@angular/router';
import { ApiService, Task }  from '../../services/api.service';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.scss']
})
export class TaskListComponent implements OnInit {
  tasks: Task[] = [];

  constructor(private api: ApiService, private router: Router) {}

  ngOnInit(): void {
    this.api.listTasks().subscribe(data => this.tasks = data);
  }

  viewScore(id?: string) {
    if (id) this.router.navigate(['/tasks', id, 'score']);
  }
}
