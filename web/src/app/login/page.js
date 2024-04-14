import styles from "../styles/page.module.css";
import "../globals.css";
import ".././signup/signup.css"

function Login() {

    

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
                <h2>Log In</h2>
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

            <button type="submit" className="submitBtn">Log In</button>

            <p className={styles.loginLink}>
                Don't have an account? <a href="/signup">Sign Up</a>
            </p>
            </form>
          </div>
        </main>

       </div>

       
        
    );
}

export default Login;