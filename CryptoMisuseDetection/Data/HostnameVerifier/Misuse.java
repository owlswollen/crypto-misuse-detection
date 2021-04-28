// HostnameVerifier that accept any signed certificates

public class Misuse implements HostnameVerifier {
    public boolean verify(final String hostname, final SSLSession session) {
        return true;
    }
}