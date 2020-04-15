/*Before running this sql script, create the zensvcs_ts tablespace.
For the zensvcs_ts tablespace, first create a directory off root, such as /postgres/data.  
Then issue the command 'chown -R postgres:postgres postgres'.  
The chown command recursively (-R) gives postgres read-write permissions on the data directory to store
zensvcs database data.  After these 2 operations you can run the restdemo sql script
that configures the database to host the restdemo application.  Change the restdemo.sql 
to reflect your username. My username is monica.  Change the first 2 sql commands to reflect
your username*/

create database zensvcs_dev owner monica tablespace zensvcs_ts;
create database zensvcs_test owner monica tablespace zensvcs_ts;
\connect zensvcs_test
create schema restdemo;
\connect zensvcs_dev
create schema restdemo;
revoke create on schema public from public;
revoke all on database zensvcs_dev from public;
revoke all on database zensvcs_test from public;
create role readonly;
grant usage on schema restdemo to readonly;
grant select on all tables in schema restdemo to readonly;
create role readwrite;
grant select, insert, update, delete on all tables in schema restdemo to readwrite;
grant usage on all sequences in schema restdemo to readwrite;
create user reporting_user1 with password 'reporting_user1';
grant readonly to reporting_user1;
create user app_user1 with password 'app_user1';
grant readwrite to app_user1;
create user app_user2 with password 'app_user2';
grant readwrite to app_user2;
grant connect on database zensvcs_dev to app_user1;
grant connect on database zensvcs_test to app_user1;
grant connect on database zensvcs_dev to reporting_user1;
grant connect on database zensvcs_test to reporting_user1;
grant connect on database zensvcs_dev to app_user2;
grant connect on database zensvcs_test to app_user2;
