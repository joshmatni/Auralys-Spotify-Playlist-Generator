import styles from "../styles/page.module.css";

function Signup() {

    
    const handleSubmit = (event) => {
        event.preventDefault(); // Prevents the default form submit action
        console.log('Form submission placeholder');
    };

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

        <main className={styles.mainContent}>
            <form className={styles.signupForm} onSubmit={handleSubmit}>
                <h2>Sign Up</h2>
                <input 
                    type="text" 
                    id="fullName" 
                    name="fullName" 
                    required 
                    placeholder="Full Name" 
                    className={styles.inputField}
                />

                <input 
                    type="email" 
                    id="email" 
                    name="email" 
                    required 
                    placeholder="Email" 
                    className={styles.inputField}
                />

                <input 
                    type="password" 
                    id="password" 
                    name="password" 
                    required 
                    minLength="2" 
                    placeholder="Password" 
                    className={styles.inputField}
                />

            <button type="submit" className={styles.submitBtn}>Create Account</button>

            <p className={styles.loginLink}>
                Already have an account? <a href="/login">Log in</a>
            </p>
            </form>
        </main>

       </div>

       
        
    );
}

export default Signup;