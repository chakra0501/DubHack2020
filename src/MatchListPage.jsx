import React, { Component } from "react";
import { Card, Button,  } from "antd";
import { CheckOutlined, CloseOutlined } from "@ant-design/icons";
import styled from "styled-components";
import Sidebar from './Sidebar';
import { EditOutlined, EllipsisOutlined, SettingOutlined } from '@ant-design/icons';

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


export default class MatchListPage extends Component {

  componentDidMount(){

  }

  getNewProfile() {
    fetch('http://127.0.0.1:5000/getMatch'+'?user='+getUsername(), 
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

  render() {
    return (
      <HorizontalMain>
        <Sidebar currentPage="matches" />
        <Margins>
          <Horizontal>
            <MarginN>
              
            <Card title="Your Matches" bordered={false} style={{ width: 300 }}>
            <p>Card content</p>
            <p>Card content</p>
            <p>Card content</p>
          </Card>
            </MarginN>

            <MarginY>
            <MarginN>

           
            </MarginN>

            </MarginY>
            <MarginY>
            <MarginN>

           
            </MarginN>
            </MarginY>
            
          </Horizontal>
        </Margins>
      </HorizontalMain>
    );
  }
}
