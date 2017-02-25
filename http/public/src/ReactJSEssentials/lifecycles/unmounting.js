/*
    A component's unmounting period occurs when the component is removed from the DOM. This could happen if the DOM is
    rendered without the component, or if the user navigates to a different website or closes their web browser.

    componentWillUnmount is the only unmounting lifecycle method
 */

var React = require('react');
var ReactDOM = require('react-dom');

var App = React.createClass({
  getInitialState: function () {
    return {
      enthused: false,
      text: ''
    };
  },

  toggleEnthusiasm: function () {
    this.setState({
      enthused: !this.state.enthused
    });
  },

  setText: function (text) {
    this.setState({ text: text });
  },

  addText: function (newText) {
    var text = this.state.text + newText;
    this.setState({ text: text });
  },

  handleChange: function (e) {
    this.setText(e.target.value);
  },

  render: function () {
    var button;
    if (this.state.enthused) {
      button = (
        <Enthused
          toggle={this.toggleEnthusiasm}
          addText={this.addText} />
      );
    } else {
        //This block removes our Enthused component and replaces it for a regular button
        //This in turn dismounts Enthused from our application
      button = (
        <button
          onClick={this.toggleEnthusiasm}>
          Add Enthusiasm!
        </button>
      );
    }

    return (
      <div>
        <h1>Auto-Enthusiasm</h1>
        <textarea
          rows="7"
          cols="40"
          value={this.state.text}
          onChange={this.handleChange}>
        </textarea>
        {button}
        <h2>{this.state.text}</h2>
      </div>
    );
  }
});

ReactDOM.render(
  <App />,
  document.getElementById('app')
);

var Enthused = React.createClass({
  interval: null,

  componentDidMount: function () {
    this.interval = setInterval(function(){
      this.props.addText('!');
    }.bind(this), 15);
  },
	componentWillUnmount: function(prevProps, prevState){
    clearInterval(this.interval);
  },
  render: function () {
    return (
      <button onClick={this.props.toggle}>
        Stop!
      </button>
    );
  }
});