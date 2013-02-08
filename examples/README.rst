::

    virtualenv .
    . bin/activate
    pip install -r requirements.txt


domain name::

    vim /etc/hosts
    # 127.0.0.1 client.local

::

    python runserver.py

Add client (just leave RSA public key blank). Set credentials in plaintext_client.py::

    python plaintext_client.py

