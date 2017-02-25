/*
    The first time that a component instance renders, it does not update. A component updates every time that it
    renders, starting with the second render

    There are five updating lifecycle methods:
        componentWillReceiveProps   only gets called if the component will receive props. componentWillReceiveProps gets
                                    passed one argument: an object called nextProps. nextProps is a preview of the
                                    upcoming props object that the component is about to receive
        shouldComponentUpdate       automatically receives two arguments: nextProps and nextState. It's typical to
                                    compare nextProps and nextState to the current this.props and this.state, and use
                                    the result to decide what to do. shouldComponentUpdate should return either true
                                    or false. If true nothing noticeable happens; if false component will not update and
                                    none of the remaining lifecycles will be called.
        componentWillUpdate         The main purpose of componentWillUpdate is to interact with things outside of the
                                    React architecture. If you need to do non-React setup before a component renders,
                                    such as checking the window size or interacting with an API
        render
        componentDidUpdate          gets passed two arguments: prevProps and prevState which are references to the
                                    components props and state before the current updating period began. Similar use
                                    like componentWillUpdate but after render
 */
var React = require('react');
var ReactDOM = require('react-dom');
var yellow = 'rgb(255, 215, 18)';

var TopNumber = React.createClass({
    propTypes: {
        number: React.PropTypes.number,
        game: React.PropTypes.bool
    },
    getInitialState: function () {
        return { 'highest': 0 };
    },
    componentWillReceiveProps: function(nextProps){
        if ( nextProps.number > this.state.highest) {
            this.setState({highest: nextProps.number});
        }
    },
    componentWillUpdate: function(){
        if (document.body.style.background != 'rgb(255, 215, 18)' && this.state.highest >= 950*1000) {
            document.body.style.background = 'rgb(255, 215, 18)';
        }
        else if (!this.props.game && nextProps.game) {
            document.body.style.background = 'white';
        }
    },
    componentDidUpdate: function(prevProps, prevState){
        if (this.state.latestClick < prevState.latestClick){
            this.endGame();
        }
    },
    render: function () {
        return (
        <h1>
            Top Number: {this.state.highest}
        </h1>
        );
    }
});

var Target = React.createClass({
  propTypes: {
    number: React.PropTypes.number.isRequired
  },
	shouldComponentUpdate: function(nextProps, nextState){
    return this.props.number != nextProps.number;
  },
  render: function () {
    var visibility = this.props.number
      ? 'visible' : 'hidden';
    var style = {
      position: 'absolute',
      left: random(100) + '%',
      top:  random(100) + '%',
      fontSize: 40,
      cursor: 'pointer',
      visibility: visibility
    };

    return (
      <span
        style={style}
        className="target" >
        {this.props.number}
      </span>
    )
  }
});
