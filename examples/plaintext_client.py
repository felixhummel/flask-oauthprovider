from client import app
app.config["OAUTH_CREDENTIALS"] = {
    u"client_secret": u"ZDaxszXUOUc1cyH4RrGtjVpNm78q9g",
    u"signature_method": u"PLAINTEXT"
}
app.config["CLIENT_KEY"] = u"EDwsTDy5SN1pdBF1hZ8De37oyfxzpJ"
app.run(debug=True, port=5001, host='0.0.0.0')
