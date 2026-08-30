/** Drizzle schema, migrations, transactions, outbox, and repository adapters. Implementation status: contract scaffold. */
export interface DbModule { readonly name: 'db'; readonly status: 'contract-scaffold'; }
export const dbModule: DbModule = { name: 'db', status: 'contract-scaffold' };
