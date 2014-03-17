package Regexp::Common::balanced; {

use strict;
local $^W = 1;

use vars qw /$VERSION/;
($VERSION) = q $Revision: 2.101 $ =~ /[\d.]+/g;

use Regexp::Common qw /pattern clean no_defaults/;

my %closer = ( '{'=>'}', '('=>')', '['=>']', '<'=>'>' );
my $count = -1;
my %cache;

sub nested {
    local $^W = 1;
    my ($start, $finish) = @_;

    return $Regexp::Common::balanced [$cache {$start} {$finish}]
            if exists $cache {$start} {$finish};

    $count ++;
    my $r = '(??{$Regexp::Common::balanced ['. $count . ']})';

    my @starts   = map {s/\\(.)/$1/g; $_} grep {length}
                        $start  =~ /([^|\\]+|\\.)+/gs;
    my @finishes = map {s/\\(.)/$1/g; $_} grep {length}
                        $finish =~ /([^|\\]+|\\.)+/gs;

    push @finishes => ($finishes [-1]) x (@starts - @finishes);

    my @re;
    local $" = "|";
    foreach my $begin (@starts) {
        my $end = shift @finishes;

        my $qb  = quotemeta $begin;
        my $qe  = quotemeta $end;
        my $fb  = quotemeta substr $begin => 0, 1;
        my $fe  = quotemeta substr $end   => 0, 1;

        my $tb  = quotemeta substr $begin => 1;
        my $te  = quotemeta substr $end   => 1;

        use re 'eval';

        my $add;
        if ($fb eq $fe) {
            push @re =>
                   qr /(?:$qb(?:(?>[^$fb]+)|$fb(?!$tb)(?!$te)|$r)*$qe)/;
        }
        else {
            my   @clauses =  "(?>[^$fb$fe]+)";
            push @clauses => "$fb(?!$tb)" if length $tb;
            push @clauses => "$fe(?!$te)" if length $te;
            push @clauses =>  $r;
            push @re      =>  qr /(?:$qb(?:@clauses)*$qe)/;
        }
    }

    $cache {$start} {$finish} = $count;
    $Regexp::Common::balanced [$count] = qr/@re/;
}


pattern name    => [qw /balanced -parens=() -begin= -end=/],
        create  => sub {
            my $flag = $_[1];
            unless (defined $flag -> {-begin} && length $flag -> {-begin} &&
                    defined $flag -> {-end}   && length $flag -> {-end}) {
                my @open  = grep {index ($flag->{-parens}, $_) >= 0}
                             ('[','(','{','<');
                my @close = map {$closer {$_}} @open;
                $flag -> {-begin} = join "|" => @open;
                $flag -> {-end}   = join "|" => @close;
            }
            my $pat = nested @$flag {qw /-begin -end/};
            return exists $flag -> {-keep} ? qr /($pat)/ : $pat;
        },
        version => 5.006,
        ;

}

1;
#
#     Copyright (c) 2001 - 2003, Damian Conway. All Rights Reserved.
#       This module is free software. It may be used, redistributed
#      and/or modified under the terms of the Perl Artistic License
#            (see http://www.perl.com/perl/misc/Artistic.html)
