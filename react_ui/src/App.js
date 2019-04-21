import React, { Component } from "react";

import { Route, Switch, BrowserRouter } from "react-router-dom";

import Navigation from "./component/Navigation";
import Overview from "./component/Overview";
import Console from "./component/Console";
import PageNotFound from "./component/PageNotFound";
import BotControl from "./component/BotControl";
import ImageProcessing from "./component/ImageProcessing";

class App extends Component {
  render() {
    return (
      <BrowserRouter>
        <div>
          <Navigation />
          <Switch>
            <Route path="/" component={Overview} exact />
            <Route path="/bot_control" component={BotControl} />
            <Route path="/image_processing" component={ImageProcessing} />
            <Route path="/console" component={Console} />
            <Route component={PageNotFound} />
          </Switch>
        </div>
      </BrowserRouter>
    );
  }
}

export default App;
