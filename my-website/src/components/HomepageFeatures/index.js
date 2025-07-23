import React from 'react';
import Link from '@docusaurus/Link';
import styles from './styles.module.css';

export default function HomepageFeatures() {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', marginTop: '10rem' }}>
      <div className={styles.buttons}>
        <Link
          className={`button button--secondary button--lg ${styles.growOnHover}`}
          to="/docs/category/index"
          style={{
            fontSize: '2.5rem',
            padding: '2.5rem 5rem',
            minWidth: '400px',
            textAlign: 'center',
            fontWeight: 'bold'
          }}
        >
          Documentation 📰
        </Link>
      </div>
    </div>
  );
}