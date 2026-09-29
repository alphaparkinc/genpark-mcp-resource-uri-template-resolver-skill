"""MCP Resource URI Template Resolver.
100% Python Standard Library.
"""

import re

class URIResourceResolver:
    """RFC 6570 URI template resolution and parameter extraction for MCP resources."""
    @staticmethod
    def expand_template(template, variables):
        res = template
        for k, v in variables.items():
            res = res.replace(f"{{{k}}}", str(v))
        return res

    @staticmethod
    def match_template(template, uri):
        regex = re.sub(r"\{(\w+)\}", r"(?P<\1>[^/]+)", template)
        match = re.match(f"^{regex}$", uri)
        if match:
            return match.groupdict()
        return None
