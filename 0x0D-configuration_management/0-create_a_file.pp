# Creates a file called dhk in /tmp
file { '/tmp/dhk':
  ensure  => file,
  path    => '/tmp/dhk',
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet'
}
