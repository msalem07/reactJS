/*
A components state is not passed in from the outside. A component Decides its own state.
To make a component have state, write a getInitialState function

To read a component's state, use the expression this.state.name-of-property

To change a component's state call the function this.setState
 */
import React from 'react'

var Example = React.createClass({

    getInitialState: function (){
        return { mood: 'decent'}
    },
    toggleMood: function () {
      var newMood = this.state.mood === 'good' ? 'bad': 'good';
      this.setState({mood: newMood});
    },
    render: function() {
        return (
            <div>
                <div>I'm feeling {this.state.mood} </div>
                <button onClick={this.toggleMood}>Click Me</button>
            </div>
        )
    }
});

//or

class Example2 extends React.Component{

    constructor(props){
        super(props);
        this.state = {
            mood: 'decent'
        };
        this.toggleMood = this.toggleMood.bind(this);
    }
    toggleMood(){
        var newMood = this.state.mood === 'good' ? 'bad': 'good';
        this.setState({mood: newMood});
    }

    render(){
        return (
          <div>
              <div>I'm feeling {this.state.mood} </div>
              <button onClick={this.toggleMood}> Click Me</button>
          </div>
        );
    }
};

export default Example2;