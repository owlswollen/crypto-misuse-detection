// Hard coded key

class Misuse {
    void key() {
        byte[] key = {1, 2, 3, 4, 5, 6, 7, 8};
        SecretKeySpec spec = new SecretKeySpec(key, "AES");
        Cipher aes = Cipher.getInstance("AES");
        aes.init(Cipher.ENCRYPT_MODE, spec);
        return aesCipher.doFinal(secretData);
    }
}