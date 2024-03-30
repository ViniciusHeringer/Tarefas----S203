import { Component, OnInit } from '@angular/core';
import { Movie } from './movie.model';
import { MovieService } from './movie.service';

@Component({
  selector: 'app-movielist',
  templateUrl: './movielist.component.html',
  styleUrls: ['./movielist.component.css']
})
export class MovieListComponent implements OnInit {

  movies: Movie[];

  constructor(private movieService: MovieService) { }

  ngOnInit(): void {
    this.movies = this.movieService.getMovies();
  }
}
