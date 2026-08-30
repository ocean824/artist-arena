export type ActivationState =
  | 'LOCAL'
  | 'SANDBOX'
  | 'TESTNET'
  | 'PILOT'
  | 'REGION_LIMITED'
  | 'VALUE_CAPPED'
  | 'PRODUCTION_ENABLED'
  | 'DISABLED_BY_POLICY';

export interface PaidContestPolicyContext {
  readonly operatorProfile: string;
  readonly jurisdiction: string | null;
  readonly locationConfidence: 'NONE' | 'LOW' | 'MEDIUM' | 'HIGH';
  readonly ageEligible: boolean;
  readonly identityLevel: string;
  readonly sanctionsResult: 'UNKNOWN' | 'CLEAR' | 'REVIEW' | 'DENY';
  readonly selfExcluded: boolean;
  readonly withinLimits: boolean;
  readonly accountAllowed: boolean;
  readonly walletAllowed: boolean;
  readonly providerAvailable: boolean;
  readonly activationState: ActivationState;
  readonly policyVersion: string;
}

export interface PolicyDecision {
  readonly allowed: boolean;
  readonly reasonCodes: readonly string[];
  readonly policyVersion: string;
}

export function evaluatePaidContestPolicy(context: PaidContestPolicyContext): PolicyDecision {
  const reasons: string[] = [];
  if (context.activationState === 'DISABLED_BY_POLICY') reasons.push('ACTIVATION_DISABLED');
  if (!context.jurisdiction || context.locationConfidence !== 'HIGH') reasons.push('LOCATION_NOT_VERIFIED');
  if (!context.ageEligible) reasons.push('AGE_NOT_ELIGIBLE');
  if (context.sanctionsResult !== 'CLEAR') reasons.push('SANCTIONS_OR_RISK_NOT_CLEAR');
  if (context.selfExcluded) reasons.push('SELF_EXCLUDED');
  if (!context.withinLimits) reasons.push('LIMIT_EXCEEDED');
  if (!context.accountAllowed || !context.walletAllowed) reasons.push('ACCOUNT_OR_WALLET_RESTRICTED');
  if (!context.providerAvailable) reasons.push('PROVIDER_UNAVAILABLE');
  return { allowed: reasons.length === 0, reasonCodes: reasons, policyVersion: context.policyVersion };
}
