// RSA usage with short key

class Misuse {
    void rsaKey() {
        KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA");
        keyGen.initialize(512);
    }
}