/*
If you have a component class with nothing but a render function, then you can rewrite that component class in a very
different way. Instead of using React.createClass, you can write it as a JavaScript function.
A component class written as a function is called a stateless functional component.

//Stateless functional components usually have props passed to them. To access these props, give your stateless
functional component a parameter. This parameter will automatically be equal to the component's props object

 */

//A component class written in the usual way:
//Normal way to display props

var MyComponentClass = React.createClass({
   render: function(){
       return <h1>Hello World and hello {this.props.title}</h1>;
   }
});

//The same component class, written as a stateless functional component
//Stateless functional component way to display a prop:

function MyComponentClass2(props) {
    return <h1>Hello World and hello {props.title}</h1>;
}