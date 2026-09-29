from client import URIResourceResolver

template = "database://{db}/tables/{table}/rows/{row_id}"
variables = {"db": "analytics_prod", "table": "users", "row_id": "9021"}

expanded = URIResourceResolver.expand_template(template, variables)
print("Expanded MCP URI:", expanded)
matched_vars = URIResourceResolver.match_template(template, expanded)
print("Extracted Variables:", matched_vars)
