'use client';
import Image from "next/image";
import styles from "./page.module.css";
import {generateResponse} from "./main";

export default function Home() {
  return (
      <div className={styles.background}>
        <header>
          <nav className={styles.header}>
            <div className={styles.container}>

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
            </div>
          </nav>
        </header>
          <div className={styles.hero}>

            <div className={styles.chatbox}>
                <p className={styles.chatboxtext}>
                  Enter a prompt!
                </p>

                <div className={styles.inputbox}>

                <input className={styles.inputfield} type={styles.text} placeholder="Enter prompt"></input>
                
              <button type={styles.submit} className={styles.inputbutton} onClick={generateResponse}>
                Submit
              </button>
                </div>

            </div>
          </div>
        </div>
        

        
  );
}
