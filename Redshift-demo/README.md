# Redshift命令操作

>查询所有表详细信息

```bash
select * from SVV_TABLE_INFO ORDER BY size desc;
```

```bash
analyze compression tablename;
```

Redshift has very fast I/O, so that opeation should take less than 1 second for any cluster type or size. As diemacht said, the issue is caused because you have another connection with an open transaction.

I had a similar issue: A crash on the client left a transaction 'open' but unreacheable. No db locks appeared on the STV_LOCKS table: using

```bash
select table_id, last_update, lock_owner, lock_owner_pid from stv_locks;
```

Also, no query was still running: checked with

```bash
select pid, trim(user_name), starttime, query , substring(query,1,20), status from stv_recents where status='Running';
```

So the solution was to list the user sessions

```bash
SELECT * FROM STV_SESSIONS
```

And then kill it using

```bash
SELECT pg_terminate_backend(pid)
```
