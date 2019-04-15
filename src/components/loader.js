import React from 'react';
import headphonesLoading from '../headphones.svg';

export default class Navigation extends React.Component {
    state = {
      current: 'home',
    }
    
    handleClick = (e) => {
        console.log('click ', e);
        this.setState({
            current: e.key,
        });
    }
    
    render() {
        return (
            <div style={{margin: '80px 0px'}}>
                <img src={headphonesLoading} style={{margin: 'auto', display: 'block'}} alt="logo" />
                <div style={{textAlign: 'center'}}>Loading...</div>
            </div>
        );
    }
}