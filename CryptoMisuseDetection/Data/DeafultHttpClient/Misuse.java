// DefaultHttpClient with default constructor is not compatible with TLS 1.2

class Misuse {
    HttpClient client = new DefaultHttpClient();
}