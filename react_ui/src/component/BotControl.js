import React, { Component } from "react";
import { Container, Row, Col, Button } from "react-bootstrap";
class BotControl extends Component {
  render() {
    return (
      <Container>
        <Row>
          <Col>
            <Button>FirstDegree Up</Button>
          </Col>
          <Col>
            <Button>SecondDegree Up</Button>
          </Col>
          <Col>
            <Button>Thirdegree Up</Button>
          </Col>
          <Col>
            <Button>FourthDegree Up</Button>
          </Col>
          <Col>
            <Button>Fifthegree Up</Button>
          </Col>
          <Col>
            <Button>Claw Up</Button>
          </Col>
        </Row>
        <Row>
          <Col>1 of 3</Col>
          <Col>2 of 3</Col>
          <Col>3 of 3</Col>
        </Row>
      </Container>
    );
  }
}

export default BotControl;
