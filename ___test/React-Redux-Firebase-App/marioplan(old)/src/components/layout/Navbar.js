import React from 'react';
import { Link } from 'react-router-dom';
import SignetInLinks from './SignedInLinks';
import SignetOutLinks from './SignedOutLinks';

const Navbar = () => {
    return (
        <nav className="nav-wrapper grey darken-3">
            <div className="container">
                <Link to='/' className="brand-logo">MarioPlan</Link>
                <SignetInLinks />
                <SignetOutLinks />
            </div>
        </nav>
    )
};

export default Navbar;