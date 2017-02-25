import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import './index.css';
import Flashy from './ReactJSEssentials/lifecycles/mounting'
import FavoriteFoods from './ReactJSEssentials/Conditionals'
import TwoTextInputboxes from './ReactJSEssentials/Components/TwoTextInputBoxes'
import { Router, Route, IndexRoute, IndexRedirect, Link, hashHistory } from 'react-router'

//For routing, make sure that the home component, or any component, has {this.props.children} in their render function
//Check App.js for an example.
//Anything in IndexRoute component= will be passed as a children of App.


ReactDOM.render((
    <Router history={hashHistory}>
        <Route path="/" component={App} >
            <IndexRedirect to="login"/>
            <Route path="login" component={TwoTextInputboxes} />
            <Route path="welcome2" component={Flashy} />
            <Route path="about" component={App} />
        </Route>
  </Router>),
    document.getElementById('root')
);
/*setTimeout(function () {
  ReactDOM.render(
    <App color='red'/>,
    document.getElementById('root')
  );
}, 2000);*/