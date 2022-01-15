import type { NextPage } from 'next'
import { DefaultHead } from '@/layouts/Head'
import { Navbar } from '@/layouts/Navbar'
import { CreateMarketplace } from '@/layouts/CreateMarketplace'
// import styles from '../styles/Home.module.scss'

const MyStore: NextPage = () => {
    return (
        <>
			<DefaultHead />
			<Navbar />
			<main style={{ marginTop: '10rem' }}>
				<CreateMarketplace />
			</main>
		</>
    )
}

export default MyStore