/* eslint-disable @next/next/no-img-element */
import styles from '@/styles/CreateMarketplace.module.scss'
import selectImageIcon from '@/images/select-image.svg'
import { useState } from 'react'

type Form = {
	name: string,
	description: string,
	logo: File | string,
	banner: File | string,
	email: string,
	category: string
}

export const CreateMarketplace = () => {
	const [formData, setFormData] = useState<Form>({} as Form);

	const submit = () => {
		console.log(formData)
		// add network request here
	}

	return (
		<div>
			<h1 className={styles.heading}>Create Marketplace</h1>
			<div className={styles.form}>

				<div className={styles.flex}>
					<div className={styles.formGroup}>
						<p className={styles.label}>Logo</p>
						<input onChange={(e) => setFormData({...formData, logo: e.target.files ? e?.target?.files[0] : '' })} id="logo-input" style={{ display: 'none' }} type="file" />
						<div onClick={() => document.getElementById('logo-input')?.click()} className={styles.logoInput}>
							<img src={selectImageIcon.src} alt="Select Image" />
						</div>
					</div>
					<div className={styles.formGroup}>
						<p className={styles.label}>Banner</p>
						<input onChange={(e) => setFormData({...formData, banner: e.target.files ? e?.target?.files[0] : '' })} id="banner-input" style={{ display: 'none' }} type="file" />
						<div onClick={() => document.getElementById('banner-input')?.click()} className={styles.bannerInput}>
							<img src={selectImageIcon.src} alt="Select Image" />
						</div>
					</div>
				</div>

				<div className={styles.flex}>
					<div className={styles.formGroup}>
						<p className={styles.label}>Name of the store</p>
						<input onChange={(e) => setFormData({...formData, name: e.target.value })} className={styles.input} type="text" />
					</div>
					<div className={styles.formGroup}>
						<p className={styles.label}>Email ID for communications</p>
						<input onChange={(e) => setFormData({...formData, email: e.target.value })} className={styles.input} type="text" />
					</div>
				</div>

				<div className={styles.flex} style={{ width: '100%'}}>
					<div className={styles.formGroup} style={{ width: '100%' }}>
						<p className={styles.label}>Description</p>
						<textarea onChange={(e) => setFormData({...formData, description: e.target.value })} className={styles.input} style={{ paddingTop: '1rem', width: '100%', height: '10rem', resize: 'none' }} />
					</div>
				</div>

				<div className={styles.flex}>
					<div className={styles.formGroup}>
						<button onClick={submit} style={{ padding: '1rem 2rem'}} className="purple-btn">Create Marketplace</button>
					</div>
				</div>


			</div>
		</div>
	)
}