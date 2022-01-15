import {
	Connection,
	Transaction,
	SystemProgram,
	PublicKey,
	LAMPORTS_PER_SOL,
} from '@solana/web3.js';
import toast from 'react-hot-toast';
import getWallet from '@/util/whichWallet';

declare global {
	interface Window {
		solana: any,
			solflare: any,
			sollet: any
	}
}

export const connectWallet = async () => {
	const wallet = getWallet();
	if (wallet) {
		const response = await wallet.connect();
		if (response || response.publicKey) {
			toast.success('Connected to wallet');
		} else {
			toast.error('Failed to connect to wallet');
			return;
		}
		return wallet.publicKey;
	}
	toast.error('No Solana wallets found');
	window.open('https://phantom.app/', '_blank');
};

export const disconnectWallet = async () => {
	const wallet = getWallet();
	if (wallet) {
		await wallet.disconnect();
		toast.success('Disconnected from wallet');
	}
};

export const sendMoney = async (to: PublicKey, amount: number, buying ? : boolean) => {
	const wallet = getWallet();
	const publicKey = await connectWallet();
	console.log(publicKey);
	const environment = window.location.hostname === 'localhost' ? 'devnet' : 'mainnet-beta';
	const network = `https://api.${environment}.solana.com`;

	const connection = new Connection(network);
	const transaction = new Transaction()
		.add(
			SystemProgram.transfer({
				fromPubkey: publicKey,
				toPubkey: to,
				lamports: Number(amount) * LAMPORTS_PER_SOL,
			}),
		);
	const {
		blockhash,
	} = await connection.getRecentBlockhash();
	transaction.recentBlockhash = blockhash;
	transaction.feePayer = publicKey;
	const signedTransaction = await wallet.signTransaction(transaction);

	try {
		const txid = await connection.sendRawTransaction(signedTransaction.serialize());
		if (!txid) throw new Error('txid is undefined');
		const verified = connection.confirmTransaction(txid);
		if (!buying) {
			toast.promise(
				verified, {
					loading: 'Confirming Transaction, you can close this tab',
					success: 'Transaction Confirmed',
					error: 'Transaction Failed',
				},
			);
		}
		// const signature = await verified;
		return txid;
	} catch (error) {
		console.error(error);
		toast.error('Failed to send transaction');
	}
	// const confirmed = await connection.confirmTransaction(txid);
	// return confirmed
};

export const signMessage = async (message: string) => {
	const wallet = getWallet();
	const encodedMessage = new TextEncoder().encode(message);
	const signedMessage = await wallet.signMessage(encodedMessage, 'utf8');
	return signedMessage;
};

export const walletIsConnected = () => {
	const wallet = getWallet();
	return wallet.isConnected;
};

export const connectIfTrusted = () => {
	const wallet = getWallet();
	if (wallet) {
		return wallet.connect({
			onlyIfTrusted: true,
		});
	}
};