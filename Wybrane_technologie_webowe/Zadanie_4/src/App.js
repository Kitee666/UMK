import React, { Component } from 'react';
import './App.css';
import { Button } from './components/Button';
import { Input } from './components/Input';
import { ClearButton } from './components/ClearButton';
import * as math from 'mathjs';

class App extends Component {
  constructor(props) {
    super(props);

    this.state = {
      input: ""
    };
  }

  addToInput = value => {
    if (this.state.input === "Infinity" || this.state.input === "NaN" || this.state.input === "-Infinity" || this.state.input === "") {
      this.setState({input: value })
      return;
    }

    let i = 0;
    for (i = this.state.input.length - 1; i >= 0; i--) {
      if (isNaN(this.state.input[i])) {
        break;
      }
    }
    if (isNaN(value) && isNaN(this.state.input[this.state.input.length - 1]))
      return;
    if (value === "." && this.state.input[i] === ".")
      return;
    this.setState({input: this.state.input + value })
  };
  handleEqual = () => {
    if (this.state.input === "")
      return;
    if (this.state.input !== "" && isNaN(this.state.input[this.state.input.length - 1]))
      this.setState({input: math.evaluate(this.state.input.substr(0, this.state.input.length - 1).toString())});
    else
      this.setState({input: math.evaluate(this.state.input).toString()});
  }

  render() {
    return (
      <div className="app">
        <div className="calc-wrapper">
          <Input input={this.state.input}/>
          <div className="row">
            <Button handleClick={this.addToInput}>7</Button>
            <Button handleClick={this.addToInput}>8</Button>
            <Button handleClick={this.addToInput}>9</Button>
            <Button handleClick={this.addToInput}>/</Button>
          </div>
          <div className="row">
            <Button handleClick={this.addToInput}>4</Button>
            <Button handleClick={this.addToInput}>5</Button>
            <Button handleClick={this.addToInput}>6</Button>
            <Button handleClick={this.addToInput}>*</Button>
          </div>
          <div className="row">
            <Button handleClick={this.addToInput}>1</Button>
            <Button handleClick={this.addToInput}>2</Button>
            <Button handleClick={this.addToInput}>3</Button>
            <Button handleClick={this.addToInput}>+</Button>
          </div>
          <div className="row">
            <Button handleClick={this.addToInput}>.</Button>
            <Button handleClick={this.addToInput}>0</Button>
            <Button handleClick={() => this.handleEqual()}>=</Button>
            <Button handleClick={this.addToInput}>-</Button>
          </div>
          <div className="row">
            <ClearButton handleClear={() => this.setState({input: ""})}>
              Clear
            </ClearButton>
          </div>
        </div>
      </div>
    );
    }
}

export default App;
