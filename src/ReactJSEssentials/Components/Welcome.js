import React from 'react'


class Welcome extends React.Component{

    render(){
        return (
            <div>
                <h1>Welcome {this.props.params.username}</h1>
            </div>
        );
    }
}
export default Welcome;