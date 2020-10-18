 import React, { Component } from "react";
import { Card, Button } from "antd";
import { CheckOutlined, CloseOutlined } from "@ant-design/icons";
import styled from "styled-components";
import Sidebar from "./Sidebar";

const { Meta } = Card;

const Horizontal = styled.div`
  display: flex;
  align-items: center;
`;

const HorizontalMain = styled.div`
  display: flex;
`;

const Margins = styled.div`
  margin: 100px;
  margin-left: 300px;
  margin-right: 300px;
  display: flex;
  flex-direction: column;
  align-items: center;
`;

const MarginN = styled.div`
  margin-right: 10px;
`;

const MarginY = styled.div`
  margin-left: 10px;
`;  

function getUsername() {
  let URLParse = new URLSearchParams((new URL(window.location.href)).search);
  console.log(window.location.href);
  const username = URLParse.get("user");
  console.log(username);
  return username;
}

export default class MatchPage extends Component {

  constructor() {
    super();
    this.state = {first:'NA',last:'NA',workout:'NA',about:'NA',profile:'NA'};
    this.swipeLeft = this.swipeLeft.bind(this);
    this.swipeRight = this.swipeRight.bind(this);
  }

  componentDidMount(){
    this.getNewProfile();
  }

  getNewProfile() {
    fetch('http://127.0.0.1:5000/getNext'+'?user='+getUsername(), 
      {
        method:"POST",
        cache: "no-cache",
        headers:{
            "content_type":"application/string",
        },
        body:JSON.stringify({name : 'joy'})
        })
          .then(res => {
              console.log("Result:");
              console.log(res);
              return res.json();     
            })
          .then((res) => 
              {
                console.log("Parsed return...");
                this.setState({
                  first: res.first,
                  last: res.last,
                  workout: res.workout,
                  about: res.about,
                  profile: res.username
                });
              },
              // Note: it's important to handle errors here
                // instead of a catch() block so that we don't swallow
              // exceptions from actual bugs in components.
              (error) => {
              });
  }

  swipeLeft() {
    fetch('http://127.0.0.1:5000/newDislike'+'?user='+getUsername()+"&like="+this.state.profile, 
      {
        method:"POST",
        cache: "no-cache",
        headers:{
            "content_type":"application/json",
        }, body:JSON.stringify({name : 'joy'})
        });
    this.getNewProfile();
  }

  swipeRight() {
    fetch('http://127.0.0.1:5000/newLike'+'?user='+getUsername()+"&like="+this.state.profile, 
      {
        method:"POST",
        cache: "no-cache",
        headers:{
            "content_type":"application/json",
        }, body:JSON.stringify({name : 'joy'})
        });
    this.getNewProfile();
  }

  render() {
    return (
      <HorizontalMain>
        <Sidebar currentPage="matching" />
        <Margins>
          <h1>Find your workout buddies</h1>
          <Horizontal>
            <MarginN>
              <Button
                type="primary"
                shape="circle"
                icon={<CloseOutlined />}
                size="large"
                danger
                onClick={this.swipeLeft}
              ></Button>
            </MarginN>
            <Card
              style={{ width: 300 }}
              cover={
                <img
                  alt="example"
                  src="https://os.alipayobjects.com/rmsportal/QBnOOoLaAfKPirc.png"
                />
              }
            >
              <Meta title="Profile"></Meta>
                <div>
                <p id= "name">Name: {this.state.first} {this.state.last}</p>
                <p id = "work" >Favorite workout(s): {this.state.workout}</p>
                <p>About me: {this.state.about}</p>
                </div>
            </Card>
            <MarginY>
              <Button
                type="primary"
                shape="circle"
                icon={<CheckOutlined />}
                size="large"
                onClick={this.swipeRight}
              ></Button>
            </MarginY>
          </Horizontal>
        </Margins>
      </HorizontalMain>
    );
  }
}

// export default MatchPage;
