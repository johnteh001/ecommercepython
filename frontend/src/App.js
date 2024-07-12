// frontend/src/App.js

import React from 'react';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import ProductList from './components/ProductList';
import Cart from './components/Cart';
import Checkout from './components/Checkout';
import UserLogin from './components/UserLogin';
import UserRegister from './components/UserRegister';
import ProfilePage from './components/ProfilePage';
import AdminPanel from './components/AdminPanel';

function App() {
  return (
    <Router>
      <Switch>
        <Route path="/" exact component={ProductList} />
        <Route path="/cart" component={Cart} />
        <Route path="/checkout" component={Checkout} />
        <Route path="/login" component={UserLogin} />
        <Route path="/register" component={UserRegister} />
        <Route path="/profile" component={ProfilePage} />
        <Route path="/admin" component={AdminPanel} />
      </Switch>
    </Router>
  );
}

export default App;
