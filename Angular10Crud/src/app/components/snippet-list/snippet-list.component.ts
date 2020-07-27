import { Component, OnInit } from '@angular/core';
import { SnippetService } from 'src/app/services/snippet.service';

@Component({
  selector: 'app-snippet-list',
  templateUrl: './snippet-list.component.html',
  styleUrls: ['./snippet-list.component.css']
})
export class SnippetListComponent implements OnInit {

  snippets: any;
  currentSnippet = null;
  currentIndex = -1;
  title = '';

  constructor(private snippetService: SnippetService) { }

  ngOnInit(): void {
    this.retrieveSnippets();
  }

  retrieveSnippets(): void {
    this.snippetService.getAll()
      .subscribe(
        data => {
          this.snippets = data;
          console.log(data);
        },
        error => {
          console.log(error);
        });
  }

  refreshList(): void {
    this.retrieveSnippets();
    this.currentSnippet = null;
    this.currentIndex = -1;
  }

}
