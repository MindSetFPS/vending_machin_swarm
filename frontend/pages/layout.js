import { Inter } from "next/font/google";
import { Providers } from "./providers";
import Nav from "@/components/Navbar";

const inter = Inter({ subsets: ["latin"] });

export default function RootLayout({ children }) {
  return (
        <Providers>
          <Nav />
          <div className="container mx-auto px-12">
            {children}
          </div>
        </Providers>
  );
}
