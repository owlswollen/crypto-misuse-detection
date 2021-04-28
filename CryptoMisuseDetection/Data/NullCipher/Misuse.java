// NullCipher is insecure

class Misuse {
    void cipher() {
        Cipher doNothingCihper = new NullCipher();

        // The ciphertext produced will be identical to the plaintext.
        byte[] cipherText = c.doFinal(plainText);
    }
}