import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';
import Flashy from './ReactJSEssentials/lifecycles/mounting'
import FavoriteFoods from './ReactJSEssentials/Conditionals'
import TwoTextInputboxes from './ReactJSEssentials/Components/TwoTextInputBoxes'
import Basic_Form from './ReactJSEssentials/Components/Basic_Form'
import { Router, Route, IndexRoute, IndexRedirect, Link, hashHistory } from 'react-router'

//For routing, make sure that the home component, or any component, has {this.props.children} in their render function
//Check App.js for an example.
//Anything in IndexRoute component= will be passed as a children of App.

class Index extends React.Component{
    constructor(props){
        super(props);
        this.state = {
            greeting: 'f'
        };
        this.handleClick = this.handleClick.bind(this);
    }
    handleClick(name){
        this.setState({greeting: name});
        console.log("im here" + name + ' ' + this.state.greeting);
    }
    render(){
        return((
            <Router history={hashHistory}>
                <Route path="/" greeting={this.state.greeting} component={App} >
                    <IndexRedirect to="/login" />
                    <Route path="login" component={TwoTextInputboxes} />
                    <Route path="basicForm" component={()=>(<Basic_Form color="blue" onClick={this.handleClick} />)} />
                </Route>
            </Router>
        ));
    }
}

ReactDOM.render((
    <Index />),
    document.getElementById('root')
);
/*setTimeout(function () {
  ReactDOM.render(
    <App color='red'/>,
    document.getElementById('root')
  );
}, 2000);*/