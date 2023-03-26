import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs/internal/Observable';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent implements OnInit {

  title = 'quizgen';
  baseurl = 'https://137edb13-b1a9-49dd-b3a6-fc81f72953d8.mock.pstmn.io';
  content_url = this.baseurl + '/content'
  validate_url = this.baseurl + '/validate'
  content: any
  request: string = '';
  validationRequest: string[] = [];
  validationResponse: string[] = [];
  
  constructor(private http: HttpClient) {

  }

  ngOnInit() {
    this.getContent().subscribe(data => {
      this.content = data;
      console.log(data)
    }
    );
  }

  onItemChange(value: any) {
    var selectedItem = value.value;
    var question = selectedItem.split('-')[0];
    if (this.validationRequest.length == 0) {
      this.validationRequest.push(selectedItem)
    }
    else {
      this.removeDuplicates(question)
      this.validationRequest.push(selectedItem)
    }
    this.request = this.validationRequest.join(',')
  }

  submit() {
    if(this.request.split(',').length<3){
      alert('Answer all the questions before submitting !')
      return
    }
    console.log(this.request)
    this.http.post<any>(this.validate_url, this.request).subscribe(data => {
        console.log(data);
        this.validationResponse = data;
      }
    )
  }

  removeDuplicates(question: any){
    for (var key of this.validationRequest) {
      var q = key.split('-')[0]
      if (q === question) {
        const index = this.validationRequest.indexOf(key, 0);
        if (index > -1) {
          this.validationRequest.splice(index, 1);
        }
      }
    }
  }


  getContent() {
    return this.http.post<any>(this.content_url, "app service"); // request options as second parameter
  }
}