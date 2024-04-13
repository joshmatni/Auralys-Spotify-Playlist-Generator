import Image from "next/image";
import styles from "./page.module.css";

export default function Home() {
  return (
    <main className={styles.main} >
      <div className={styles.description}>
        <header>
          <nav className={styles.header}>
            <div className={styles.headertext}>
              <h1 className={styles.title}>Auralys</h1>
            </div>
          </nav>
        </header>
        </div>
    </main>
  );
}
