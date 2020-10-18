import React, { Component } from "react";
import RegistrationPage from "./RegistrationPage";
import HomePage from "./HomePage";
import MatchPage from "./MatchPage";  
import MatchListPage from "./MatchListPage";
import ProfilePage from "./ProfilePage";

// import { BrowserRouter as Router, Route } from "react-router-dom";
import { Route, Switch } from "react-router";
import { BrowserRouter } from "react-router-dom";
// import history from "./history";
import "./App.css";
// import { createBrowserHistory } from "history";
/*
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;

*/

//const history = createBrowserHistory();

export default class App extends Component {
  render() {
  
    return (
      <BrowserRouter>
        <Switch>
          <Route path="/register">
            <RegistrationPage />
          </Route>
          <Route path="/matching">
            <MatchPage />
          </Route>
          <Route path="/profile">
            <ProfilePage />
          </Route>
          <Route path="/matches">
              <MatchListPage/>
          </Route>
          <Route exact path="/">
            <HomePage />
          </Route>
        </Switch>
      </BrowserRouter>
    );
  }
}
