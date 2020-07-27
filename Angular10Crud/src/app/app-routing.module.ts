import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { SnippetListComponent } from './components/snippet-list/snippet-list.component';

const routes: Routes = [
  { path: '', redirectTo: 'snippets', pathMatch: 'full' },
  { path: 'snippets', component: SnippetListComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
