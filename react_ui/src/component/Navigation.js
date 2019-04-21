import React, { Component } from "react";
import { Navbar, Nav } from "react-bootstrap";
import { Link } from "react-router-dom";
class Navigation extends Component {
  render() {
    return (
      <Navbar expand="lg" variant="light" bg="light" sticky="top">
        <Navbar.Toggle />
        <Link to="/" className="navbar-brand">
          <img
            alt=""
            src="https://avatars2.githubusercontent.com/u/16348041?s=460&v=4"
            width="30"
            height="30"
            className="d-inline-block align-top"
          />
          {" Object Detection Robot "}
        </Link>
        <Navbar.Collapse className="justify-content-end">
          <Nav className="mr-auto">
            <Link to="/bot_control" className="nav-link">
              botControl
            </Link>
            <Link to="/image_processing" className="nav-link">
              imageProcessing
            </Link>
            <Link to="/console" className="nav-link">
              console
            </Link>
          </Nav>
          <Navbar.Text>
            Developed By :{" "}
            <a href="https://github.com/extinctCoder">extinctCoder</a>
          </Navbar.Text>
        </Navbar.Collapse>
      </Navbar>
    );
  }
}

export default Navigation;
