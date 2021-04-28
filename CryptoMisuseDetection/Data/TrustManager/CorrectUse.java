// TrustMangager based on a keystore

class CorrectUse implements X509TrustManager {

    public void generateTrustManager() {
        KeyStore ks; // Load keystore containing the certificates trusted

        SSLContext sc = SSLContext.getInstance("TLS");

        TrustManagerFactory tmf = TrustManagerFactory.getInstance("SunX509");
        tmf.init(ks);

        sc.init(kmf.getKeyManagers(), tmf.getTrustManagers(), null);
    }
}