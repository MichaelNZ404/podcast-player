import React, { Component } from 'react';
import headphones from './headphones-static.svg';
import './App.css';

import Loader from './components/loader';
import Library from './components/Library';
import { BrowserRouter as Router, Route, Link } from "react-router-dom";

import {
  Layout, Menu,
} from 'antd';

const {
  Header, Content, Footer,
} = Layout;

class App extends Component {
  state = {
    collapsed: false,
  };

  onCollapse = (collapsed) => {
    console.log(collapsed);
    this.setState({ collapsed });
  }

 render() {
    return (
      <Router>
        <Layout className="layout">
          <Header>
            <img src={headphones} style={{float: "left", marginTop: "7px"}} alt="logo" />
            <Menu
              theme="dark"
              mode="horizontal"
              defaultSelectedKeys={['home']}
              style={{ lineHeight: '64px' }}
            >
              <Menu.Item key="home" className="red"><Link to="/">Home</Link></Menu.Item>
              <Menu.Item key="about" className="red"><Link to="/about/">About</Link></Menu.Item>
            </Menu>
          </Header>
          <Content style={{ padding: '0 50px' }}>
            <Route path="/" exact component={Library} />
            <Route path="/about/" component={Loader} />
          </Content>
          <Footer style={{ textAlign: 'center' }}>
            Podsync ©2019 Created by Michael Coleman
          </Footer>
        </Layout>
      </Router>
    );
  }
}

export default App;
