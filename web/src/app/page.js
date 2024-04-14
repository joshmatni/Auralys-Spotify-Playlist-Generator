'use client';
import axios from 'axios';
import { useState } from "react";
import Loading from "./components/loading.js";
import Image from "next/image";
import styles from "./styles/page.module.css";
import { useRouter } from 'next/navigation';
import { useEffect } from "react";


async function getGPT() {
  const client = axios.create({
      headers: { "Content-Type": "application/json" },
  });
  const params = {
      prompt: Prompt,
  };
  try {
    const response = await axios.post("http://localhost:5000/create_playlist", {
    prompt: Prompt,
});
      setResponse(response.data.text);
      console.log({ Response });
      console.log(result.response.data)
      setIsLoading(false);
  } catch (error) {
      console.error(error.response.data);
  }
}

export default function Home() {
  const router = useRouter();
  const [Prompt, setPrompt] = useState("");
  const [Response, setResponse] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const [isPromptEmpty, setIsPromptEmpty] = useState(true);

  async function getGPT() {
    const client = axios.create({
      headers: { "Content-Type": "application/json" },
    });
    const params = {
      Prompt: {Prompt},
    };
    client
      .post("api/openai", JSON.stringify(params))
      .then((result) => {
        setResponse(result.data.text);
        console.log({Response});
        setIsLoading(false);
      })
      .catch((error) => {
        console.log(error.response.data);
      });
  }


  
  return (
      <div className={styles.background}>
        <header>
          <nav className={styles.header}>
            <div className={styles.container}>

            <div className={styles.headertext}>
              <h1 className={styles.title}>Auralys</h1>
            </div>

            <button onClick={getGPT}>Test Connection</button>

            <ul className={styles.headermenu}>

            <li>
            <button className={styles.lgin} 
                type="navbutton" 
                onClick = {(e) => { 
                  router.push('/login')
                }}
            > Log In </button>
              </li>

              <li>
              <button className={styles.sgnup} 
                type="navbutton"
                onClick = {(e) => { 
                  router.push('/signup')
                }}
              > Sign Up </button>
              </li>

              <li>
              <button className={styles.question} 
                type="navbutton"
                onClick = {(e) => { 
                  router.push('/contact')
                }}
              > Contact Us </button>
              </li>

            </ul>
            </div>
          </nav>
        </header>

        <div className={styles.description}>

          <Image src={'/music.svg'}
                width={200}
                height={125}
                alt="photo"></Image>
            <p>Welcome to Auralys, your personalized playlist experience! </p>
        </div>
      

          <div className={styles.promptsection}>

            <div className={styles.chatbox}>
            {isLoading ? (<div> <Loading/>
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
                    console.log({Prompt});
                    setIsLoading(true);
                    getGPT();
                    /*router.push('/response');*/
                  }
                
              }}
            >
              Submit </button>

            <button 
              type={styles.inputbutton} 
              className={styles.clearbutton}
              onClick = {(e) => {
                setResponse("");
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
