#!/usr/bin/env perl

use POSIX qw(strftime);
use Time::HiRes qw/gettimeofday/;

sub iso8601
{
  my ($s, $f) = split (/\./, gettimeofday);
  strftime ('%Y-%m-%dT%H:%M:%S.'.$f.'Z', gmtime ($s))
}

print '{"msg": "pong", "process": "perl", "created": "' . iso8601 . '"}';
