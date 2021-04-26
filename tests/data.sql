INSERT INTO bad_url (host, port)
VALUES
    ('bad-host.com', 8899);

INSERT INTO bad_url (host, port, path)
VALUES
    ('grey-host.com', 8231, 'free-mony.html'),
    ('grey-host.com', 8231, 'a/path/with/several/levels.html');
