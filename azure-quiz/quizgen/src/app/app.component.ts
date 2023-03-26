import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})

export class AppComponent {

  title = 'quizgen';
  mock_baseurl = 'https://137edb13-b1a9-49dd-b3a6-fc81f72953d8.mock.pstmn.io';
  baseurl = 'http://127.0.0.1:5000'
  content_url = this.baseurl + '/content'
  validate_url = this.baseurl + '/validate'
  content: any
  request: string = '';
  validationRequest: string[] = [];
  validationResponse: string[] = [];
  topic: string = '';

  constructor(private http: HttpClient) {}

  getQuestions() {
    if (this.topic.length == 0)
    {
      alert('Choose a topic')
      return
    }
    this.validationResponse = []
    this.getContent().subscribe(data => {
      this.content = data;
      console.log(data)
    });
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
    if (this.request.split(',').length < 3) {
      alert('Answer all the questions before submitting !')
      return
    }
    console.log(this.request)
    let body = new FormData();
    body.append('userresponse', this.request)
    this.http.post<any>(this.validate_url, body).subscribe(data => {
      console.log(data);
      this.validationResponse = data;
    }
    )
  }

  removeDuplicates(question: any) {
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
    let body = new FormData();
    body.append('topic', this.topic)
    return this.http.post<any>(this.content_url, body); // request options as second parameter
  }
}