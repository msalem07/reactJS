/*
    There are three categories of lifecycle methods: mounting, updating, and unmounting.

    A component "mounts" when it renders for the first time. This is when mounting lifecycle methods get called.

    There are three mounting lifecycle methods:
        componentWillMount  gets called when a component renders for the first time
        render              gets called when a component a component is mounter or updated
        componentDidMount   gets called when a component renders for the first time
                            If your React app uses AJAX to fetch initial data, then this is the place to make that call
                            Also best place to set timers using setTimeouts or setIntervals

        When a component mounts, it automatically calls these three methods, in order
 */

import React from 'react';
import ReactDOM from "react-dom";

var Flashy = React.createClass({
    componentWillMount: function(){
        alert('AND NOW, FOR THE FIRST TIME EVER... FLASHY!!!');
        alert('Flashy is rendering!');

    },
    componentWillReceiveProps: function(nextProps){
        alert('My new prop is now ' + nextProps.color);
    },
    shouldComponentUpdate(nextProps, nextState){
      var entry = prompt("Should I change to " + nextProps.color + '?');
      if (entry.toLowerCase() === 'yes') {
          return true;
      }
      else
          return false;
    },
    render: function() {

        return (
            <h1 style={{color: this.props.color}}>
                OOH LA LA LOOK AT ME I AM THE FLASHIEST {this.props.color}
            </h1>
        );
    }
});

export default Flashy;