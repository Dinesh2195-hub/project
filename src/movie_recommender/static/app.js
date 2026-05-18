const moviesElement = document.getElementById("movies");
const recommendationsElement = document.getElementById("recommendations");
const genreInput = document.getElementById("genre");
const likedMovieInput = document.getElementById("liked-movie");
const loadMoviesButton = document.getElementById("load-movies");
const loadRecommendationsButton = document.getElementById("load-recommendations");

async function fetchMovies() {
  const genre = genreInput.value;
  const url = new URL("/api/movies", window.location.origin);
  if (genre) url.searchParams.set("genre", genre);

  const response = await fetch(url.toString());
  return response.json();
}

async function fetchRecommendations() {
  const genre = genreInput.value;
  const likedMovie = likedMovieInput.value.trim();
  const url = new URL("/api/recommend", window.location.origin);
  if (genre) url.searchParams.set("genre", genre);
  if (likedMovie) url.searchParams.set("liked_movie", likedMovie);

  const response = await fetch(url.toString());
  return response.json();
}

function renderCards(items, container) {
  container.innerHTML = items
    .map(
      (movie) => `
      <article class="card">
        <h3>${movie.title}</h3>
        <div class="meta">
          <span>${movie.genre}</span>
          <span>${movie.year}</span>
          <span>★ ${movie.rating.toFixed(1)}</span>
        </div>
        <p>${movie.description}</p>
      </article>
    `,
    )
    .join("");
}

async function loadMovies() {
  const movies = await fetchMovies();
  renderCards(movies, moviesElement);
}

async function loadRecommendations() {
  const recommendations = await fetchRecommendations();
  renderCards(recommendations, recommendationsElement);
}

loadMoviesButton.addEventListener("click", loadMovies);
loadRecommendationsButton.addEventListener("click", loadRecommendations);

window.addEventListener("load", () => {
  loadMovies();
  loadRecommendations();
});
