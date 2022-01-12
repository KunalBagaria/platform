import Head from 'next/head'

export const DefaultHead = () => (
	<Head>
        <title>SolStore</title>
        <link rel="icon" href="/favicon.ico" />
		<link rel="preload" href="/fonts/Mont/Mont-Book.otf" as="font" crossOrigin="" />
		<link rel="preload" href="/fonts/Mont/Mont-Regular.otf" as="font" crossOrigin="" />
		<link rel="preload" href="/fonts/Mont/Mont-SemiBold.otf" as="font" crossOrigin="" />
    </Head>
)