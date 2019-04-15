import React from 'react';

import { Affix, Menu, Icon, Avatar  } from 'antd';

const SubMenu = Menu.SubMenu;
const MenuItemGroup = Menu.ItemGroup;

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
        <Affix>
            <Menu
            onClick={this.handleClick}
            selectedKeys={[this.state.current]}
            mode="horizontal"
          >
            <Menu.Item key="home">
              <Icon type="home" />Home
            </Menu.Item>
            <Menu.Item key="about">
              <Icon type="about" />About
            </Menu.Item>
            <Avatar size={24} icon="user" />
          </Menu>
        </Affix>
        );
    }
}