import Image from "next/image";
import styles from "./page.module.css";

export default function Home() {
  return (
      <div className={styles.background}>
        <header>
          <nav className={styles.header}>
            <div className={styles.headertext}>
              <h1 className={styles.title}>Auralys</h1>
              <button className={styles.lgin} type="button"> Log In </button>
              <button className={styles.sgnup} type="button"> Sign Up </button>
            </div>
          </nav>
        </header>
          <div className={styles.hero}>
            <div className={styles.chatbox}>
              <input className={styles.inputbox} type="text" placeholder="Enter something we'll decide later"></input>
            </div>
          </div>
        </div>
  );
}
