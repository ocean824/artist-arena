export type UtcInstant = string & { readonly __brand: 'UtcInstant' };

export function asUtcInstant(value: string): UtcInstant {
  const parsed = new Date(value);
  if (Number.isNaN(parsed.getTime()) || !value.endsWith('Z')) {
    throw new Error('UtcInstant must be a valid ISO-8601 UTC timestamp ending in Z');
  }
  return parsed.toISOString() as UtcInstant;
}
