import React from 'react'

/*
When you make a list in JSX, sometimes your list will need to include something called keys
key is a JSX attribute; React uses them internally to keep track of lists
 */

var List = React.createClass({

    getInitialState: function(){
        return {
            counter: 1,
            input:  '',
            myList: []
        }
    },
    //e because it takes the event of the input being filled
    handleInput: function(e) {
        var data = e.target.value;
        this.setState({input: data});
    },
    handleClick: function(){
      var data = this.state.myList;
      data.push(<li key={"entry_" + this.state.counter}>{this.state.input}</li>);

      this.setState({myList: data,input: '',counter: this.state.counter+1});

    },
    render: function () {

        return (
            <div>
                <h1>My List Values</h1>
                <ul>
                    {this.state.myList}
                </ul>
                <input type="text" value={this.state.input} onInput={this.handleInput} />
                <button onClick={this.handleClick}>Add Name to list</button>
            </div>
        );
    }
});

//or

class List2 extends React.Component{

    constructor(props){
        super(props);
        this.state = {
            myList: [],
            input:  '',
            counter: 1
        };
        this.handleInput = this.handleInput.bind(this);
        this.handleClick = this.handleClick.bind(this);
    }
    handleClick(){
        let data = this.state.myList;
        data.push(<li key={"entry_"+this.state.counter}>{this.state.input}</li>);
        this.setState({input:'',myList: data,counter: this.state.counter+1});
    }
    handleInput(e){
        let data = e.target.value;
        this.setState({input: data});
    }
    render(){

        return (
            <div>
                <h1>My List Values</h1>
                <ul>
                    {this.state.myList}
                </ul>
                <input type="text" value={this.state.input} onInput={this.handleInput} />
                <button onClick={this.handleClick}>Add Name to list</button>
            </div>
        );
    }
}

export default List2;