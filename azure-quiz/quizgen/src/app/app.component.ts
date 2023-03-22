import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/internal/Observable';
import { FormGroup, FormControl } from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {
  myForm: FormGroup;

  title = 'quizgen';
  url = 'http://127.0.0.1:5000/content'

  questions = [
    {type: "name", description : "What is your name ?", isHidden:false},
    {type: "email", description : "What is your email ?", isHidden:true},
    {type: "message", description : "What is your message ?", isHidden:true}
  ]

  constructor(private http: HttpClient){}

  ngOnInit(){
    this.myForm = new FormGroup({
      name: new FormControl('Benedict'),
      email: new FormControl(''),
      message: new FormControl('')
    });
  }

  getAny(): Observable<any> {
    return this.http.get<any>(this.url); // request options as second parameter
  }
}