import { Component, OnInit } from '@angular/core';
import { ActivatedRoute }     from '@angular/router';
import { ApiService, Task, Weather } from '../../services/api.service';

@Component({
  selector: 'app-weather-score',
  templateUrl: './weather-score.component.html',
  styleUrls: ['./weather-score.component.scss']
})
export class WeatherScoreComponent implements OnInit {
  task!: Task;
  weather!: Weather;
  score!: number;

  constructor(private api: ApiService, private route: ActivatedRoute) {}

  ngOnInit(): void {
    const id = this.route.snapshot.params['id'];
    this.api.listTasks().subscribe(tasks => {
      this.task = tasks.find(t => t.id === id)!;
      this.api.getWeather(this.task.city).subscribe(res => {
        this.weather = res.weather;
        this.api.scoreTask({ prefs: this.task, weather: this.weather })
          .subscribe(r => this.score = r.score);
      });
    });
  }
}
