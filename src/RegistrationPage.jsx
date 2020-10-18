import React, {useState} from "react";
import { Form, Input, Button, Select } from "antd";
import styled from "styled-components";
import { useHistory } from "react-router-dom";
import {UserOutlined} from "@ant-design/icons";

const { TextArea } = Input;

const Margins = styled.div`
  margin: 100px;
  margin-left: 300px;
  margin-right: 300px;
`;

function RegistrationPage() {
  let history = useHistory();
  let [first, setFirst] = useState('');
  let [last, setLast] = useState('');
  let [user, setUser] = useState('');
  let [email, setEmail] = useState('');
  let [gender, setGender] = useState('');
  let [age, setAge] = useState('');
  let [work, setWork] = useState('');
  let [loc, setLoc] = useState('');
  let [about, setAbout] = useState('N/A');

  let findBuddies = () => {
    history.push("/matching");
  };

  let onFinish = (values) => {
    findBuddies();
  };
  let onFinishFailed = (errorInfo) => {};

  function newProfile(event){
    console.log(user);
    
    fetch('http://127.0.0.1:5000/newUser?'+'user='+user+'&gender='+gender+'&loc='+loc+'&work='+work+'&age='+age+'&about='+about+'&email='+email+'&first='+first+'&last='+last, 
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
                if (res == "Success"){
                  history.push("/profile?user="+user);
                } else {
                  document.getElementById("Fail").textContent = "Not Enough Details Filled"
                }
              },
              // Note: it's important to handle errors here
                // instead of a catch() block so that we don't swallow
              // exceptions from actual bugs in components.
              (error) => {
              });
  }

  return (
    <Margins>
      <h1>Registration</h1>
      <Form
        name="basic"
        initialValues={{ remember: true }}
        onFinish={onFinish}
        onFinishFailed={onFinishFailed}
      >
        <Form.Item
          label="First name"
          name="firstname"
          rules={[{ required: true, message: "Please input your first name!" }]}
        >
          <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="FirstName"
            onChange={(e) => {setFirst(e.target.value);}}/>
        </Form.Item>

        <Form.Item
          label="Last name"
          name="lastname"
          rules={[{ required: true, message: "Please input your last name!" }]}
        >
          <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="LastName"
            onChange={(e) => {setLast(e.target.value);}}/>
        </Form.Item>

        <Form.Item
          label="Username"
          name="username"
          rules={[{ required: true, message: "Please input your username!" }]}
        >
          <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="user"
            onChange={(e) => {setUser(e.target.value);}}/>
        </Form.Item>

        <Form.Item
          label="Age"
          name="age"
          rules={[{ required: true, message: "Please input your age!" }]}
        >
          <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="age"
            onChange={(e) => {setAge(e.target.value);}}/>
        </Form.Item>

        <Form.Item
          label="Email"
          name="email"
          rules={[{ required: true, message: "Please input your Email!" }]}
        >
          <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="Email"
            onChange={(e) => {setEmail(e.target.value);}}/>
        </Form.Item>

        <Form.Item label="Gender" name="gender">
          <Select>
            <Select.Option value="female">Female</Select.Option>
            <Select.Option value="male">Male</Select.Option>
            <Select.Option value="nonbinary">Non-binary</Select.Option>
          </Select>
          <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="Gender"
            onChange={(e) => {setGender(e.target.value);}}/>
        </Form.Item>

        <Form.Item
          label="Preferred workout area"
          name="workouttype"
          rules={[{ required: true, message: "Please input your username!" }]}
        >
          <Input prefix={<Select>
            <Select.Option value="like">I like everything</Select.Option>
            <Select.Option value="abs">Abs</Select.Option>
            <Select.Option value="arms">Arms</Select.Option>
            <Select.Option value="back">Back</Select.Option>
            <Select.Option value="butt">Butt</Select.Option>
            <Select.Option value="legs">Legs</Select.Option>
          </Select>}
            onChange={(e) => {setWork(e.target.value);}}/>
        </Form.Item>

        <Form.Item
          label="Location"
          name="location"
          rules={[{ required: true, message: "Please input your username!" }]}
        >
          <Input prefix={<UserOutlined className="site-form-item-icon" />} placeholder="Location"
            onChange={(e) => {setLoc(e.target.value);}}/>
        </Form.Item>

        <Form.Item label="About Me" name="aboutme">
          <Input prefix={<TextArea rows={3} placeholder="About" />} 
            onChange={(e) => {setAbout(e.target.value);}}/>
        </Form.Item>

        <Form.Item>
        <Button onClick={newProfile} type="primary" htmlType="submit" className="login-form-button">
            Submit
          </Button>
        </Form.Item>
          </Form>
    </Margins>
  );
}

export default RegistrationPage;
