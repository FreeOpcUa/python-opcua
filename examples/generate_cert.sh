openssl req -x509 -newkey rsa:2048 -keyout mykey.pem -out server_cert.pem -days 355 -nodes
openssl x509 -outform der -in server_cert.pem -out server_cert.der
