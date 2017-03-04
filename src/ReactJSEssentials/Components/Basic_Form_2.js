import React from 'react'

class FormContainer extends React.Component{

    constructor(props){

        super(props);
        this.state = {

            firstTextBox: {expectedValue: 'string'},
            secondTextBox: {expectedValue: 'phoneNumber'},
            thirdTextBox: {expectedValue: 'number'},
            firstCheckBox: {expectedValue: 'boolean'},
            firstOptionsBox: {text: 'option1',},
            firstRadioButton: {text: ''},

        };
        this.errorBoxStyle = {
            border: '2px solid red',
        };

        this.handleSubmit = this.handleSubmit.bind(this);
        this.validateSingleInput = this.validateSingleInput.bind(this);
    }

    //Sets the initial states with additional attributes,
    componentWillMount(){
        for (var state in this.state){
            //Set isValid to empty so that page doesn't start with errors
            this.setAttributes(state,'','empty',this.state[state].expectedValue);
        }
    }

    setAttributes(name, value, isValidInput, expectedValue){

        if(expectedValue === undefined){
            isValidInput = true;
        }

        let newData = {
            name: name,
            text: value,
            isValid: isValidInput,
            expectedValue: expectedValue
        };

        this.setState({[name]: newData});
    }

    //Validates all the inputs and returns an array of the states that are not valid
    validateInputs(){

        let invalidInputs = [];

        let currentState = this.state;

        for ( var prop in currentState) {

            if (currentState[prop].hasOwnProperty('isValid')){

                if( !currentState[prop].isValid || currentState[prop].isValid == 'empty'){
                    invalidInputs.push(currentState[prop]);
                }
            }
        }
        return invalidInputs;
    }

    //Validates state based on their expected value. If no expected value, then it's isValid attribute is set to true
    validateSingleInput(name, value) {

        let currentState = this.state[name];
        let isValidInput = 0;

        switch(currentState.expectedValue){

            case 'string':
                isValidInput = /.{5}/g.test(value);
                break;
            case 'number':
                isValidInput = /\d{5}/g.test(value);
                break;
            case 'phoneNumber':
                isValidInput = /(\d{3}-\d{3}-\d{4})$/g.test(value);
                break;
            case 'boolean':
                isValidInput = value;
                break;
            default:
                isValidInput = true;
                break;
        }

        this.setAttributes(name,value,isValidInput,currentState.expectedValue);
        return isValidInput;
    }

    handleSubmit(){

        let self = this;
        let invalidElements = [];
        let isFormValid = this.validateInputs();

        if (isFormValid.length === 0){
            this.props.router.push('/home/Mariano');
        }
        else {
            for(let i = 0; i < isFormValid.length; i++){

            }
        }
    }

    render(){

        return (
            <BasicForm2 errorBoxStyle={this.errorBoxStyle}
                        onChange={this.validateSingleInput}
                        onSubmit={this.handleSubmit}
                        {...this.state} />
        );
    }
}

class BasicForm2 extends React.Component{

    constructor(props){

        super(props);
        this.handleInput = this.handleInput.bind(this);
        this.getErrorStyle = this.getErrorStyle.bind(this);
    }
    getErrorStyle(){
        if (this.props.secondTextBox){
            return {border: '',}
        }
        return this.props.errorBoxStyle;
    }
    handleInput(e){

        let elementName = e.target.name;

        switch(e.target.type){

            case ('checkbox'):
                this.props.onChange(elementName,e.target.checked);
                break;
            default:
                this.props.onChange(elementName,e.target.value);
                break;
        }
    }

    render(){

        return (
            <div>
                <form>
                    <label>First Text Box: {this.props.firstTextBox.text} (Any character)</label>
                    <input style={this.getErrorStyle()} name="firstTextBox" onChange={this.handleInput} type="text" />
                    {!this.props.firstTextBox.isValid && <span>This field is not valid</span>}
                    <br/>

                    <label>Second Text Box: {this.props.secondTextBox.text} (phone Number)</label>
                    <input name="secondTextBox" onChange={this.handleInput} type="text" />
                    {!this.props.secondTextBox.isValid && <span>This field is not valid</span>}
                    <br/>

                    <label>Third Text Box: {this.props.thirdTextBox.text} (number)</label>
                    {this.props.thirdTextBox.isValid ? (
                            <input name="thirdTextBox" onChange={this.handleInput} type="text" />
                        ):(
                            <input style={this.props.errorBoxStyle} name="thirdTextBox" onChange={this.handleInput} type="text" />
                        )
                    }
                    {!this.props.thirdTextBox.isValid && <span>This field is not valid</span>}
                    <br/>

                    <label>Third Text Box: {this.props.firstCheckBox.text} (checkbox //If you need it required)</label>
                    <input name="firstCheckBox" onClick={this.handleInput} type="checkbox"/>
                    {!this.props.firstCheckBox.isValid && <span>This field is not valid</span>}
                    <br/>

                    <select name="firstOptionsBox" value={this.props.firstOptionsBox.text} onChange={this.handleInput}>
                        <option value="option1">Options Usually</option>
                        <option value="option2">Do not need to </option>
                        <option value="option3">be validated </option>
                    </select>

                    <div>
                        <label>Option 1</label>
                        <input type="radio" name="firstRadioButton" value="option1" onClick={this.handleInput}/>
                        <br/>

                        <label>Option 2</label>
                        <input type="radio" name="firstRadioButton" value="option2" onClick={this.handleInput}/>
                        <br/>

                        <label>Option 3</label>
                        <input type="radio" name="firstRadioButton" value="option3" onClick={this.handleInput}/>
                        <br/>

                    </div>
                    <h1>{this.props.testProp}</h1>
                    <button name="submitButton" type="button" onClick={this.props.onSubmit}>Submit Form</button>
                </form>
            </div>
        );
    }

}


export default FormContainer;