import React from 'react'
import Link from 'react-router/lib/Link'

class NavBar extends React.Component{
    constructor(props){
        super(props);
        this.stylesA = {
            color:              '#FFFFFF',
            textDecoration:     'none',
            fontFamily:         'Open Sans, Verdana',
            fontSize:           '18px'
        };
        this.stylesUl = {
            listStyleType:      'none',
            margin:             '0',
            backgroundColor:    '#1e88e5'

        };
        this.stylesLi = {
            padding:            '16px 10%',
            margin:             '0 16px',
            display:            'inline-block',
            borderRadius:       '7px'
        }
        this.stylesDiv = {
            backgroundColor:    '#0d47a1',
            height:             '16px'
        }
    }

    render(){

        return (
            <div>
                <div id="filler" style={this.stylesDiv}></div>
                <div style={{backgroundColor: '#1e88e5',color: '#FFFFFF',fontSize: '32px', fontFamily: 'Open Sans'}}> My Vote </div>
                <ul style={this.stylesUl}>
                    <li style={this.stylesLi}><Link style={this.stylesA} to="welcome2">HOME</Link></li>
                    <li style={this.stylesLi}><Link style={this.stylesA} to="/about">HOME</Link></li>
                    <li style={this.stylesLi}><a style={this.stylesA} href="#">HOME</a></li>
                    <li style={this.stylesLi}><a style={this.stylesA} href="#">HOME</a></li>
                </ul>
            </div>
        );
    }
}

export default NavBar;