import React from 'react'
import Link from 'react-router/lib/Link'


class Basic_Form extends React.Component{

    constructor(props){
        super(props);
        this.state = {
            entry1: '',
            entry2: '',
            entry3: '',
            entry4: 'option4',
            data: {}
        };
        this.handleUserInput = this.handleUserInput.bind(this);
        this.handleChange= this.handleChange.bind(this);
        this.handleChecked = this.handleChecked.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    handleChange(e){
        this.setState({entry4: e.target.value});
    }
    handleUserInput(e){
        let name = e.target.name;

        this.setState({[name]: e.target.value});
    }
    handleChecked(e){
        this.setState({entry3: e.target.checked});
    }
    handleSubmit(){
        let temp = {
            entry1: this.state.entry1,
            entry2: this.state.entry2,
            entry3: this.state.entry3,
            entry4: this.state.entry4
        };
        this.setState({data: temp});

        this.props.onClick(this.state.entry1);
        console.log("pressed");
    }
    render(){
        return (
            <div>
                <form>
                    <label>Value for entry one: {JSON.stringify(this.state)} </label><br/>

                    <input name="entry1" onChange={this.handleUserInput} type="text" value={this.state.entry1}/><br/>
                    <label>Value for entry two: {this.state.entry2}</label><br/>
                    <input name="entry2" onChange={this.handleUserInput} type="text" value={this.state.entry2}/><br/>
                    <label>checked? {this.state.entry3.toString()}</label><br/>
                    <input name="entry3" type="checkbox" onClick={this.handleChecked} checked={this.state.entry3}/><br/>

                    <label>Currently selected item {this.state.entry4}</label><br/>
                    <select value={this.state.entry4} onChange={this.handleChange} >
                        <option value="option1">Option 1</option>
                        <option value="option2">Option 2</option>
                        <option value="option3">Option 3</option>
                        <option value="option4">Option 4</option>
                    </select>
                    <br/>
                    <Link to="/"><button onClick={this.handleSubmit} type="button">Submit</button></Link>
                </form>

                <label>This is the submitted result:</label><br />
                <p> {JSON.stringify(this.props) }</p>

                <div id="result"></div>
            </div>
        );
    }
}



export default Basic_Form;