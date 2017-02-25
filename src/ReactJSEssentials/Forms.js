/*
    A traditional form doesn't update the server until a user hits "submit." But you want to update the server any time
    a user enters or deletes any character
    You want to respond to any entered or deleted character in the <input /> field. The best way to do that is by
    listening for a "change" event on the <input />
 */

var React = require('react');

var Input = React.createClass({
    getInitialState: function(){
        return {
            userInput: ''
        }
    },
    handleUserInput: function(e){
        this.setState({userInput: e.target.value});
    },
    render: function(){
        return (
            <div>
                <input onChange={this.handleUserInput} value={this.state.userInput} type="text" />
                <h1>{this.state.userInput}</h1>
            </div>
        );
    }
});

export default Input;