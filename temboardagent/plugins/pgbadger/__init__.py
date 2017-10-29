"""
A simple plugin to generate and fetch pgBadger reports

WARNING : WIP
"""

import sys
import subprocess

from temboardagent.routing import add_route
from temboardagent.api_wrapper import (
    api_function_wrapper,
    api_function_wrapper_pg,
)
from temboardagent.tools import validate_parameters
from temboardagent.errors import HTTPError


def version(config, http_context):
    """
    Return the version of pgBadger or an error if pgBadger is not installed 

    Usage:
    $ export XSESSION=`curl -s -k -X POST --data '{"username":"<user>", "password":"<password>"}' https://localhost:2345/login | sed -E "s/^.+\"([a-f0-9]+)\".+$/\1/"`
    $ curl -s -k -H "X-Session:$XSESSION" "https://localhost:2345/hello" | python -m json.tool
    {
         "version": "pgBadger version 3.3\n"
    }
    """  # noqa
    try:
    	version = subprocess.check_output(["pgbadger", "--version"])
    except subprocess.CalledProcessError, e:
	raise HTTPError(402,"%s" % e)

    return {"version": version.rstrip()}


@add_route('GET', '/pgbadger/version')
def get_version(http_context,
              queue_in=None,
              config=None,
              sessions=None,
              commands=None):
    """
    Parameters:
        http_context: HTTP context containing HTTP paramaters and variables.
        queue_in: Task queue to schedule asynchronous job.
        config: Agent configuration.
        sessions: List of current sessions.
        commands: List of current commands (async. jobs).
    """
    return api_function_wrapper(config,
                                http_context,
                                sessions,
                                sys.modules[__name__],
                                'version')


