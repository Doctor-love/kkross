# kkross
#### Cross-site attack tool for redteams (and skiddies)

**WORK IN PROGRESS**


## Introduction
kkross enables it's users to exploit various types of known Cross-Site vulnerabilities,
such as XSS, CSRF, CSWSH and similar, without prior knowledge of the specific vulnerabilities. 

It is similar to the Metasploit framework,
except that it does not get involved payload generation or post-exploitation activities.

Exploit modules, which describes how vulnerabilities can be exploited and user controllable options,
are defined in a [straight forward YAML structure independent of kkross](https://github.com/doctor-love/xs_exploits).

kkross can currently be used as a Python 3 module or a interactive CLI.  


## Dependencies
The application requires Python 3.x with the standard library and the third-party module "jinja2".
The interactive command line interface also requires the "cmd2" module.
