import styles from "../styles/page.module.css";
import "../globals.css";
import "./signup.css";

function Signup() {

    

    return (
        <div>
        <header>
          <nav className={styles.header}>
            <div className={styles.container}>

            <div className={styles.headertext}>
              <h1 className={styles.title}>Auralys</h1>
            </div>
            <div className={styles.loadingAnimation}> </div>

            <ul className={styles.headermenu}>

            <li>
            <button className={styles.lgin} type="navbutton"> Log In </button>
              </li>

              <li>
              <button className={styles.sgnup} type="navbutton"> Sign Up </button>
              </li>

              <li>
              <button className={styles.question} type="navbutton"> Contact Us </button>
              </li>

            </ul>
            </div>
          </nav>
        </header>

        <main className="mainContent">
          <div className="signupCard">
            <form className="signupForm">
                <h2>Sign Up</h2>
                <input 
                    type="text" 
                    id="Name" 
                    name="Name" 
                    required 
                    placeholder="Name" 
                    className="inputField"
                />

                <input 
                    type="password" 
                    id="password" 
                    name="password" 
                    required 
                    minLength="2" 
                    placeholder="Password" 
                    className="inputField"
                />

            <button type="submit" className="submitBtn">Create Account</button>

            <p className={styles.loginLink}>
                Already have an account? <a href="/login">Log in</a>
            </p>
            </form>
          </div>
        </main>

       </div>

       
        
    );
}

export default Signup;