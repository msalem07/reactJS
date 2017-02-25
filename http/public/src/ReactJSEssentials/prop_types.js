import React from 'react'

/*
    PropTypes are useful for two reasons:
        Prop Validation- Validation can ensure that your props are doing what they're supposed to be doing. If props
        are missing, or if they're present but they aren't what you're expecting, then a warning will print in the
        console.

        Documentation- Documenting props makes it easier to glance at a file and quickly understand the component class
        inside. When you have a lot of files, this can be a huge benefit.

        First step to making a propType is to search for a property named propTypes on the instructions object. If there
        isn't one, make one
        The name of each property in propTypes should be the name of an expected prop.
        The value of each property in propTypes should fit this patter: React.PropTypes.expected-data-type-goes-here


 */

var React = require('react');

var BestSeller = React.createClass({
    //By adding .isRequired to a propType, then you will get a console warning if that prop isn't sent.
    propTypes: {
        title: React.PropTypes.string.isRequired,
        author: React.PropTypes.string.isRequired,
        weeksOnList: React.PropTypes.number.isRequired

    },
    render: function(){
        return (
          <li>
              Title <span>
              {this.props.title}
          </span><br />
              Author: <span>
              {this.props.author}
          </span><br />
              Weeks: <span>
              {this.props.weeksOnList}
          </span>
          </li>
        );
    }

});

/*
    How could you write propTypes for a stateless functional component?
    To write propTypes for a stateless functional component, you define a propTypes object, as a property of the
    stateless functional component itself
 */

function GuineaPigs(props){
    var src = props.src;
    return (
        <div>
            <h1>Cute Guinea Pigs</h1>
            <img src={src} />
        </div>
    )
}

GuineaPigs.propTypes = {
    src:    React.PropTypes.string.isRequired
};

/*
    How about for a component written with ES6 class keyword
 */

class Hamsters extends React.Component{
    render(){
        var src = this.props.src;
        return (
            <div>
                <h1>Cute Guinea Pigs</h1>
                <img src={src} />
            </div>
        );
    }
}

Hamsters.propTypes ={
    src:    React.PropTypes.string.isRequired
}