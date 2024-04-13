import Image from "next/image";
import styles from "./page.module.css";

export default function Home() {
  return (
      <div className={styles.background}>
        <header>
          <nav className={styles.header}>
            
            <div className={styles.headertext}>
              <h1 className={styles.title}>Auralys</h1>
            </div>

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
          </nav>
        </header>
          <div className={styles.hero}>

            <div className={styles.chatbox}>
              <input className={styles.inputbox} type="text" placeholder="Enter prompt"></input>
            </div>
          </div>
        </div>
        
  );
}
