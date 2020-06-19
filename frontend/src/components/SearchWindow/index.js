import React, { Component} from 'react';

import './style.css';

class SearchWindow extends Component {
  constructor(props){
    super(props);
    /*this.state = {
      //stateValue: this.props.stateValue,
      senators: this.props.senators
      //houseList: this.props.houseList
    };*/
  }

  generate_multi_senator_html(senatorDict, senatorList){
    for(var senatorID in senatorDict){
      var senatorData = senatorDict[senatorID];
      senatorList.push(this.generate_senator_html(senatorID, senatorData));
    }
    //console.log(this.props.senators)
  }
  generate_senator_html(sID, sData){
    var twitter_url = "https://twitter.com/" + sData["twitter"];
    return (
      <div key={sID}>
        <h2>{sData["name"]}</h2>
        <li>{sData["role"]}</li>
        <li>{sData["party"]}</li>
        <li><a href={twitter_url}>Twitter</a></li>
      </div>
    );
  }



  render() {
    var senList = [];
    this.generate_multi_senator_html(this.props.senators, senList);
    return(
      <div className="SearchWindow">
        {senList}
      </div>
    );
  }
}

export default SearchWindow;