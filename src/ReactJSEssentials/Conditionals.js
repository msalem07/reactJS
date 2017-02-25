import React from 'react'

var number = Math.random() < .5;

function FavoriteFoods(props){

    return (
        <div>
            <h1>Is the number greater than .5?</h1>
            { !number && <h2>No....</h2>}
            { number && <h2>Yes!</h2>}
        </div>
    )
}

export default FavoriteFoods;