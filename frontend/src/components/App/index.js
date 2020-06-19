import React, { Component } from 'react';
import SearchWindow from '../SearchWindow';
import { getReps } from '../../api.js';
import { STATE_ABBRS } from '../../constants.js';

import './style.css';


class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      stateValue: 'Any',
      senators: {},
    };
    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event){
    this.setState({state: event.target.value});
    this.updateReps(event.target.value);
  }

  handleSubmit(event){
  }

  updateReps = (state) => {
    /** Query backend for representatives related to the given state
      Input: State (and soon county / District) 
      Output: new set of rep info to pass to SearchWindow*/

    if (state == "Any"){
      return;
    }
    getReps(state)
      .then(response => {
        this.setState({senators: response['data']['senators']});
      })
      .catch(function (error) {
        console.log(error);
      });
  }

  generate_multi_state(){
    return STATE_ABBRS.map((sAbbr) => this.generate_state(sAbbr))
  }
  generate_state(abbr){
    return (
      <option value={abbr}>{abbr}</option>
    );
  }

  render() {
    var sAbbrList = this.generate_multi_state();
    return (
      <div className="App">
        <header className="App-header">
          <label>
            <select value={this.state.stateValue} onChange={this.handleChange}>
              <option value="Any">Any</option>
              {sAbbrList}
            </select>
          </label>
          <SearchWindow senators={this.state.senators}/>
        </header>
      </div>
    );
  }
}







/*class DropDown extends Component{
  constructor(props){
    super(props){
      this.state = {value};
    }
  }

  render(){
    <select value=this.stateValue onChange={this.handleChange}>
      <option value="Any"/>
      <option value="MI"/>
    </select>
  }
}*/

export default App;








/*
<img src={logo} className="App-logo" alt="logo" />
<p>
  Edit <code>src/App.js</code> and save to reload.
</p>
<a
  className="App-link"
  href="https://reactjs.org"
  target="_blank"
  rel="noopener noreferrer"
>
  Learn React
</a>
*/
