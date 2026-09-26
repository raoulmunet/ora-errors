# ora-errors

[![tests](https://github.com/raoulmunet/ora-errors/actions/workflows/tests.yml/badge.svg)](https://github.com/raoulmunet/ora-errors/actions/workflows/tests.yml) ![Python](https://img.shields.io/badge/Python-3.10--3.13-blue) [![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

A compact offline Oracle error explainer for common ORA errors, with causes, diagnostic questions and practical next steps.

> **Oracle compatibility**
>
> | Oracle version | Support |
> |---|---|
> | Oracle Database 19c | ✅ Catalog entries marked common are applicable |
> | Oracle Database 23ai | ✅ Catalog entries marked common are applicable |
> | Oracle AI Database 26ai | ✅ Catalog entries marked common are applicable |
>
> Error meanings can evolve or gain version-specific variants. Entries in this project are intentionally concise and version-neutral unless a version note is explicitly attached.

## Usage

```bash
python -m pip install "git+https://github.com/raoulmunet/ora-errors.git"

ora-errors ORA-01722
ora-errors ORA-01555 --format json
ora-errors --search "listener"
```

Example:

```text
ORA-01722 — invalid number

What it means
Oracle attempted a character-to-number conversion that failed.

Common causes
- comparing NUMBER and character data with implicit conversion
- TO_NUMBER on non-numeric text
- dirty source data in ETL pipelines

Check next
- inspect datatypes on both sides of comparisons
- isolate rows that fail explicit conversion
- avoid relying on implicit conversion
```

## Included starter catalog

The initial catalog includes frequently encountered errors such as:

- ORA-00001
- ORA-00942
- ORA-01400
- ORA-01403
- ORA-01555
- ORA-01722
- ORA-02291
- ORA-03113
- ORA-06502
- ORA-12154
- ORA-12514
- ORA-12541

## Important

This tool is a troubleshooting aid, not a replacement for the exact error text and documentation corresponding to your Oracle release and environment.

## Oracle Dev Tools family

This repository is part of the **Oracle Dev Tools** suite: small, composable developer utilities designed around Oracle Database 19c, 23ai and 26ai.

| Area | Tools |
|---|---|
| Foundation | [ora-core](https://github.com/raoulmunet/ora-core) |
| SQL analysis | [ora-impact](https://github.com/raoulmunet/ora-impact) · [ora-plan](https://github.com/raoulmunet/ora-plan) · [ora-lineage](https://github.com/raoulmunet/ora-lineage) · [ora-lint](https://github.com/raoulmunet/ora-lint) · [ora-sql-diff](https://github.com/raoulmunet/ora-sql-diff) · [ora-sql-complexity](https://github.com/raoulmunet/ora-sql-complexity) · [ora-join-viz](https://github.com/raoulmunet/ora-join-viz) · [ora-bind](https://github.com/raoulmunet/ora-bind) |
| Data & operations | [ora-doc](https://github.com/raoulmunet/ora-doc) · [ora-data-quality](https://github.com/raoulmunet/ora-data-quality) · [ora-csv-loader](https://github.com/raoulmunet/ora-csv-loader) · [ora-etl-log](https://github.com/raoulmunet/ora-etl-log) · [ora-migration-check](https://github.com/raoulmunet/ora-migration-check) · [ora-errors](https://github.com/raoulmunet/ora-errors) · [ora-schema-explorer](https://github.com/raoulmunet/ora-schema-explorer) |
| PL/SQL analysis | [ora-exception-flow](https://github.com/raoulmunet/ora-exception-flow) · [ora-call-graph](https://github.com/raoulmunet/ora-call-graph) · [ora-dead-code](https://github.com/raoulmunet/ora-dead-code) |

## License

MIT.
