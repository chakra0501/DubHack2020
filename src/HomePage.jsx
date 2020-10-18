import React, {Component, useState} from "react";
import { useHistory } from "react-router-dom";
import styled from "styled-components";
import { Form, Input, Button, Checkbox } from 'antd';
import { UserOutlined, LockOutlined } from '@ant-design/icons';

const Margins = styled.div`
  margin: 100px;
  margin-left: 300px;
  margin-right: 300px;
`;

/*
function HomePage() {
  let history = useHistory();

  function handleClick() {
    history.push('/register');
  };

  return (
      <Margins>
        <h1>Login</h1>
        <button onClick={handleClick}>
          Register now!
        </button>
      </Margins>
    );
}
*/

function HomePage() {

  let history = useHistory();
  let [user, setUser] = useState("");

  let goToRegistration = () => {
    history.push("/register");
  };

  function goToProfile(event){
    console.log(user);
    
    fetch('http://127.0.0.1:5000/infoUser'+'?user='+user, 
      {
        method:"POST",
        cache: "no-cache",
        headers:{
            "content_type":"application/json",
        }, body:JSON.stringify({name : 'joy'})
        })
          .then(res => {
              console.log("Result:");
              console.log(res);
              return res.json();
            })
          .then((res) => 
              {
                console.log("Parsed return...");
                if (res.username){
                  history.push("/profile?user="+user);
                } else {
                  document.getElementById("Fail").textContent = "username or password incorrect"
                }
              },
              // Note: it's important to handle errors here
                // instead of a catch() block so that we don't swallow
              // exceptions from actual bugs in components.
              (error) => {
              });
  }

  let onFinish = (values) => {
      console.log('Received values of form: ', values)};
    
  //render() {
  return (
    <Margins>
      <h1>Login</h1>
        <Form
      name="normal_login"
      className="login-form"
      initialValues={{
          remember: true,
      }}
      onFinish={onFinish}
      >
          <Form.Item
              name="username"
              id="username"
              rules={[
              {
                  required: true,
                  message: 'Please input your Username!',
              }
              ]}
    >
                <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="Username"
                  onChange={(e) => {setUser(e.target.value);}}/>
    </Form.Item>
    {/* <Form.Item
      name="password"
      rules={[
        {
          required: true,
          message: 'Please input your Password!',
        },
      ]}
    >
      <Input
        prefix={<LockOutlined className="site-form-item-icon" />}
        type="password"
        placeholder="Password"
      />
    </Form.Item> */}
    <Form.Item>
      <Button onClick={goToProfile} type="primary" htmlType="submit" className="login-form-button">
        Log in
      </Button>
      <div id="Fail"></div>
    </Form.Item>
        </Form>
      <Button onClick={goToRegistration}>Register now!</Button>
    </Margins>
  );
  //}
}

export default HomePage;
