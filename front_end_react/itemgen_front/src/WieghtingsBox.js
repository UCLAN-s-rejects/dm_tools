import React, { Component } from 'react';
import {Endpoint} from './constants';

export default class Wieghtingsbox extends Component {
    constructor(props) {
        super(props);
        this.state = {
            lowval: "",
            medval: "",
            highval: "",
            vhighval: "",
            returnval:""
        };
        this.inputupdater=this.inputupdater.bind(this)
    }
    postform = () => {
        let url=`${Endpoint}/test`;
        let posty = new XMLHttpRequest();
        posty.responseType="json"
        posty.open("post",url);
        posty.setRequestHeader("Content-Type", "application/json");
        posty.setRequestHeader("Accept", "application/json;charset=UTF-8");
        let postbody = {"weightings":{
            low: this.state.lowval,
            med: this.state.medval,
            high:this.state.highval,
            vhigh:this.state.vhighval
        }}
        postbody.onload=()=>{
            this.setState({
                returnval:postbody.response
            })
        }
        postbody = JSON.stringify(postbody);
        console.log(postbody)
        posty.send(postbody);
    }
    handleform = (event) => {
        event.preventDefault()
    }
    inputupdater = (event) => {
        event.preventDefault();
        this.setState({
            [event.target.name]: event.target.value
            
        })
    }
    render() {
        return (
            <div><p>show state</p>
                <p> {this.state.lowval} </p>
                <form id="frm1" onSubmit={this.handleform}>
                    low value weighting:<input type="number" name="lowval" className="inputfield" onChange={this.inputupdater} />
                    <br />
                    mid value weighting:<input type="number" name="medval" className="inputfield" onChange={this.inputupdater}/>
                    <br />
                    high value weighting<input type="number" name="highval" className="inputfield" onChange={this.inputupdater}/>
                    <br />
                    very high value weighting:<input type="number" name="vhighval" className="inputfield" onChange={this.inputupdater} />
                    <br />
                </form>
                <button onClick={this.postform}>click here</button>
                <div>
                {this.state.returnval}
            </div>
            </div>
            
        )
    }
}