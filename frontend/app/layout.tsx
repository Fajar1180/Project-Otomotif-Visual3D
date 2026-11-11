import type { Metadata } from 'next'
import Navbar from './components/Navbar'
import Footer from './components/Footer'
import './globals.css'

export const metadata: Metadata = {
  title: 'Otomotif AI - Vehicle Diagnosis & Configurator',
  description: 'AI-powered vehicle diagnostic and 3D customization platform',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body className="flex flex-col min-h-screen">
        <Navbar />
        <main className="flex-1 container-app py-8">{children}</main>
        <Footer />
      </body>
    </html>
  )
}
