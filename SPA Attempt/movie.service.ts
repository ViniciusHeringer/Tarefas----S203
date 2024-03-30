import { Injectable } from '@angular/core';
import { Movie } from './movie.model';

@Injectable({
  providedIn: 'root'
})
export class MovieService {

  private movies: Movie[] = [
    new Movie('Filme 1', 'Ação'),
    new Movie('Filme 2', 'Comédia'),
    new Movie('Filme 3', 'Drama')
  ];

  constructor() { }

  getMovies(): Movie[] {
    return this.movies;
  }
}
