// eslint-disable-next-line import/no-anonymous-default-export
export default () => typeof window !== "undefined" ? (window.solana || window.solflare) : null;