// URL de tu backend FastAPI
const API = 'http://localhost:8000';

async function loadTasks() {
  const ul = document.getElementById('task-list');
  ul.innerHTML = '<li class="list-group-item">Cargando…</li>';
  const tasks = await fetch(`${API}/tasks`).then(r => r.json());
  ul.innerHTML = '';
  tasks.forEach(t => {
    const li = document.createElement('li');
    li.className = 'list-group-item d-flex justify-content-between align-items-center';
    li.innerHTML = `
      <span>${t.title} (${t.city})</span>
      <button class="btn btn-sm btn-outline-secondary">Score</button>
    `;
    li.querySelector('button').onclick = () => showScore(t);
    ul.appendChild(li);
  });
}

document.getElementById('task-form').addEventListener('submit', async e => {
  e.preventDefault();
  const task = {
    title: document.getElementById('title').value,
    description: '',  // opcional
    city: document.getElementById('city').value,
    temp_min: +document.getElementById('temp_min').value,
    temp_max: +document.getElementById('temp_max').value,
    rain: document.getElementById('rain').checked,
    wind: +document.getElementById('wind').value,
  };
  await fetch(`${API}/tasks`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(task)
  });
  e.target.reset();
  document.getElementById('score-result').innerHTML = '';
  loadTasks();
});

async function showScore(task) {
  // obtenemos datos de clima
  const w = await fetch(`${API}/weather/${task.city}`)
    .then(r => r.json())
    .then(d => d.weather);

  // enviamos el task completo al endpoint /tasks/score
  const res = await fetch(`${API}/tasks/score`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(task)
  }).then(r => r.json());

  document.getElementById('score-result').innerHTML = `
    <h4>Score para "${task.title}"</h4>
    <p>Clima: ${w.condition}, ${w.temp}°C, viento ${w.wind} m/s</p>
    <p><strong>Puntuación: ${res.score}</strong></p>
    <button class="btn btn-secondary mt-2" onclick="loadTasks()">Volver a lista</button>
  `;
}

loadTasks();
