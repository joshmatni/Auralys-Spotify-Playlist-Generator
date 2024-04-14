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

        <div className={styles.container}>
  <h1 className={styles.contactTitle}>Contact Us With Any Inquiries</h1>
  <form className={styles.contactForm} action="submit.php" method="post">
    <div className={styles.inputWrapper}> {/* This is the new wrapper */}
      <div className={styles.formGroup}>
        <label htmlFor="name" className={styles.inputLabel}>Name:</label>
        <input type="text" id="name" name="name" required/>
      </div>
      <div className={styles.formGroup}>
        <label htmlFor="email" className={styles.inputLabel}>Email:</label>
        <input type="email" id="email" name="email" required/>
      </div>
      <div className={styles.formGroup}>
        <label htmlFor="message" className={styles.inputLabel}>Message:</label>
        <textarea id="message" name="message" rows="4" required></textarea>
      </div>
    </div> {/* End of the new wrapper */}
    <button className={styles.submitButton} type="submit">Submit</button>
  </form>
</div>
</div>
  


    );
}

export default Contact;