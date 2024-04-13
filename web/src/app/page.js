'use client';
import { useState } from "react";
import Loading from "./components/loading.js";
import Image from "next/image";
import styles from "./styles/page.module.css";
// import { useHistory } from "react-router-dom";


export default function Home() {
  const [Prompt, setPrompt] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [isPromptEmpty, setIsPromptEmpty] = useState(true);
  
  return (
      <div className={styles.background}>
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

        <div className={styles.description}>
            <p>Welcome to Auralys, your handly helper for creating personalized playlists! </p>
        </div>
      

          <div className={styles.promptsection}>

            <div className={styles.chatbox}>
            {isLoading ? (<div> <Loading/><div className={styles.loadingAnimation}>
      {/* Here you can insert your animated graphic or icon */}
    </div>
    <p className={styles.loadingText}>
      Tuning your personalized playlist...
    </p></div> ) : 
            (
              
            <div className={styles.inputbox} >
            <input className={styles.inputfield} 
                    type={styles.text} 
                    placeholder="Enter prompt"
                    value={Prompt}
                    onChange={(e) => {
                      setPrompt(e.target.value);
                      setIsPromptEmpty(false);
                    }}
            />
    
            <button 
              type={styles.inputbutton} 
              className={styles.submitbutton}
              onClick = {(e) => { 
                  if (isPromptEmpty)
                  {
                    setIsLoading(false);
                  }
                  else
                  {
                    setIsLoading(true);
                    /*call gpt method*/
                    //console.log('Navigating to /songs');
                    //navigate('../pages/songs');
                  }
                
              }}
            >
              Submit </button>

            <button 
              type={styles.inputbutton} 
              className={styles.clearbutton}
              onClick = {(e) => {
                setIsLoading(false);
                setPrompt("");
                setIsPromptEmpty(true);
              }}
            >
              Clear </button>
            </div>
    )}
          </div>
              </div>



            </div>
  );

}
