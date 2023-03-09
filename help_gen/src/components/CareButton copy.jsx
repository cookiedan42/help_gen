import React, { Component } from 'react';
import data from '../data/selfcare.json'

export default class CareButton extends Component {

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
            <div class="areaDiv" >
                <h1>Self Care tips</h1>
                <button style={{height:"50px", width:"50%"}} onClick={()=>this.handleClick("low")}>low effort</button>
                <br/>
                <button style={{height:"50px", width:"50%"}} onClick={()=>this.handleClick("med")}>medium effort</button>
                <br/>
                <button style={{height:"50px", width:"50%"}} onClick={()=>this.handleClick("high")}>high effort</button>
                <br/>
                <div dangerouslySetInnerHTML={{ __html: this.state.body }}></div>
            </div>
        )

    }
}