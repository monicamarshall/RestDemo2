monicarhvm=# \c - monicarhvm
You are now connected to database "monicarhvm" as user "monicarhvm".
monicarhvm=# create database zensvcs_dev owner monicarhvm;
CREATE DATABASE
monicarhvm=# create database zensvcs_test owner monicarhvm;
CREATE DATABASE
monicarhvm=# \connect zensvcs_test
You are now connected to database "zensvcs_test" as user "monicarhvm".
zensvcs_test=# create schema restdemo;
CREATE SCHEMA
zensvcs_test=# \connect zensvcs_dev
You are now connected to database "zensvcs_dev" as user "monicarhvm".
zensvcs_dev=# create schema restdemo;
CREATE SCHEMA

zensvcs_dev=# create tablespace zensvcs_dev_ts owner monicarhvm location '/home/monicarhvm/postgres/tablespaces';
ERROR:  could not set permissions on directory "/home/monicarhvm/postgres/tablespaces": Permission denied

zensvcs_dev=# revoke create on schema public from public;
REVOKE
zensvcs_dev=# revoke all on database zensvcs_dev from public;
REVOKE
zensvcs_dev=# revoke all on database zensvcs_test from public;
REVOKE
zensvcs_dev=# create role readonly;
CREATE ROLE
zensvcs_dev=# grant usage on schema restdemo to readonly;
GRANT
zensvcs_dev=# grant select on all tables in schema restdemo to readonly;
GRANT
zensvcs_dev=# create role readwrite;
CREATE ROLE
zensvcs_dev=# grant select, insert, update, delete on all tables in schema restdemo to readwrite;
GRANT
zensvcs_dev=# grant usage on all sequences in schema restdemo to readwrite;
GRANT
zensvcs_dev=# create user reporting_user1 with password 'reporting_user1';
CREATE ROLE
zensvcs_dev=# grant readonly to reporting_user1;
GRANT ROLE
zensvcs_dev=# create user app_user1 with password 'app_user1';
CREATE ROLE
zensvcs_dev=# grant readwrite to app_user1;
GRANT ROLE
zensvcs_dev=# create user app_user2 with password 'app_user2';
CREATE ROLE
zensvcs_dev=# grant readwrite to app_user2;
GRANT ROLE
zensvcs_dev=# grant connect on database zensvcs_dev to app_user1;
GRANT
zensvcs_dev=# grant connect on database zensvcs_test to app_user1;
GRANT
zensvcs_dev=# grant connect on database zensvcs_dev to reporting_user1;
GRANT
zensvcs_dev=# grant connect on database zensvcs_test to reporting_user1;
GRANT
zensvcs_dev=# grant connect on database zensvcs_dev to app_user2;
GRANT
zensvcs_dev=# grant connect on database zensvcs_test to app_user2;
GRANT


