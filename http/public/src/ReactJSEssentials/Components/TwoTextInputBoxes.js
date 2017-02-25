import React from 'react'
import Link from 'react-router/lib/Link'

class TwoTextInputBoxes extends React.Component{

    constructor(props){
        super(props);
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
    }
    render(){

        return (
            <div style={this.styleDiv}>
                <label style={this.styleLabel}> Username:</label><br/>
                <input style={this.styleInput} type="text" /><br/>
                <label style={this.styleLabel}>Password:</label><br/>
                <input style={this.styleInput} type="password" /><br/>

                <div >
                    <div style={{display: 'inline-block', margin: '0px 15px'}}>
                        <input type="checkbox"/><label>Remember Me?</label>
                    </div>
                    <div style={{display: 'inline-block', margin: '0px 15px'}}>
                        <Link to="#">Forgot Password?</Link>
                    </div>

                </div>
                <button style={this.styleButton} type="button">Log In</button>
            </div>
        );
    }

}

export default TwoTextInputBoxes;