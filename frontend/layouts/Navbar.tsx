/* eslint-disable @next/next/no-img-element */
import Image from 'next/image'
import Link from 'next/link'
import styles from '@/styles/Navbar.module.scss'
import { connectWallet } from '@/components/Wallet'
import logo from '@/images/logo.svg'

export const Navbar = () => {
	return (
		<div className="container">
			<nav className={styles.parent}>
				<div className="standard-grid">
					<Link href="/">
						<a className={`${styles.logo} v-center`}>
							<img alt="" src={logo.src} />
						</a>
					</Link>
					<div />
					<div className={styles.links}>
						<Link href="/street">
							<a>SolStreet</a>
						</Link>
						<Link href="/mystore">
							<a>My Store</a>
						</Link>
					</div>
					<button onClick={connectWallet} className="blue-btn v-center a-right">Sign in using Solana</button>
				</div>
			</nav>
		</div>
	)
}