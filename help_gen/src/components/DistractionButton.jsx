import React, { Component } from 'react';
import data from '../data/distraction.json'

export default class DistractionButton extends Component {

    constructor(props){
        super(props)
        this.state = {
            content: <p></p>
        }
    }
    
    handleClick(key) {
        let newIndex = [Math.floor((Math.random()*data[key].length))];
        let newBody = data[key][newIndex]
        this.setState({body:newBody})
    }

    render() {

        return (
            <div class="areaDiv" style={{flexDirection:"row"}}>

                <h1>Distraction tips</h1>
                <button style={{height:"50px", width:"25%", minWidth:"200px"}} onClick={()=>this.handleClick("low")}>low effort</button>
                <button style={{height:"50px", width:"25%", minWidth:"200px"}} onClick={()=>this.handleClick("med")}>medium effort</button>
                <button style={{height:"50px", width:"25%", minWidth:"200px"}} onClick={()=>this.handleClick("high")}>high effort</button>
                <div dangerouslySetInnerHTML={{ __html: this.state.body }}></div>
            </div>
        )

    }
}