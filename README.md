This repo contains a Flask based web-service which authorizes URLs.  The
request has the following format:

- GET /urlinfo/1/{hostname_and_port}/{original_path_and_query_string}

For example:

- GET /urlinfo/1/bad-host.org:8080/free-money.html

If the URL is in the database (i.e. suspected malicious) it returns a
`403 - Forbidden` response.  Otherwise, it returns a `204 - No Content`.
"No Content" is returned to keep the response simple.  Richer responses
may be added in the future.
