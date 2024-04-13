import styles from "../styles/page.module.css";

function Contact() {
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

        <header>
          <h1> Welcome to contact page </h1
        </header>
    </div>

    );
}

export default Contact;