'use client';
import { useState } from "react";
import Image from "next/image";
import styles from "./styles/page.module.css";
import {generateResponse} from "./main";

export default function Home() {

  const [Prompt, setPrompt] = useState("");
  const [isLoading, setIsLoading] = useState(false);

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
                <div className={styles.chatboxtext}>
                  {isLoading ? (<p> {Prompt} </p>) 
                  : <p> Enter prompt: </p>}
                </div>

                <div className={styles.inputbox}>

                <input className={styles.inputfield} 
                        type={styles.text} 
                        placeholder="Enter prompt"
                        value={Prompt}
                        onChange={(e) => {
                          setPrompt(e.target.value);
                        }}
                />
                
              <button 
                type={styles.inputbutton} 
                className={styles.submitbutton}
                onClick = {(e) => { 
                    setIsLoading(true);
                  
               }}
              >
                Submit
              </button>

              <button 
                type={styles.inputbutton} 
                className={styles.clearbutton}
                onClick = {(e) => {
                  setIsLoading(false);
                  setPrompt("");
               }}
              >
                Clear
              </button>
                </div>

            </div>
          </div>
        </div>
        

        
  );
}
