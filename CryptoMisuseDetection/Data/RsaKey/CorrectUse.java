// at least 2048 bit key size

class CorrectUse {
    void rsaKey() {
        KeyPairGenerator keyGen = KeyPairGenerator.getInstance("RSA");
        keyGen.initialize(2048);
    }
}