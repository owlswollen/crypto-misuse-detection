// SSL Socket

class CorrectUse {
    Socket soc = SSLSocketFactory.getDefault().createSocket("www.google.com", 443);
}