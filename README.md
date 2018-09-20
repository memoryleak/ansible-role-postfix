memoryleak.postfix
==================

A simple role to install and manage postfix.

Requirements
------------
No special requirements.

Role Variables
--------------
```
# Path to main.cf file.
postifx_main_config_file: /etc/postfix/main.cf
```
```
# Change or set configuration options in the main.cf file.
postifx_main_config
```
```
# Location of passwd file.
postifx_sasl_passwd_file: /etc/postfix/sasl_passwd
```
```
# postifx_sasl_passwd:
postifx_sasl_passwd: []
```

```
# Location of virtual alias file.
postfix_virtual_alias_maps_file: /etc/postfix/virtual
```
```
# Postfix alias map values.
postfix_virtual_alias_maps: []
```

Dependencies
------------

If you want to run the tests, get molecule set up.

Example Playbook
----------------

```
- hosts: all
  roles:
    - role: memoryleak.postfix
      postfix_virtual_alias_maps_file: /etc/postfix/virtual
      postifx_sasl_passwd_file: /etc/postfix/sasl_passwd
      postifx_main_config:
        - name: relayhost
          value: "[localhost]:25"
          state: present

        - name: smtp_sasl_auth_enable
          value: "yes"
          state: present

        - name: smtp_sasl_security_options
          value: noanonymous
          state: present

        - name: smtp_sasl_password_maps
          value: hash:/etc/postfix/sasl_passwd
          state: present

        - name: smtp_use_tls
          value: "yes"
          state: present

        - name: smtp_tls_security_level
          value: encrypt
          state: present

        - name: smtp_tls_note_starttls_offer
          value: "yes"
          state: present

        - name: -o smtp_fallback_relay
          value: ""
          state: absent

        - name: virtual_alias_maps
          value: regexp:/etc/postfix/virtual
          state: present

        - name: virtual_alias_domains
          value: ""
          state: present

        - name: inet_interfaces
          value: all
          state: present

        - name: inet_protocol
          value: ipv4
          state: present

      postifx_sasl_passwd:
        - host: localhost
          port: 25
          username: hello
          password: secret

      postfix_virtual_alias_maps:
        - alias: /^.+$/
          value: hello@example.com

```

License
-------

BSD

Author Information
------------------

Haydar Ciftci <haydar.ciftci@gmail.com>
