'use client';
import styles from "../styles/page.module.css";
import "../globals.css"
import "./response.css"
function Response() {
    return (
        <div className={styles.receiptContainer}>
        <div className={styles.receiptHeader}>
          <h2>Receiptify</h2>
          <p>Your Custom Mix</p>
        </div>
        <div className={styles.receiptBody}>
          <p className={styles.title}>Order #0001 for</p>
          <p>Thursday, November 10, 2022</p>
  
          <div className={styles.itemRow}>
            <span>01 POP</span>
            <span>4</span>
          </div>
          {/* Repeat for each item */}
          {/* ... */}
          
          <div className={styles.totalRow}>
            <span>Item Count:</span>
            <span>10</span>
          </div>
          <div className={styles.totalRow}>
            <span>Total:</span>
            <span>15</span>
          </div>
          
          {/* Card Details */}
          <div className={styles.totalRow}>
            <span>Card:</span>
            <span>**** **** **** 2022</span>
          </div>
          <div className={styles.totalRow}>
            <span>Auth Code:</span>
            <span>123421</span>
          </div>
          <div className={styles.totalRow}>
            <span>Cardholder:</span>
            <span>John Doe</span>
          </div>
        </div>
        <div className={styles.receiptFooter}>
          <p>Thank you for visiting!</p>
          <p>receiptify.herokuapp.com</p>
        </div>
      </div>
    );
}

export default Response;
