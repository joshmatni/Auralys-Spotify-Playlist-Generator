import { Inter } from "next/font/google";
import "./globals.css";
import "./main.js"

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Auralys",
  description: "Auralys",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>{children}</body>
    </html>
  );
}
