postgres=# create user master;create role
CREATE ROLE
postgres=# ALTER USER master WITH CREATEDB;
ALTER ROLE
postgres=# ALTER USER master SUPERUSER;
ALTER ROLE
postgres=# ALTER USER master WITH CREATEROLE;
ALTER ROLE
postgres=# ALTER USER master WITH REPLICATION;
ALTER ROLE
postgres=# create user monicadba login password 'monicasu' in role master inherit;
CREATE ROLE
postgres=# \c - monicadba
FATAL:  Peer authentication failed for user "monicadba"
Previous connection kept
postgres=# \conninfo
You are connected to database "postgres" as user "postgres" via socket in "/var/run/postgresql" at port "5432".

bash-4.2$ history | grep vi
    9  vi /var/lib/pgsql/12/data/pg_hba.conf
   16  sudo systemctl restart postgresql-12.service
   17  systemctl restart postgresql-12.service
   42  vi /etc/postgresql/12/main/pg_hba.conf
   51  vi /var/lib/pgsql/12/data/pg_hba.conf
   52  systemctl restart postgresql-12.service
   57  vi /var/lib/pgsql/12/data/pg_hba.conf
   62  vi /var/lib/pgsql/12/data/pg_hba.conf
   63  sudo systemctl restart postgresql-12.service
   64  systemctl restart postgresql-12.service
   69  vi /var/lib/pgsql/12/data/pg_hba.conf
   70  systemctl restart postgresql-12.service
   75  history | grep vi

[monicarhvm@rhel77 ~]$ netstat -nlp | grep 5432
(Not all processes could be identified, non-owned process info
 will not be shown, you would have to be root to see it all.)
tcp        0      0 0.0.0.0:5432            0.0.0.0:*               LISTEN      -                   
tcp6       0      0 :::5432                 :::*                    LISTEN      -                   
unix  2      [ ACC ]     STREAM     LISTENING     25058    -                    /tmp/.s.PGSQL.5432
unix  2      [ ACC ]     STREAM     LISTENING     24927    -                    /var/run/postgresql/.s.PGSQL.5432
[monicarhvm@rhel77 ~]$ 
[monicarhvm@rhel77 ~]$ vi /var/lib/pgsql/12/data/postgresql.conf

# TYPE  DATABASE        USER            ADDRESS                 METHOD

# "local" is for Unix domain socket connections only
local   all             postgres                                md5

local   all             monicadba                               md5
local   all             all                                     peer
# IPv4 local connections:
host    all             all             127.0.0.1/32            md5
# IPv6 local connections:
host    all             all             ::1/128                 md5
# Allow replication connections from localhost, by a user with the
# replication privilege.
local   replication     all                                     peer
host    replication     all             127.0.0.1/32            ident
host    replication     all             ::1/128                 ident
host    all             all             0.0.0.0/0               md5
host    all             all             ::/0                    md5








