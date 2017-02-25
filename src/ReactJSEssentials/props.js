/*
* Every component has something called props.
* A component props is an object, it holds information about that component.
* To see a component's props object, you use the expression this.props
*
* There is a naming convention when naming props and the values passed.
* If you are listening for a 'click' event, then you should name your event handler
* handleClick, if 'keyPress' then name your event handler handleKeyPress... etc
*
* Your prop name should be the word on plus your event type. If you are listening for a 'click' event, then you name
* your prop onClick.
* */

import React from 'react';

/*
* Every component props object has a property named children. this.props.children will return everything in between a
* component's opening and closing JSX tags. If a component has more than one child between its JSX tags, then
* this.props.children will return those children in an array. However, if a component has only one child, then
* this.props.children will return the single child, not wrapped in an array
* */

var List = React.createClass({

   getDefaultProps: function(){
        return {children: ['ar','ra','y']}
   },
  render: function () {
    var titleText = 'Favorite ' + this.props.type;
    if (this.props.children instanceof Array) {
    	titleText += 's';
    }
    return (
        <div>
            <h1>{titleText}</h1>
            <ul>{this.props.children}</ul>
        </div>
    );
  }
});

//What if nobody passes any text to PropPasser. If nobody passes any text to PropPasser then Hello {this.props.name}
//will be blank. It would be better if PropPasser could display a default message instead.
//You can make this happen by writing a function named getDefaultProps whenever you use React.createClass like above
//Or if you're using class like below, set the member variable .defaultProps
class PropPasser extends React.Component{

    render() {
        //(1) This is how you display the information passed to the attribute name
        //(2) These are the children of List
        return (
            <div>
                <h1>(1) Hello {this.props.name}</h1>
                <List type='Living Musician'>
                    <li>(2) Sachiko M</li>
                    <li>(2) Harvey Sid Fisher</li>
                </List>
                <List type="Living Cat Musician">
                    <li>Nora The Piano Cat</li>
                </List>
            </div>
        );
    }
}

//Like this
PropPasser.defaultProps = {
    name: 'stranger'
};

class PropDisplayer extends React.Component{

    //You pass information to a React component by giving that component an attribute
    render(){
        return(
            <div>
                <PropPasser name="Mariano"/>
            </div>
        );
    }
}

export default PropDisplayer;