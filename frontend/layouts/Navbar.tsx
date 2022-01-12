import Image from 'next/image'
import Link from 'next/link'
import styles from '@/styles/Navbar.module.scss'
import logo from '@/images/logo.svg'

export const Navbar = () => {
	return (
		<div className="container">
			<nav className={styles.parent}>
				<div className="standard-grid">
					<Link href="/">
						<a className={`${styles.logo} v-center`}>
							<Image alt="" src={logo} />
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
					<button className="blue-btn v-center a-right">Sign in using Solana</button>
				</div>
			</nav>
		</div>
	)
}