// Don't keep cryptographic keys in the source code

class CorrectUse {
    void key() {
        byte[] key; // Load key from outside
        SecretKeySpec spec = new SecretKeySpec(key, "AES");
        Cipher aes = Cipher.getInstance("AES");
        aes.init(Cipher.ENCRYPT_MODE, spec);
        return aesCipher.doFinal(secretData);
    }
}