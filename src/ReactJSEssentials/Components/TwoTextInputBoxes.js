import React from 'react'
import Link from 'react-router/lib/Link'
import hashHistory from 'react-router'

class TwoTextInputBoxes extends React.Component{

    constructor(props){
        super(props);
        this.state = {
            username: '',
            password: ''
        }
        this.styleDiv = {
            marginTop:  '200px'
        };
        this.styleInput = {
            minWidth:       '300px',
            minHeight:      '25px',
            marginBottom:   '16px',
            borderRadius:   '4px',
            fontSize:       '20px',
            background:     '#f0f0f0'
        };
        this.styleLabel = {
            fontWeight:      'bold',
            fontFamily:     'Open Sans',
            fontSize:       '24px'
        };
        this.styleButton = {
            width:          '200px',
            margin:         '16px',
            height:         '30px',
            fontFamily:     'Open Sans',
            borderRadius:   '4px',
            backgroundColor:'orange'
        }
        this.handleUserInput = this.handleUserInput.bind(this);
        this.handleClick = this.handleClick.bind(this);
    }
    handleUserInput(e){
        let name = e.target.name;

        this.setState({[name]: e.target.value});
    }
    handleClick(){
        alert('username: ' + this.state.username);
        alert('password: ' + this.state.password);
        let answer = prompt('Yes?:');
        if(answer.toLowerCase() == 'yes') {
            //Apparently the new way to navigate to a new link
            this.props.router.push('home/'+this.state.username);
        }

    }
    render(){

        return (
            <div style={this.styleDiv}>
                <label style={this.styleLabel}> Username:</label><br/>
                <input style={this.styleInput} onChange={this.handleUserInput} name="username" type="text" /><br/>
                <label style={this.styleLabel}>Password:</label><br/>
                <input style={this.styleInput} onChange={this.handleUserInput} type="password" name="password" /><br/>

                <div >
                    <div style={{display: 'inline-block', margin: '0px 15px'}}>
                        <input type="checkbox"/><label>Remember Me?</label>
                    </div>
                    <div style={{display: 'inline-block', margin: '0px 15px'}}>
                        <Link to="#">Forgot Password?</Link>
                    </div>

                </div>
                <button style={this.styleButton} onClick={this.handleClick} type="button">Log In</button>
            </div>
        );
    }

}

export default TwoTextInputBoxes;