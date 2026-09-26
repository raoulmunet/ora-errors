# ora-errors

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

## License

MIT.
