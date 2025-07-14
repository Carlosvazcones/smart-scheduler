import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

export interface Task {
  id?: string;
  title: string;
  description: string;
  city: string;
  temp_min: number;
  temp_max: number;
  rain: boolean;
  wind: number;
}

export interface Weather {
  temp: number;
  wind: number;
  condition: string;
}

@Injectable({ providedIn: 'root' })
export class ApiService {
  private baseUrl = 'http://localhost:8000';  // ajusta si tu backend corre en otra URL

  constructor(private http: HttpClient) {}

  listTasks(): Observable<Task[]> {
    return this.http.get<Task[]>(`${this.baseUrl}/tasks`);
  }

  createTask(task: Task): Observable<Task> {
    return this.http.post<Task>(`${this.baseUrl}/tasks`, task);
  }

  getWeather(city: string): Observable<{ weather: Weather }> {
    return this.http.get<{ weather: Weather }>(
      `${this.baseUrl}/weather/${city}`
    );
  }

  scoreTask(payload: {
    prefs: Task;
    weather: Weather;
  }): Observable<{ score: number }> {
    return this.http.post<{ score: number }>(
      `${this.baseUrl}/tasks/score`,
      payload
    );
  }
}
