import type { AppProps } from 'next/app';
import '../styles/globals.css';  // Importa los estilos de Tailwind

export default function MyApp({ Component, pageProps }: AppProps) {
  return <Component {...pageProps} />;
}