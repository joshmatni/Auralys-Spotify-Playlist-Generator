import "./globals.css";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import Home from "./page";
import Songs from "./songs";

function App() {
  return (
    <div className="App">
      <Router>
        <Switch> 
            <Route exact path = "/Home" component = {page} />
            <Route exact path="/Songs" component={songs} />

        </Switch>
      </Router>
    </div>
  );
}

export default App;