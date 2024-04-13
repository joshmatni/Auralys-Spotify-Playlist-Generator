'use client';
import styles from "../styles/page.module.css";
import "../globals.css"

function Response() {
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
            <button className={styles.lgin} 
            type="navbutton"
            //     onClick = {(e) => { 
            //     router.push('../login')
            //   }}
              > Log In </button>
              </li>

              <li>
              <button className={styles.sgnup} type="navbutton"
                // onClick = {(e) => { 
                //     router.push('../signup')
                // }}
              > Sign Up </button>
              </li>

              <li>
              <button className={styles.question} type="navbutton"
            //   onClick = {(e) => { 
            //     router.push('../contact')
            //   }}
              > Contact Us </button>
              </li>

            </ul>
            </div>
          </nav>
        </header>
        <body>
            {/* <img src="songbkgrnd.jpg" className={styles.background} alt="Color"></img> */}
        </body>
        </div>
    );
}

export default Response;