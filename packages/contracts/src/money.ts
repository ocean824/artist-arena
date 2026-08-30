export type EconomicInstrument =
  | 'ARENA_POINTS'
  | 'PURCHASED_CREDIT'
  | 'EARNED_CREDIT'
  | 'FIAT'
  | 'CHAIN_ASSET';

export interface Amount {
  readonly instrument: EconomicInstrument;
  readonly currencyOrDenom: string;
  readonly minorOrAtomicUnits: bigint;
}

function assertCompatible(left: Amount, right: Amount): void {
  if (left.instrument !== right.instrument || left.currencyOrDenom !== right.currencyOrDenom) {
    throw new Error('Amounts with different instruments or currencies/denominations cannot be combined');
  }
}

export function addAmount(left: Amount, right: Amount): Amount {
  assertCompatible(left, right);
  return { ...left, minorOrAtomicUnits: left.minorOrAtomicUnits + right.minorOrAtomicUnits };
}

export function subtractAmount(left: Amount, right: Amount): Amount {
  assertCompatible(left, right);
  return { ...left, minorOrAtomicUnits: left.minorOrAtomicUnits - right.minorOrAtomicUnits };
}

export function calculateBasisPointFee(amount: Amount, basisPoints: bigint): Amount {
  if (amount.minorOrAtomicUnits < 0n) throw new Error('Fee input must not be negative');
  if (basisPoints < 0n || basisPoints > 10_000n) throw new Error('Basis points must be between 0 and 10000');
  return { ...amount, minorOrAtomicUnits: (amount.minorOrAtomicUnits * basisPoints) / 10_000n };
}

export const FOUNDER_DEFAULT_CONVERSION_FEE_BPS = 100n;
