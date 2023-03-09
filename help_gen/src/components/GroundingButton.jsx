import React, { Component } from 'react';
import data from '../data/grounding.json'

export default class GroundingButton extends Component {

    constructor(props){
        super(props)
        this.state = {
            content: <p></p>
            // index:[Math.floor((Math.random()*data.length))]
        }
    }
    
    handleClick() {
        let newIndex = [Math.floor((Math.random()*data.length))];
        let newBody = data[newIndex]
        // this.setState({index:newIndex})
        this.setState({body:newBody})
    }

    render() {

        return (
            <div class="areaDiv" >
                <h1>Grounding tips</h1>
                <button style={{height:"50px", width:"50%"}} onClick={()=>this.handleClick()}> generate</button>
                <br/>
                <div dangerouslySetInnerHTML={{ __html: this.state.body }}></div>
            </div>
        )

    }
}