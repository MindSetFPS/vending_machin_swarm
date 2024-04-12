// These styles apply to every route in the application
import './globals.css'
import type { AppProps } from 'next/app'
import RootLayout from './layout'

export default function App({ Component, pageProps }: AppProps) {
    return (
        <RootLayout>
            <Component {...pageProps} />
        </RootLayout>
    )
}