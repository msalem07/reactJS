import React from 'react';

let SelectItems = React.createClass({

    people: ["Mariano","My Baby","What"],
    render: function(){
        const listNames = this.people.map(function(name) {
            return <option value={name}>{name}</option>;
        });
        return (
            <div>
                <select>
                    {listNames}
                </select>
            </div>
        );
    }
});

export default SelectItems;