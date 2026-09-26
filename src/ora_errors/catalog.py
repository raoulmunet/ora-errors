CATALOG = {
"ORA-00001": {
"title": "unique constraint violated",
"meaning": "An INSERT or UPDATE would create a duplicate value for a unique constraint or unique index.",
"causes": ["duplicate business key or primary key", "sequence/key generation collision", "unexpected duplicate source data"],
"checks": ["identify the violated constraint/index", "inspect the existing row with the same key", "verify key-generation logic"]
},
"ORA-00942": {
"title": "table or view does not exist",
"meaning": "The referenced object is unavailable under the current name resolution and privileges.",
"causes": ["wrong schema or object name", "missing direct privilege", "object not created in this environment"],
"checks": ["qualify the owner explicitly", "verify ALL_OBJECTS/ALL_TABLES visibility", "check direct grants for stored PL/SQL"]
},
"ORA-01400": {
"title": "cannot insert NULL",
"meaning": "A row attempted to store NULL in a NOT NULL column.",
"causes": ["missing source value", "mapping error", "default not defined or not used"],
"checks": ["identify the target column", "trace the source mapping", "decide whether data or DDL should change"]
},
"ORA-01403": {
"title": "no data found",
"meaning": "A PL/SQL query expecting a row returned none, or application logic explicitly raised NO_DATA_FOUND.",
"causes": ["SELECT INTO found no row", "lookup data is missing", "predicate is more restrictive than expected"],
"checks": ["run the SELECT independently", "review predicates and lookup data", "handle NO_DATA_FOUND only where it is an expected business case"]
},
"ORA-01555": {
"title": "snapshot too old",
"meaning": "Oracle could not reconstruct the required read-consistent version from available undo.",
"causes": ["long-running query with heavy concurrent changes", "insufficient undo retention/capacity", "processing pattern repeatedly revisits changed blocks"],
"checks": ["measure query duration and undo pressure", "review UNDO_RETENTION and undo tablespace sizing", "reduce unnecessary long scans or commit-sensitive processing patterns"]
},
"ORA-01722": {
"title": "invalid number",
"meaning": "A character-to-number conversion failed.",
"causes": ["implicit conversion between NUMBER and character data", "TO_NUMBER on non-numeric text", "dirty ETL source data"],
"checks": ["compare datatypes on both sides of predicates", "isolate invalid source values", "prefer explicit validated conversion over implicit conversion"]
},
"ORA-02291": {
"title": "integrity constraint violated - parent key not found",
"meaning": "A child row references a parent key that does not exist.",
"causes": ["ETL load order is wrong", "missing parent record", "foreign-key mapping uses the wrong key"],
"checks": ["identify the foreign key and parent table", "look up the missing parent key", "load/repair the parent before the child"]
},
"ORA-03113": {
"title": "end-of-file on communication channel",
"meaning": "The client/server Oracle communication channel ended unexpectedly.",
"causes": ["server process terminated", "instance/network interruption", "database-side error caused session termination"],
"checks": ["inspect alert log and trace files around the timestamp", "confirm instance/listener health", "correlate with network and server events"]
},
"ORA-06502": {
"title": "PL/SQL numeric or value error",
"meaning": "PL/SQL encountered a value, conversion, length or numeric problem.",
"causes": ["string too large for variable", "invalid conversion", "numeric precision/range issue"],
"checks": ["inspect variable declarations and input sizes", "review conversion points", "capture a backtrace and failing values"]
},
"ORA-12154": {
"title": "TNS: could not resolve the connect identifier specified",
"meaning": "The client could not resolve the supplied Oracle Net connect identifier.",
"causes": ["wrong TNS alias", "tnsnames.ora not found or not used", "malformed connect descriptor"],
"checks": ["verify the connect identifier", "check TNS_ADMIN and client configuration", "test with a full Easy Connect string"]
},
"ORA-12514": {
"title": "listener does not currently know of service requested",
"meaning": "The listener is reachable but does not currently advertise the requested service name.",
"causes": ["wrong SERVICE_NAME", "database/PDB service not registered", "service is stopped"],
"checks": ["run lsnrctl services", "compare requested service with registered services", "check PDB/service state and dynamic registration"]
},
"ORA-12541": {
"title": "TNS: no listener",
"meaning": "The client could not reach an Oracle listener at the requested address/port.",
"causes": ["listener is stopped", "wrong host or port", "firewall/NAT/routing issue"],
"checks": ["run lsnrctl status on the server", "verify host and port", "test TCP reachability from the client"]
}
}
