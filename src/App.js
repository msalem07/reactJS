import React, { Component } from 'react';
import logo from './logo.svg';
import './App.css';
import NavBar from './ReactJSEssentials/Components/NavBar'

class App extends Component {

  componentWillReceiveProps(nextProps){
    console.log(nextProps);
  }

  render() {
    return (
      <div className="App">
          <NavBar greeting={this.props.route.greeting}/>
          {this.props.children}
      </div>
    );
  }
}

export default App;
